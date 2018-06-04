from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import U2FKey, SeFirmwareVersion, Application
from api.models import ApplicationVersion, Device, DeviceVersion, SeFirmware
from api.models import Publisher, Provider, Category, Mcu, McuVersion


# VERSION RESOURCES SERIALIZERS

class SeFirmwareVersionSerializer(serializers.ModelSerializer):
    providers = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=Provider.objects.all(),
    )

    se_firmware = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=SeFirmware.objects.all(),
    )

    device_versions = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=DeviceVersion.objects.all(),
    )

    previous_se_firmware_versions = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=SeFirmwareVersion.objects.all(),
    )

    mcu_versions = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    application_versions = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = SeFirmwareVersion
        fields = (
            'id',
            'name',
            'se_firmware',
            'description',
            'display_name',
            'notes',
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
            'date_creation',
            'date_last_modified',
            'device_versions',
            'mcu_versions',
            'application_versions',
            'previous_se_firmware_versions',
            'providers',
        )


class ApplicationVersionSerializer(serializers.ModelSerializer):
    providers = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=Provider.objects.all(),
    )

    app = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Application.objects.all(),
    )

    device_versions = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=DeviceVersion.objects.all(),
    )

    se_firmware_versions = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=SeFirmwareVersion.objects.all()
    )

    class Meta:
        model = ApplicationVersion
        fields = (
            'id',
            'name',
            'app',
            'description',
            'display_name',
            'icon',
            'notes',
            'perso',
            'hash',
            'firmware',
            'firmware_key',
            'delete',
            'delete_key',
            'app',
            'device_versions',
            'se_firmware_versions',
            'providers',
            'date_creation',
            'date_last_modified',
        )


class DeviceVersionSerializer(serializers.ModelSerializer):
    providers = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=Provider.objects.all(),
    )

    device = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Device.objects.all(),
    )

    mcu_versions = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    se_firmware_versions = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    application_versions = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = DeviceVersion
        fields = (
            'id',
            'name',
            'display_name',
            'target_id',
            'description',
            'device',
            'providers',
            'mcu_versions',
            'se_firmware_versions',
            'application_versions',
            'date_creation',
            'date_last_modified',
        )


class DeviceVersionDetailSerializer(serializers.ModelSerializer):
    application_version = ApplicationVersionSerializer(many=True)
    se_firmware_version = SeFirmwareVersionSerializer(many=True)

    class Meta:
        model = DeviceVersion
        fields = (
            'id',
            'name',
            'display_name',
            'target_id',
            'description',
            'application_version',
            'se_firmware_version',
            'date_creation',
            'date_last_modified',
        )


class McuVersionSerializer(serializers.ModelSerializer):
    mcu = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Mcu.objects.all(),
    )

    providers = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=Provider.objects.all(),
    )

    se_firmware_versions = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=SeFirmwareVersion.objects.all(),
    )

    device_versions = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=DeviceVersion.objects.all(),
    )

    class Meta:
        model = McuVersion
        fields = (
            'id',
            'mcu',
            'name',
            'description',
            'providers',
            'device_versions',
            'from_bootloader_version',
            'se_firmware_versions',
            'date_creation',
            'date_last_modified',
        )


# TOP LEVEL RESOURCES SERIALIZERS

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = (
            'id',
            'name',
            'description',
            'date_creation',
            'date_last_modified',
        )


class ApplicationSerializer(serializers.ModelSerializer):
    providers = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=Provider.objects.all(),
    )

    publisher = serializers.PrimaryKeyRelatedField(
        many=False,
        allow_null=True,
        queryset=Publisher.objects.all(),
    )

    category = serializers.PrimaryKeyRelatedField(
        many=False,
        allow_null=True,
        queryset=Category.objects.all(),
    )

    application_versions = ApplicationVersionSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Application
        fields = (
            'id',
            'name',
            'description',
            'application_versions',
            'providers',
            'category',
            'publisher',
            'date_creation',
            'date_last_modified',
        )


class SeFirmwareSerializer(serializers.ModelSerializer):
    providers = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Provider.objects.all(),
        allow_null=True,
    )
    se_firmware_versions = SeFirmwareVersionSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = SeFirmware
        fields = (
            'id',
            'name',
            'description',
            'se_firmware_versions',
            'providers',
            'date_creation',
            'date_last_modified',
        )


class DeviceSerializer(serializers.ModelSerializer):
    device_versions = DeviceVersionSerializer(many=True, read_only=True)

    providers = serializers.PrimaryKeyRelatedField(
        many=True,
        allow_null=True,
        queryset=Provider.objects.all(),
    )

    class Meta:
        model = Device
        fields = (
            'id',
            'name',
            'description',
            'device_versions',
            'providers',
            'date_creation',
            'date_last_modified',
        )


class PublisherSerializer(serializers.ModelSerializer):
    providers = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Provider.objects.all(),
        allow_null=False
    )

    applications = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Publisher
        fields = (
            'id',
            'name',
            'description',
            'providers',
            'date_creation',
            'applications',
            'date_last_modified',
        )


class CategorySerializer(serializers.ModelSerializer):
    providers = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Provider.objects.all(),
        allow_null=True
    )

    applications = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'description',
            'providers',
            'date_creation',
            'applications',
            'date_last_modified',
        )


class McuSerializer(serializers.ModelSerializer):
    providers = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Provider.objects.all(),
        allow_null=True
    )

    mcu_versions = McuVersionSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Mcu
        fields = (
            'id',
            'name',
            'description',
            'providers',
            'mcu_versions',
            'date_creation',
            'date_last_modified',
        )


# U2F SERIALIZERS

class U2FKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = U2FKey
        fields = ('id', 'publicKey', 'keyHandle', 'appId', 'version')


class UserSerializer(serializers.ModelSerializer):
    u2f_key = U2FKeySerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'u2f_key')
