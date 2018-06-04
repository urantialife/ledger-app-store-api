import json
import semver
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate
from api.serializers import UserSerializer, U2FKeySerializer
from api.serializers import ApplicationVersionSerializer
from api.serializers import ApplicationSerializer, SeFirmwareSerializer
from api.serializers import DeviceVersionSerializer
from api.serializers import DeviceVersionDetailSerializer
from api.serializers import SeFirmwareVersionSerializer, DeviceSerializer
from api.serializers import PublisherSerializer, ProviderSerializer
from api.serializers import CategorySerializer
from api.serializers import McuSerializer, McuVersionSerializer
from api.models import U2FRegistrationRequest, U2FAuthenticationRequest
from api.models import U2FKey, ApplicationVersion, Application
from api.models import SeFirmwareVersion, SeFirmware, DeviceVersion
from api.models import Device, Publisher, Provider, Category
from api.models import Mcu, McuVersion
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, exception_handler
from u2flib_server import u2f


############ APPLICATIONS VIEWS #################

class ApplicationView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationVersionView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ApplicationVersion.objects.all()
    serializer_class = ApplicationVersionSerializer


class ApplicationVersionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ApplicationVersion.objects.all()
    serializer_class = ApplicationVersionSerializer


@api_view(["POST"])
def get_app_to_display(request):
    current_se_firmware_version_id = request.data.get('current_se_firmware_version')
    current_device_version_id = request.data.get('device_version')

    apps_to_display = ApplicationVersion.objects.filter(device_versions__id=current_device_version_id,
                                                        previous_se_firmware_versions__id=current_se_firmware_version_id)

    serializer = ApplicationVersionSerializer(apps_to_display, many=True)
    return Response({"apps": serializer.data})


# @api_view(["POST"])
# def get_app_updates(request):
#     current_se_firmware_version_id = request.data.get('current_se_firmware_version')
#     current_apps_version_list = request.data.get('current_application_versions')
#     current_device_version_id = request.data.get('device_version')
#     providers_id_list = request.data.get('providers')
#
#     next_se_app_versions = None
#     for app_ver_id in current_apps_version_list:
#         app_ver = get_object_or_404(ApplicationVersion, id=app_ver_id)
#         next_se_app_versions = ApplicationVersion.objects.filter(device_versions__id=current_device_version_id,
#                                                                  previous_se_firmware_versions__id=current_se_firmware_version_id
#                                                                  )


############ FIRMWARES VIEWS #################

class SeFirmwareView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SeFirmware.objects.all()
    serializer_class = SeFirmwareSerializer


class SeFirmwareDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SeFirmware.objects.all()
    serializer_class = SeFirmwareSerializer


class SeFirmwareVersionView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SeFirmwareVersion.objects.all()
    serializer_class = SeFirmwareVersionSerializer


class SeFirmwareVersionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SeFirmwareVersion.objects.all()
    serializer_class = SeFirmwareVersionSerializer


@api_view(["POST"])
def se_firmware_version_by_name_and_device(request):
    se_firmware_version_name = request.data.get('se_firmware_name')
    if 'device_version' in request.data:
        device_version_id = request.data.get('device_version')
        se_firmware_ver = get_object_or_404(SeFirmwareVersion, name=se_firmware_version_name, device_versions__id=device_version_id)
    else:
        target_id = request.data.get('target_id')
        device_ver = get_object_or_404(DeviceVersion, target_id=target_id)
        se_firmware_ver = get_object_or_404(SeFirmwareVersion, name=se_firmware_version_name, device_versions=device_ver)

    serializer = SeFirmwareVersionSerializer(se_firmware_ver)
    return Response(serializer.data)


@api_view(["POST"])
def get_latest(request):
    current_se_firmware_version_id = request.data.get('current_se_firmware_version')
    current_device_version_id = request.data.get('device_version')
    providers_id_list = request.data.get('providers')

    next_se_firmware_versions = None
    for prov_id in providers_id_list:
        try:
            next_se_firmware_versions = SeFirmwareVersion.objects.filter(device_versions__id=current_device_version_id,
                                                                         previous_se_firmware_versions__id=current_se_firmware_version_id,
                                                                         providers=prov_id
                                                                         )
            break
        except SeFirmwareVersion.DoesNotExist:
            continue
    if not next_se_firmware_versions:
        return Response({"se_firmware_version": {}, "result": "null"})

    res_firm_ver = None
    for firm_ver in next_se_firmware_versions:
        if res_firm_ver is not None:
            if semver.compare(res_firm_ver.name, firm_ver.name) == 1:
                break
        else:
            res_firm_ver = firm_ver

    serializer = SeFirmwareVersionSerializer(res_firm_ver)
    return Response({"se_firmware_version": serializer.data, "result": "success"})


