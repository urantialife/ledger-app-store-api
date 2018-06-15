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
    firmware_final_ver1.device_versions.add(device_ver1)

    firmware_final_ver2 = SeFirmwareFinalVersion.objects.create(
        name="1.4.1",
        version=int.from_bytes(bytes([0, 1, 4, 1]), 'big')
        notes=None,
        perso="perso_11",
        firmware="nanos/1.4.1/upgrade_1.4.1",
        firmware_key="nanos/1.4.1/upgrade_1.4.1_key",
        hash="74d10f134677adb030bafce8adb70c6510e7181a9aae509159f904be01edeed2",
        se_firmware=firmware
    )
    firmware_final_ver2.device_versions.add(device_ver5)

    firmware_final_ver3 = SeFirmwareFinalVersion.objects.create(
        name="1.4.2",
        version=int.from_bytes(bytes([0, 1, 4, 2]), 'big')
        notes=None,
        perso="perso_11",
        firmware="nanos/1.4.2/fw_1.4.1/upgrade_1.4.2",
        firmware_key="nanos/1.4.2/fw_1.4.1/upgrade_1.4.2_key",
        hash="8309d76fee0e809f22d4a00960b795ffdc631970cdd4b9c2a547f6c7cad3ea48",
        se_firmware=firmware
    )
    firmware_final_ver3.device_versions.add(device_ver5)
    firmware_final_ver3.providers.add(provider1)

    firmware_final_ver4 = SeFirmwareFinalVersion.objects.create(
        name="1.4.2-das",
        version=int.from_bytes(bytes([0, 1, 4, 2]), 'big')
        notes=None,
        perso="perso_11",
        firmware="nanos/1.4.2-das/upgrade_1.4.2_das",
        firmware_key="nanos/1.4.2-das/upgrade_1.4.2_das_key",
        hash="8309d76fee0e809f22d4a00960b795ffdc631970cdd4b9c2a547f6c7cad3ea48",
        se_firmware=firmware2
    )
    firmware_final_ver4.device_versions.add(device_ver5)
    firmware_final_ver4.providers.add(provider2)

    firmware_final_ver5 = SeFirmwareFinalVersion.objects.create(
        name="1.3.1-das",
        version=int.from_bytes(bytes([0, 1, 3, 1]), 'big')
        notes=None,
        perso="perso_11",
        firmware="",
        firmware_key="",
        hash="",
        se_firmware=firmware2
    )
    firmware_final_ver5.device_versions.add(device_ver1)
    firmware_final_ver5.providers.add(provider2)

# OSU
    firmware_osu_ver1 = SeFirmwareOSUVersion.objects.create(
        name="1.4.2-osu",
        notes="The firmware 1.4.2 update brings several user experience and minor security improvements:\n- User Pin code's start number is now always randomized\n- Each recovery word's first letter is now always randomized\n- Improvement of the interaction between microcontroller (MCU) and secure element to remove confusing error message\n- Verification & checks of installed applications\n- Improved dashboard responsiveness\n\nTo update your device, please [refer to our step by step guide](https://support.ledgerwallet.com/hc/en-us/articles/360002731113).\n\nMore information about the firmware available on [our firmware 1.4.2 FAQ](https://www.ledger.fr/2018/04/17/announcing-ledger-firmware-1-4-2/)\n",
        perso="perso_11",
        firmware="nanos/1.4.2/fw_1.3.1/upgrade_osu_1.4.2",
        firmware_key="nanos/1.4.2/fw_1.3.1/upgrade_osu_1.4.2_key",
        hash="4a1a484f7b57ad41909b2c5115e4cfb69dafb173d0eedf85ea82152deb7d7637",
    )
    firmware_osu_ver1.device_versions.add(device_ver1)
    firmware_osu_ver1.next_se_firmware_final_version.add(firmware_final_ver3)
    firmware_osu_ver1.previous_se_firmware_final_versions.add(
        firmware_final_ver1)

    firmware_osu_ver2 = SeFirmwareOSUVersion.objects.create(
        name="1.4.1-osu",
        notes="",
        perso="perso_11",
        firmware="nanos/1.4.1/upgrade_osu_1.4.1",
        firmware_key="nanos/1.4.1/upgrade_osu_1.4.1_key",
        hash="2e88ef1ce8e01b181a9083950196dd0b99c6240198728b54b18bfe179856f573",
    )
    firmware_osu_ver2.device_versions.add(device_ver1)
    firmware_osu_ver2.next_se_firmware_final_version.add(firmware_final_ver2)
    firmware_osu_ver2.previous_se_firmware_final_versions.add(
        firmware_final_ver1)

    firmware_osu_ver3 = SeFirmwareOSUVersion.objects.create(
        name="1.3.1-osu",
        notes="",
        perso="perso_11",
        firmware="nanos/1.3.1/upgrade_osu_1.3.1",
        firmware_key="nanos/1.3.1/upgrade_osu_1.3.1_key",
        hash="78ef4503452b5810b42e6e715d4fe8ff3765f06758c78eefe3977e1949a12503",
    )
    firmware_osu_ver3.device_versions.add(device_ver1)
    firmware_osu_ver3.next_se_firmware_final_version.add(firmware_final_ver1)

    firmware_osu_ver4 = SeFirmwareOSUVersion.objects.create(
        name="1.4.2-osu",
        notes="The firmware 1.4.2 update brings several user experience and minor security improvements:\n- User Pin code's start number is now always randomized\n- Each recovery word's first letter is now always randomized\n- Improvement of the interaction between microcontroller (MCU) and secure element to remove confusing error message\n- Verification & checks of installed applications\n- Improved dashboard responsiveness\n\nTo update your device, please [refer to our step by step guide](https://support.ledgerwallet.com/hc/en-us/articles/360002731113).\n\nMore information about the firmware available on [our firmware 1.4.2 FAQ](https://www.ledger.fr/2018/04/17/announcing-ledger-firmware-1-4-2/)\n",
        perso="perso_11",
        firmware="nanos/1.4.2/fw_1.4.1/upgrade_osu_1.4.2",
        firmware_key="nanos/1.4.2/fw_1.4.1/upgrade_osu_1.4.2_key",
        hash="fbc17a950ff7576fdb22442cba6b9f32011025b4c331f44b2d6e85811e96d522",
    )
    firmware_osu_ver4.device_versions.add(device_ver5)
    firmware_osu_ver4.next_se_firmware_final_version.add(firmware_final_ver3)
    firmware_osu_ver4.previous_se_firmware_final_versions.add(
        firmware_final_ver2)

    firmware_osu_ver5 = SeFirmwareOSUVersion.objects.create(
        name="1.4.2-das-osu",
        notes=None
        perso="perso_11",
        firmware="nanos/1.4.2-das/upgrade_osu_1.4.2_das",
        firmware_key="nanos/1.4.2-das/upgrade_osu_1.4.2_das_key",
        hash="09C9000000000000000000000000000000000000000000000000000000003DCA",
    )
    firmware_osu_ver5.device_versions.add(device_ver1)
    firmware_osu_ver5.next_se_firmware_final_version.add(firmware_final_ver4)
    firmware_osu_ver5.previous_se_firmware_final_versions.add(
        firmware_final_ver5)
