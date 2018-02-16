from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import U2FKey


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class U2FKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = U2FKey
        fields = ('public_key', 'key_handle', 'app_id', 'version')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['publicKey'] = ret.pop('public_key')
        ret['keyHandle'] = ret.pop('key_handle')
        ret['appId'] = ret.pop('app_id')
        return ret