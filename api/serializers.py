from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import U2FKey, SeFirmwareVersion, Application, ApplicationVersion, Device, DeviceVersion


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


class SeFirmwareVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeFirmwareVersion
        fields = ('id',
                  'name',
                  'notes',
                  'bolos_version_min',
                  'bolos_version_max',
                  'final_perso',
                  'final_target_id',
                  'final_firmware',
                  'final_firmware_key',
                  'final_hash',
                  'osu_perso',
                  'osu_target_id',
                  'osu_firmware',
                  'osu_firmware_key',
                  'osu_hash',
                  'date_creation'
                  )


class ApplicationVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationVersion
        fields = ('id',
                  'name',
                  'notes',
                  'icon',
                  'bolos_version_min',
                  'bolos_version_max',
                  'perso',
                  'target_id',
                  'firmware',
                  'firmware_key',
                  'hash',
                  'date_creation',
                  'delete',
                  'delete_key'
                  )


class ApplicationSerializer(serializers.ModelSerializer):
    app_version = ApplicationVersionSerializer(many=True)

    class Meta:
        model = Application
        fields = ('name', 'description', 'app_version')


class DeviceVersionDetailSerializer(serializers.ModelSerializer):
    app_version = ApplicationVersionSerializer(many=True)
    se_firmware_version = SeFirmwareVersionSerializer(many=True)

    class Meta:
        model = DeviceVersion
        fields = ('id',
                  'name',
                  'target_id',
                  'description',
                  'app_version',
                  'se_firmware_version',
                  'date_creation'
                  )


class DeviceVersionSerializer(serializers.ModelSerializer):
    # app_version = ApplicationVersionSerializer(many=True)
    # se_firmware_version = SeFirmwareVersionSerializer(many=True)

    class Meta:
        model = DeviceVersion
        fields = ('id',
                  'name',
                  'target_id',
                  'description',
                  'date_creation'
                  )


class DeviceSerializer(serializers.ModelSerializer):
    device_version = DeviceVersionSerializer(many=True)

    class Meta:
        model = Device
        fields = ('name', 'description', 'device_version')