############ DEVICES VIEWS #################

class DeviceView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceVersionView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = DeviceVersion.objects.all()
    serializer_class = DeviceVersionSerializer


class DeviceVersionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = DeviceVersion.objects.all()
    serializer_class = DeviceVersionSerializer


class DeviceVersionDetailList(generics.ListAPIView):
    queryset = DeviceVersion.objects.all()
    serializer_class = DeviceVersionDetailSerializer


@api_view(["GET"])
def device_by_target_id(request, target_id):
    device_ver = get_object_or_404(DeviceVersion, target_id=target_id)

    serializer = DeviceVersionSerializer(device_ver)
    return Response(serializer.data)


############ PUBLISHER VIEWS ################


class PublisherView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PublisherSerializer


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PublisherSerializer


############ MCU VIEWS ################


class McuView(generics.ListCreateAPIView):
    queryset = Mcu.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = McuSerializer


class McuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mcu.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = McuSerializer


class McuVersionView(generics.ListCreateAPIView):
    queryset = McuVersion.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = McuVersionSerializer


class McuVersionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = McuVersion.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = McuVersionSerializer


@api_view(["POST"])
def mcu_version_by_bootloader_version(request):
    bootloader_version = request.data.get('bootloader_version')
    # device_version_id = request.data.get('device_version')

    try:
        mcu_ver = McuVersion.objects.get(from_bootloader_version=bootloader_version)
    except McuVersion.DoesNotExist:
        return Response("default")

    serializer = McuVersionSerializer(mcu_ver)
    return Response(serializer.data)


############ PROVIDER VIEWS ################


class ProviderView(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProviderSerializer


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProviderSerializer


############ CATEGORY VIEWS ################


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CategorySerializer


############ USERS VIEWS ################

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserSerializer


class RegisterKey(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        # request = u2f.begin_registration(self.get_origin(), [
        #     key for key in user.u2f_key.all()
        # ])
        if user.u2f_key.exists():
            return Response(
                {"error": "conflict with already registered key"},
                status=HTTP_409_CONFLICT
            )
        if user.u2f_registration_request.exists():
            user.u2f_registration_request.first().delete()

        reg_request = u2f.begin_registration(settings.APP_ID, [])
        U2FRegistrationRequest.objects.create(
            user=user, body=json.dumps(reg_request))
        return Response(reg_request.data_for_client)

    def post(self, request, format=None):
        user = request.user
        response = request.data.get('response')

        reg_req = get_object_or_404(U2FRegistrationRequest, user=user)
        reg_request = json.loads(reg_req.body)

        device, attestation_cert = u2f.complete_registration(
            reg_request, response)
        U2FKey.objects.create(
            user=user,
            publicKey=device['publicKey'],
            keyHandle=device['keyHandle'],
            appId=device['appId'],
        )
        reg_req.delete()
        return Response({"resp": "success"})


@api_view(["POST"])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if not user:
        return Response(
            {"error": "Login failed"},
            status=HTTP_401_UNAUTHORIZED
        )

    if user.u2f_key.exists():
        if user.u2f_authentication_request.exists():
            user.u2f_authentication_request.first().delete()

        serializer = U2FKeySerializer(user.u2f_key.first())

        sign_request = u2f.begin_authentication(
            settings.APP_ID, [serializer.data])
        U2FAuthenticationRequest.objects.create(
            user=user, body=json.dumps(sign_request))
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
        device, counter, _ = u2f.complete_authentication(
            json_auth_req, response)
        # TODO: store login_counter and verify it's increasing
        device = user.u2f_key.get(keyHandle=device['keyHandle'])
        device.last_used_at = timezone.now()
        device.save()
        auth_req.delete()
    except ValueError:
        return Response({"error": "U2F validation failed -- bad signature"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})
