import django
import os
import semver
from api.models import *

os.environ['DJANGO_SETTINGS_MODULE'] = 'ledger_app_store.settings'
django.setup()

if __name__ == '__main__':
    provider1 = Provider.objects.create(name="Ledger Live")
    provider2 = Provider.objects.create(name="DAS")

    # DEVICE CREATION

    device1 = Device.objects.create(name="Ledger Nano S")
    device2 = Device.objects.create(name="Ledger Blue")
    device3 = Device.objects.create(name="Ledger Aramis")

    device_ver1 = DeviceVersion.objects.create(
        name="nanos",
        target_id=823132162,
        device=device1
    )
    device_ver1.provider.add(provider1, provider2)
    device_ver2 = DeviceVersion.objects.create(
        name="blue_2",
        target_id=822083586,
        device=device2
    )
    device_ver3 = DeviceVersion.objects.create(
        name="blue_1",
        target_id=822083585,
        device=device2
    )
    device_ver4 = DeviceVersion.objects.create(
        name="aramis",
        target_id=824180738,
        device=device3
    )
    device_ver5 = DeviceVersion.objects.create(
        name="nanos-1.4",
        target_id=823132163,
        device=device1
    )

    # FIRMWARE CREATION

    firmware = SeFirmware.objects.create(name="Ledger nano S")
    firmware2 = SeFirmware.objects.create(name="DAS firmware")
    firmware3 = SeFirmware.objects.create(name="Bitclub firmware")

    firmware_final_ver1 = SeFirmwareFinalVersion.objects.create(
        name="1.3.1",
        version=int.from_bytes(bytes([0, 1, 3, 1]), 'big')
        notes=None,
        perso="perso_11",
        firmware="nanos/1.3.1/upgrade_1.3.1",
        firmware_key="nanos/1.3.1/upgrade_1.3.1_key",
        hash="74d10f134677adb030bafce8adb70c6510e7181a9aae509159f904be01edeed2",
        se_firmware=firmware
    )
    firmware_ver1.device_versions.add(device_ver1)

    firmware_ver2 = SeFirmwareFinalVersion.objects.create(
        name="1.4.1",
        version=int.from_bytes(bytes([0, 1, 4, 1]), 'big')
        notes=None,
        perso="perso_11",
        firmware="nanos/1.4.1/upgrade_1.4.1",
        firmware_key="nanos/1.4.1/upgrade_1.4.1_key",
        hash="74d10f134677adb030bafce8adb70c6510e7181a9aae509159f904be01edeed2",
        se_firmware=firmware
    )
    firmware_ver2.device_versions.add(device_ver5)

    firmware_ver3 = SeFirmwareFinalVersion.objects.create(
        name="1.4.2",
        version=int.from_bytes(bytes([0, 1, 4, 2]), 'big')
        notes=None,
        perso="perso_11",
        firmware="nanos/1.4.2/fw_1.4.1/upgrade_1.4.2",
        firmware_key="nanos/1.4.2/fw_1.4.1/upgrade_1.4.2_key",
        hash="8309d76fee0e809f22d4a00960b795ffdc631970cdd4b9c2a547f6c7cad3ea48",
        se_firmware=firmware
    )
    firmware_ver3.device_versions.add(device_ver5)
    firmware_ver3.providers.add(provider1)

    firmware_ver4 = SeFirmwareFinalVersion.objects.create(
        name="1.4.2-das",
        version=int.from_bytes(bytes([0, 1, 4, 2]), 'big')
        notes=None,
        perso="perso_11",
        firmware="nanos/1.4.2-das/upgrade_1.4.2_das",
        firmware_key="nanos/1.4.2-das/upgrade_1.4.2_das_key",
        hash="8309d76fee0e809f22d4a00960b795ffdc631970cdd4b9c2a547f6c7cad3ea48",
        se_firmware=firmware2
    )
    firmware_ver4.device_versions.add(device_ver5)
    firmware_ver4.providers.add(provider2)

    firmware_ver5 = SeFirmwareFinalVersion.objects.create(
        name="1.3.1-das",
        version=int.from_bytes(bytes([0, 1, 3, 1]), 'big')
        notes=None,
        perso="perso_11",
        firmware="",
        firmware_key="",
        hash="",
        se_firmware=firmware2
    )
    firmware_ver5.device_versions.add(device_ver1)
    firmware_ver5.providers.add(provider2)
