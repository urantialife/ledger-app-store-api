import json
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate
from api.serializers import UserSerializer, U2FKeySerializer
from api.models import U2FRegistrationRequest, U2FAuthenticationRequest, U2FKey
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from u2flib_server import u2f


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterKey(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        # request = u2f.begin_registration(self.get_origin(), [
        #     key for key in user.u2f_key.all()
        # ])
        if user.u2f_key.exists():
            return Response({"error": "conflict with already registered key"}, status=HTTP_409_CONFLICT)
        if user.u2f_registration_request.exists():
            user.u2f_registration_request.first().delete()

        reg_request = u2f.begin_registration(settings.APP_ID, [])
        U2FRegistrationRequest.objects.create(user=user, body=json.dumps(reg_request))
        return Response(reg_request.data_for_client)

    def post(self, request, format=None):
        user = request.user
        response = request.data.get('response')

        reg_req = get_object_or_404(U2FRegistrationRequest, user=user)
        reg_request = json.loads(reg_req.body)

        device, attestation_cert = u2f.complete_registration(reg_request, response)
        U2FKey.objects.create(
            user=user,
            public_key=device['publicKey'],
            key_handle=device['keyHandle'],
            app_id=device['appId'],
        )
        reg_req.delete()
        return Response({"resp": "success"})


@api_view(["POST"])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    if user.u2f_key.exists():
        if user.u2f_authentication_request.exists():
            user.u2f_authentication_request.first().delete()

        serializer = U2FKeySerializer(user.u2f_key.first())

        sign_request = u2f.begin_authentication(settings.APP_ID, [serializer.data])
        U2FAuthenticationRequest.objects.create(user=user, body=json.dumps(sign_request))
        return Response(sign_request.data_for_client)
    else:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


@api_view(["POST"])
def finish_login(request):
    username = request.data.get('username')
    response = request.data.get('response')

    user = get_object_or_404(User, username=username)
    auth_req = get_object_or_404(U2FAuthenticationRequest, user=user)

    json_auth_req = json.loads(auth_req.body)

    try:
        device, counter, _ = u2f.complete_authentication(json_auth_req, response)
        # TODO: store login_counter and verify it's increasing
        device = user.u2f_keys.get(key_handle=device['keyHandle'])
        device.last_used_at = timezone.now()
        device.save()
        auth_req.delete()
    except ValueError:
        return Response({"error": "U2F validation failed -- bad signature"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


@api_view(["GET"])
@permission_classes((IsAuthenticated, ))
def protected(request):
    return Response({"resp": "success"})