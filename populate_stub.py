import django
import os
import semver

os.environ['DJANGO_SETTINGS_MODULE'] = 'ledger_app_store.settings'
django.setup()
from api.models import *


if __name__ == '__main__':
    provider1 = Provider.objects.create(name="vanilla")
    provider2 = Provider.objects.create(name="das")
    provider3 = Provider.objects.create(name="club")
    provider4 = Provider.objects.create(name="shitcoins")

    # DEVICE CREATION

    device1 = Device.objects.create(name="Ledger Nano S")
    device2 = Device.objects.create(name="Ledger Blue")
    device3 = Device.objects.create(name="Ledger Aramis")

    device_ver0 = DeviceVersion.objects.create(
        name="nanos-club",
        target_id=823132162,
        device=device1
    )
    device_ver0.providers.add(provider3)

    device_ver1 = DeviceVersion.objects.create(
        name="nanos",
        target_id=823132162,
        device=device1
    )
    device_ver1.providers.add(provider1, provider2)

    device_ver2 = DeviceVersion.objects.create(
        name="blue_2",
        target_id=822083586,
        device=device2
    )
    device_ver2.providers.add(provider1)
    device_ver3 = DeviceVersion.objects.create(
        name="blue_1",
        target_id=822083585,
        device=device2
    )
    device_ver3.providers.add(provider1)
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
    device_ver5.providers.add(provider1, provider2)

    # FIRMWARE CREATION
    firmware0 = SeFirmware.objects.create(name="Ledger blue 2 firmware")
    firmware0.providers.add(provider1)
    firmware = SeFirmware.objects.create(name="Ledger nano S firmware")
    firmware.providers.add(provider1)
    firmware2 = SeFirmware.objects.create(name="DAS firmware")
    firmware2.providers.add(provider2)
    firmware3 = SeFirmware.objects.create(name="Bitclub firmware")
    firmware3.providers.add(provider3)

    # FIRMWARE FINAL CREATION
    firmware_final_ver0 = SeFirmwareFinalVersion.objects.create(
        name="2.0.1 blue only",
        version=int.from_bytes(bytes([0, 2, 0, 1]), 'big'),
        perso="perso_11",
        firmware="",
        firmware_key="",
        hash="",
        se_firmware=firmware0
    )
    firmware_final_ver0.device_versions.add(device_ver2)
    firmware_final_ver0.providers.add(provider1)

    firmware_final_ver1 = SeFirmwareFinalVersion.objects.create(
        name="1.3.1",
        version=int.from_bytes(bytes([0, 1, 3, 1]), 'big'),
        perso="perso_11",
        firmware="nanos/1.3.1/upgrade_1.3.1",
        firmware_key="nanos/1.3.1/upgrade_1.3.1_key",
        hash="74d10f134677adb030bafce8adb70c6510e7181a9aae509159f904be01edeed2",
        se_firmware=firmware
    )
    firmware_final_ver1.device_versions.add(device_ver1)
    firmware_final_ver1.providers.add(provider1)

    firmware_final_ver2 = SeFirmwareFinalVersion.objects.create(
        name="1.4.1",
        version=int.from_bytes(bytes([0, 1, 4, 1]), 'big'),
        perso="perso_11",
        firmware="nanos/1.4.1/upgrade_1.4.1",
        firmware_key="nanos/1.4.1/upgrade_1.4.1_key",
        hash="74d10f134677adb030bafce8adb70c6510e7181a9aae509159f904be01edeed2",
        se_firmware=firmware
    )
    firmware_final_ver2.device_versions.add(device_ver5)
    firmware_final_ver2.providers.add(provider1)

    firmware_final_ver3 = SeFirmwareFinalVersion.objects.create(
        name="1.4.2",
        version=int.from_bytes(bytes([0, 1, 4, 2]), 'big'),
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
        version=int.from_bytes(bytes([0, 1, 4, 2]), 'big'),
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
        version=int.from_bytes(bytes([0, 1, 3, 1]), 'big'),
        perso="perso_11",
        firmware="",
        firmware_key="",
        hash="",
        se_firmware=firmware2
    )
    firmware_final_ver5.device_versions.add(device_ver1)
    firmware_final_ver5.providers.add(provider2)

    firmware_final_ver6 = SeFirmwareFinalVersion.objects.create(
        name="1.3.1-club",
        version=int.from_bytes(bytes([0, 1, 3, 1]), 'big'),
        perso="perso_club_10",
        firmware="nanos/1.3.1-club/upgrade_1.3.1_club",
        firmware_key="nanos/1.3.1-club/upgrade_1.3.1_club_key",
        hash="74d10f134677adb030bafce8adb70c6510e7181a9aae509159f904be01edeed2",
        se_firmware=firmware3
    )
    firmware_final_ver6.device_versions.add(device_ver0)
    firmware_final_ver6.providers.add(provider3)

    firmware_final_ver7 = SeFirmwareFinalVersion.objects.create(
        name="1.2.0-club",
        version=int.from_bytes(bytes([0, 1, 2, 0]), 'big'),
        perso="perso_club_10",
        firmware="",
        firmware_key="",
        hash="",
        se_firmware=firmware3
    )
    firmware_final_ver7.device_versions.add(device_ver0)
    firmware_final_ver7.providers.add(provider3)

    # MCU CREATION
    mcu = Mcu.objects.create(name="Ledger")

    mcu11 = McuVersion.objects.create(
        name="1.1",
        mcu=mcu,
        from_bootloader_version=""
    )
    mcu11.device_versions.add(device_ver1)
    mcu11.se_firmware_final_versions.add(
        firmware_final_ver1, firmware_final_ver5)

    mcu15 = McuVersion.objects.create(
        name="1.5",
        mcu=mcu,
        from_bootloader_version="0.6"
    )
    mcu15.device_versions.add(device_ver5)
    mcu15.se_firmware_final_versions.add(
        firmware_final_ver3, firmware_final_ver4)

    mcu06 = McuVersion.objects.create(
        name="0.6",
        mcu=mcu,
        from_bootloader_version="0.0.0"
    )

    # OSU CREATION
    firmware_osu_ver1 = SeFirmwareOSUVersion.objects.create(
        name="1.4.2-osu",
        notes="The firmware 1.4.2 update brings several user experience and minor security improvements:\n- User Pin code's start number is now always randomized\n- Each recovery word's first letter is now always randomized\n- Improvement of the interaction between microcontroller (MCU) and secure element to remove confusing error message\n- Verification & checks of installed applications\n- Improved dashboard responsiveness\n\nTo update your device, please [refer to our step by step guide](https://support.ledgerwallet.com/hc/en-us/articles/360002731113).\n\nMore information about the firmware available on [our firmware 1.4.2 FAQ](https://www.ledger.fr/2018/04/17/announcing-ledger-firmware-1-4-2/)\n",
        perso="perso_11",
        firmware="nanos/1.4.2/fw_1.3.1/upgrade_osu_1.4.2",
        firmware_key="nanos/1.4.2/fw_1.3.1/upgrade_osu_1.4.2_key",
        hash="4a1a484f7b57ad41909b2c5115e4cfb69dafb173d0eedf85ea82152deb7d7637",
        next_se_firmware_final_version=firmware_final_ver3
    )
    firmware_osu_ver1.device_versions.add(device_ver1)
    firmware_osu_ver1.previous_se_firmware_final_versions.add(
        firmware_final_ver1)
    firmware_osu_ver1.providers.add(provider1)

    firmware_osu_ver2 = SeFirmwareOSUVersion.objects.create(
        name="1.4.1-osu",
        notes="",
        perso="perso_11",
        firmware="nanos/1.4.1/upgrade_osu_1.4.1",
        firmware_key="nanos/1.4.1/upgrade_osu_1.4.1_key",
        hash="2e88ef1ce8e01b181a9083950196dd0b99c6240198728b54b18bfe179856f573",
        next_se_firmware_final_version=firmware_final_ver2
    )
    firmware_osu_ver2.device_versions.add(device_ver1)
    firmware_osu_ver2.previous_se_firmware_final_versions.add(
        firmware_final_ver1)
    firmware_osu_ver2.providers.add(provider1)

    firmware_osu_ver3 = SeFirmwareOSUVersion.objects.create(
        name="1.3.1-osu",
        notes="",
        perso="perso_11",
        firmware="nanos/1.3.1/upgrade_osu_1.3.1",
        firmware_key="nanos/1.3.1/upgrade_osu_1.3.1_key",
        hash="78ef4503452b5810b42e6e715d4fe8ff3765f06758c78eefe3977e1949a12503",
        next_se_firmware_final_version=firmware_final_ver1
    )
    firmware_osu_ver3.device_versions.add(device_ver1)
    firmware_osu_ver3.providers.add(provider1)

    firmware_osu_ver4 = SeFirmwareOSUVersion.objects.create(
        name="1.4.2-osu",
        notes="The firmware 1.4.2 update brings several user experience and minor security improvements:\n- User Pin code's start number is now always randomized\n- Each recovery word's first letter is now always randomized\n- Improvement of the interaction between microcontroller (MCU) and secure element to remove confusing error message\n- Verification & checks of installed applications\n- Improved dashboard responsiveness\n\nTo update your device, please [refer to our step by step guide](https://support.ledgerwallet.com/hc/en-us/articles/360002731113).\n\nMore information about the firmware available on [our firmware 1.4.2 FAQ](https://www.ledger.fr/2018/04/17/announcing-ledger-firmware-1-4-2/)\n",
        perso="perso_11",
        firmware="nanos/1.4.2/fw_1.4.1/upgrade_osu_1.4.2",
        firmware_key="nanos/1.4.2/fw_1.4.1/upgrade_osu_1.4.2_key",
        hash="fbc17a950ff7576fdb22442cba6b9f32011025b4c331f44b2d6e85811e96d522",
        next_se_firmware_final_version=firmware_final_ver3
    )
    firmware_osu_ver4.device_versions.add(device_ver5)
    firmware_osu_ver4.previous_se_firmware_final_versions.add(
        firmware_final_ver2)
    firmware_osu_ver4.providers.add(provider1)

    firmware_osu_ver5 = SeFirmwareOSUVersion.objects.create(
        name="1.4.2-das-osu",
        perso="perso_11",
        firmware="nanos/1.4.2-das/upgrade_osu_1.4.2_das",
        firmware_key="nanos/1.4.2-das/upgrade_osu_1.4.2_das_key",
        hash="09C9000000000000000000000000000000000000000000000000000000003DCA",
        next_se_firmware_final_version=firmware_final_ver4
    )
    firmware_osu_ver5.device_versions.add(device_ver1)
    firmware_osu_ver5.previous_se_firmware_final_versions.add(
        firmware_final_ver5)
    firmware_osu_ver5.providers.add(provider2)

    firmware_osu_ver6 = SeFirmwareOSUVersion.objects.create(
        name="1.3.1-club-osu",
        perso="perso_club_10",
        firmware="nanos/1.3.1-club/upgrade_osu_1.3.1_club",
        firmware_key="nanos/1.3.1-club/upgrade_osu_1.3.1_club_key",
        hash="78ef4503452b5810b42e6e715d4fe8ff3765f06758c78eefe3977e1949a12503",
        next_se_firmware_final_version=firmware_final_ver6
    )
    firmware_osu_ver6.device_versions.add(device_ver0)
    firmware_osu_ver6.previous_se_firmware_final_versions.add(
        firmware_final_ver7)
    firmware_osu_ver6.providers.add(provider3)

    # APP CREATION
    app0 = Application.objects.create(name="Bitcoin")
    app0.providers.add(provider1, provider2)
    app1 = Application.objects.create(name="Bitcoin Cash")
    app1.providers.add(provider1, provider2)
    app2 = Application.objects.create(name="Bitcoin Gold")
    app2.providers.add(provider1)
    app3 = Application.objects.create(name="Bitcoin Private")
    app3.providers.add(provider1)
    app4 = Application.objects.create(name="Bitcoin testnet")
    app4.providers.add(provider1)
    app5 = Application.objects.create(name="Digibyte")
    app5.providers.add(provider1)
    app6 = Application.objects.create(name="HCash")
    app6.providers.add(provider1)
    app7 = Application.objects.create(name="Qtum")
    app7.providers.add(provider1)
    app8 = Application.objects.create(name="PIVX")
    app8.providers.add(provider1)
    app9 = Application.objects.create(name="Stealth")
    app9.providers.add(provider1)
    app10 = Application.objects.create(name="Vertcoin")
    app10.providers.add(provider1)
    app11 = Application.objects.create(name="Viacoin")
    app11.providers.add(provider1)
    app12 = Application.objects.create(name="Ubiq")
    app12.providers.add(provider1)
    app13 = Application.objects.create(name="Expanse")
    app13.providers.add(provider1)
    app14 = Application.objects.create(name="Dash")
    app14.providers.add(provider1)
    app15 = Application.objects.create(name="Dogecoin")
    app15.providers.add(provider1)
    app16 = Application.objects.create(name="Ethereum")
    app16.providers.add(provider1, provider2)
    app17 = Application.objects.create(name="Fido U2F")
    app17.providers.add(provider1)
    app18 = Application.objects.create(name="Litecoin")
    app18.providers.add(provider1)
    app19 = Application.objects.create(name="Stratis")
    app19.providers.add(provider1)
    app20 = Application.objects.create(name="Ripple")
    app20.providers.add(provider1, provider2)
    app21 = Application.objects.create(name="Zcash")
    app21.providers.add(provider1)
    app22 = Application.objects.create(name="ZenCash")
    app22.providers.add(provider1)
    app23 = Application.objects.create(name="Komodo")
    app23.providers.add(provider1)
    app24 = Application.objects.create(name="Peercoin")
    app24.providers.add(provider1)
    app25 = Application.objects.create(name="PoSW")
    app25.providers.add(provider1)
    app26 = Application.objects.create(name="Ark")
    app26.providers.add(provider1)
    app27 = Application.objects.create(name="Neo")
    app27.providers.add(provider1)
    app28 = Application.objects.create(name="SSH/GPG Agent")
    app28.providers.add(provider1)
    app29 = Application.objects.create(name="Passwords Manager")
    app29.providers.add(provider1)
    app30 = Application.objects.create(name="Stellar")
    app30.providers.add(provider1)
    app31 = Application.objects.create(name="Woleet")
    app31.providers.add(provider1)
    app32 = Application.objects.create(name="Monero")
    app32.providers.add(provider1)
    app33 = Application.objects.create(name="Hello")
    app33.providers.add(provider1)
    app34 = Application.objects.create(name="Open PGP")
    app34.providers.add(provider1)
    app35 = Application.objects.create(name="Nano")
    app35.providers.add(provider1)
    app36 = Application.objects.create(name="Nimiq")
    app36.providers.add(provider1)
    app37 = Application.objects.create(name="DasCoin")
    app37.providers.add(provider2)
    app38 = Application.objects.create(name="Stealthcoin")
    app38.providers.add(provider1)
    app39 = Application.objects.create(name="Clubcoin")
    app39.providers.add(provider1)
    app40 = Application.objects.create(name="Bitcoin Beta")
    app40.providers.add(provider1)
    # nanos-1.4 ,
    appVer1 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=66054,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin/app_1.2.6",
        firmware_key="nanos/1.4.2/bitcoin/app_1.2.6_key",
        delete="nanos/1.4.2/bitcoin/app_del",
        delete_key="nanos/1.4.2/bitcoin/app_del_key",
        app=app0
    )
    appVer1.providers.add(provider1)
    appVer1.device_versions.add(device_ver5)
    appVer1.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer2 = ApplicationVersion.objects.create(
        name="Bitcoin Cash",
        version=66054,
        display_name="Bitcoin Cash",
        icon="bitcoin_cash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_cash/app_1.2.6",
        firmware_key="nanos/1.4.2/bitcoin_cash/app_1.2.6_key",
        delete="nanos/1.4.2/bitcoin_cash/app_del",
        delete_key="nanos/1.4.2/bitcoin_cash/app_del_key",
        app=app1
    )
    appVer2.providers.add(provider1)
    appVer2.device_versions.add(device_ver5)
    appVer2.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer3 = ApplicationVersion.objects.create(
        name="Bitcoin Gold",
        version=66054,
        display_name="Bitcoin Gold",
        icon="bitcoin_gold",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_gold/app_1.2.6",
        firmware_key="nanos/1.4.2/bitcoin_gold/app_1.2.6_key",
        delete="nanos/1.4.2/bitcoin_gold/app_del",
        delete_key="nanos/1.4.2/bitcoin_gold/app_del_key",
        app=app2
    )
    appVer3.providers.add(provider1)
    appVer3.device_versions.add(device_ver5)
    appVer3.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer4 = ApplicationVersion.objects.create(
        name="Bitcoin Private",
        version=66054,
        display_name="Bitcoin Private",
        icon="bitcoin_private",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_private/app_1.2.6",
        firmware_key="nanos/1.4.2/bitcoin_private/app_1.2.6_key",
        delete="nanos/1.4.2/bitcoin_private/app_del",
        delete_key="nanos/1.4.2/bitcoin_private/app_del_key",
        app=app3
    )
    appVer4.providers.add(provider1)
    appVer4.device_versions.add(device_ver5)
    appVer4.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer5 = ApplicationVersion.objects.create(
        name="Bitcoin testnet",
        version=66054,
        display_name="Bitcoin testnet",
        icon="bitcoin_testnet",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_testnet/app_1.2.6",
        firmware_key="nanos/1.4.2/bitcoin_testnet/app_1.2.6_key",
        delete="nanos/1.4.2/bitcoin_testnet/app_del",
        delete_key="nanos/1.4.2/bitcoin_testnet/app_del_key",
        app=app4
    )
    appVer5.providers.add(provider1)
    appVer5.device_versions.add(device_ver5)
    appVer5.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer6 = ApplicationVersion.objects.create(
        name="Digibyte",
        version=66054,
        display_name="Digibyte",
        icon="digibyte",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/digibyte/app_1.2.6",
        firmware_key="nanos/1.4.2/digibyte/app_1.2.6_key",
        delete="nanos/1.4.2/digibyte/app_del",
        delete_key="nanos/1.4.2/digibyte/app_del_key",
        app=app5
    )
    appVer6.providers.add(provider1)
    appVer6.device_versions.add(device_ver5)
    appVer6.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer7 = ApplicationVersion.objects.create(
        name="HCash",
        version=66054,
        display_name="HCash",
        icon="hcash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/hcash/app_1.2.6",
        firmware_key="nanos/1.4.2/hcash/app_1.2.6_key",
        delete="nanos/1.4.2/hcash/app_del",
        delete_key="nanos/1.4.2/hcash/app_del_key",
        app=app6
    )
    appVer7.providers.add(provider1)
    appVer7.device_versions.add(device_ver5)
    appVer7.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer8 = ApplicationVersion.objects.create(
        name="Qtum",
        version=66054,
        display_name="Qtum",
        icon="qtum",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/qtum/app_1.2.6",
        firmware_key="nanos/1.4.2/qtum/app_1.2.6_key",
        delete="nanos/1.4.2/qtum/app_del",
        delete_key="nanos/1.4.2/qtum/app_del_key",
        app=app7
    )
    appVer8.providers.add(provider1)
    appVer8.device_versions.add(device_ver5)
    appVer8.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer9 = ApplicationVersion.objects.create(
        name="PIVX",
        version=66054,
        display_name="PIVX",
        icon="pivx",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/pivx/app_1.2.6",
        firmware_key="nanos/1.4.2/pivx/app_1.2.6_key",
        delete="nanos/1.4.2/pivx/app_del",
        delete_key="nanos/1.4.2/pivx/app_del_key",
        app=app8
    )
    appVer9.providers.add(provider1)
    appVer9.device_versions.add(device_ver5)
    appVer9.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer10 = ApplicationVersion.objects.create(
        name="Stealth",
        version=66054,
        display_name="Stealth",
        icon="stealthcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/stealthcoin/app_1.2.6",
        firmware_key="nanos/1.4.2/stealthcoin/app_1.2.6_key",
        delete="nanos/1.4.2/stealthcoin/app_del",
        delete_key="nanos/1.4.2/stealthcoin/app_del_key",
        app=app9
    )
    appVer10.providers.add(provider1)
    appVer10.device_versions.add(device_ver5)
    appVer10.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer11 = ApplicationVersion.objects.create(
        name="Vertcoin",
        version=66054,
        display_name="Vertcoin",
        icon="vertcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/vertcoin/app_1.2.6",
        firmware_key="nanos/1.4.2/vertcoin/app_1.2.6_key",
        delete="nanos/1.4.2/vertcoin/app_del",
        delete_key="nanos/1.4.2/vertcoin/app_del_key",
        app=app10
    )
    appVer11.providers.add(provider1)
    appVer11.device_versions.add(device_ver5)
    appVer11.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer12 = ApplicationVersion.objects.create(
        name="Viacoin",
        version=66054,
        display_name="Viacoin",
        icon="viacoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/viacoin/app_1.2.6",
        firmware_key="nanos/1.4.2/viacoin/app_1.2.6_key",
        delete="nanos/1.4.2/viacoin/app_del",
        delete_key="nanos/1.4.2/viacoin/app_del_key",
        app=app11
    )
    appVer12.providers.add(provider1)
    appVer12.device_versions.add(device_ver5)
    appVer12.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer13 = ApplicationVersion.objects.create(
        name="Ubiq",
        version=65560,
        display_name="Ubiq",
        icon="ubiq",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/ubiq/app_1.0.24",
        firmware_key="nanos/1.4.2/ubiq/app_1.0.24_key",
        delete="nanos/1.4.2/ubiq/app_del",
        delete_key="nanos/1.4.2/ubiq/app_del_key",
        app=app12
    )
    appVer13.providers.add(provider1)
    appVer13.device_versions.add(device_ver5)
    appVer13.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer14 = ApplicationVersion.objects.create(
        name="Expanse",
        version=65560,
        display_name="Expanse",
        icon="expanse",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/expanse/app_1.0.24",
        firmware_key="nanos/1.4.2/expanse/app_1.0.24_key",
        delete="nanos/1.4.2/expanse/app_del",
        delete_key="nanos/1.4.2/expanse/app_del_key",
        app=app13
    )
    appVer14.providers.add(provider1)
    appVer14.device_versions.add(device_ver5)
    appVer14.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer15 = ApplicationVersion.objects.create(
        name="Dash",
        version=66054,
        display_name="Dash",
        icon="dash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/dash/app_1.2.6",
        firmware_key="nanos/1.4.2/dash/app_1.2.6_key",
        delete="nanos/1.4.2/dash/app_del",
        delete_key="nanos/1.4.2/dash/app_del_key",
        app=app14
    )
    appVer15.providers.add(provider1)
    appVer15.device_versions.add(device_ver5)
    appVer15.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer16 = ApplicationVersion.objects.create(
        name="Dogecoin",
        version=66054,
        display_name="Dogecoin",
        icon="dogecoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/dogecoin/app_1.2.6",
        firmware_key="nanos/1.4.2/dogecoin/app_1.2.6_key",
        delete="nanos/1.4.2/dogecoin/app_del",
        delete_key="nanos/1.4.2/dogecoin/app_del_key",
        app=app15
    )
    appVer16.providers.add(provider1)
    appVer16.device_versions.add(device_ver5)
    appVer16.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer17 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65560,
        display_name="Ethereum",
        icon="ethereum",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/ethereum/app_1.0.24",
        firmware_key="nanos/1.4.2/ethereum/app_1.0.24_key",
        delete="nanos/1.4.2/ethereum/app_del",
        delete_key="nanos/1.4.2/ethereum/app_del_key",
        app=app16
    )
    appVer17.providers.add(provider1, provider2)
    appVer17.device_versions.add(device_ver5)
    appVer17.se_firmware_final_versions.add(
        firmware_final_ver3, firmware_final_ver4)
    # nanos-1.4 ,
    appVer18 = ApplicationVersion.objects.create(
        name="Fido U2F",
        version=66052,
        display_name="Fido U2F",
        icon="fido",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/u2f/app_1.2.4",
        firmware_key="nanos/1.4.2/u2f/app_1.2.4_key",
        delete="nanos/1.4.2/u2f/app_del",
        delete_key="nanos/1.4.2/u2f/app_del_key",
        app=app17
    )
    appVer18.providers.add(provider1)
    appVer18.device_versions.add(device_ver5)
    appVer18.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer19 = ApplicationVersion.objects.create(
        name="Litecoin",
        version=66054,
        display_name="Litecoin",
        icon="litecoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/litecoin/app_1.2.6",
        firmware_key="nanos/1.4.2/litecoin/app_1.2.6_key",
        delete="nanos/1.4.2/litecoin/app_del",
        delete_key="nanos/1.4.2/litecoin/app_del_key",
        app=app18
    )
    appVer19.providers.add(provider1)
    appVer19.device_versions.add(device_ver5)
    appVer19.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer20 = ApplicationVersion.objects.create(
        name="Stratis",
        version=66054,
        display_name="Stratis",
        icon="stratis",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/stratis/app_1.2.6",
        firmware_key="nanos/1.4.2/stratis/app_1.2.6_key",
        delete="nanos/1.4.2/stratis/app_del",
        delete_key="nanos/1.4.2/stratis/app_del_key",
        app=app19
    )
    appVer20.providers.add(provider1)
    appVer20.device_versions.add(device_ver5)
    appVer20.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer21 = ApplicationVersion.objects.create(
        name="Ripple",
        version=65540,
        display_name="Ripple",
        icon="ripple",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/ripple/app_1.0.4",
        firmware_key="nanos/1.4.2/ripple/app_1.0.4_key",
        delete="nanos/1.4.2/ripple/app_del",
        delete_key="nanos/1.4.2/ripple/app_del_key",
        app=app20
    )
    appVer21.providers.add(provider1, provider2)
    appVer21.device_versions.add(device_ver5)
    appVer21.se_firmware_final_versions.add(
        firmware_final_ver3, firmware_final_ver4)
    # nanos-1.4 ,
    appVer22 = ApplicationVersion.objects.create(
        name="Zcash",
        version=66054,
        display_name="Zcash",
        icon="zcash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/zcash/app_1.2.6",
        firmware_key="nanos/1.4.2/zcash/app_1.2.6_key",
        delete="nanos/1.4.2/zcash/app_del",
        delete_key="nanos/1.4.2/zcash/app_del_key",
        app=app21
    )
    appVer22.providers.add(provider1)
    appVer22.device_versions.add(device_ver5)
    appVer22.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer23 = ApplicationVersion.objects.create(
        name="ZenCash",
        version=66054,
        display_name="ZenCash",
        icon="zencash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/zencash/app_1.2.6",
        firmware_key="nanos/1.4.2/zencash/app_1.2.6_key",
        delete="nanos/1.4.2/zencash/app_del",
        delete_key="nanos/1.4.2/zencash/app_del_key",
        app=app22
    )
    appVer23.providers.add(provider1)
    appVer23.device_versions.add(device_ver5)
    appVer23.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer24 = ApplicationVersion.objects.create(
        name="Komodo",
        version=66054,
        display_name="Komodo",
        icon="komodo",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/komodo/app_1.2.6",
        firmware_key="nanos/1.4.2/komodo/app_1.2.6_key",
        delete="nanos/1.4.2/komodo/app_del",
        delete_key="nanos/1.4.2/komodo/app_del_key",
        app=app23
    )
    appVer24.providers.add(provider1)
    appVer24.device_versions.add(device_ver5)
    appVer24.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer25 = ApplicationVersion.objects.create(
        name="Peercoin",
        version=66054,
        display_name="Peercoin",
        icon="peercoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/peercoin/app_1.2.6",
        firmware_key="nanos/1.4.2/peercoin/app_1.2.6_key",
        delete="nanos/1.4.2/peercoin/app_del",
        delete_key="nanos/1.4.2/peercoin/app_del_key",
        app=app24
    )
    appVer25.providers.add(provider1)
    appVer25.device_versions.add(device_ver5)
    appVer25.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer26 = ApplicationVersion.objects.create(
        name="PoSW",
        version=66054,
        display_name="PoSW",
        icon="posw",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/posw/app_1.2.6",
        firmware_key="nanos/1.4.2/posw/app_1.2.6_key",
        delete="nanos/1.4.2/posw/app_del",
        delete_key="nanos/1.4.2/posw/app_del_key",
        app=app25
    )
    appVer26.providers.add(provider1)
    appVer26.device_versions.add(device_ver5)
    appVer26.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer27 = ApplicationVersion.objects.create(
        name="Ark",
        version=259,
        display_name="Ark",
        icon="ark",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/ark/app_0.1.3",
        firmware_key="nanos/1.4.2/ark/app_0.1.3_key",
        delete="nanos/1.4.2/ark/app_del",
        delete_key="nanos/1.4.2/ark/app_del_key",
        app=app26
    )
    appVer27.providers.add(provider1)
    appVer27.device_versions.add(device_ver5)
    appVer27.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer28 = ApplicationVersion.objects.create(
        name="Neo",
        version=66305,
        display_name="Neo",
        icon="neo",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/neo/app_1.3.1",
        firmware_key="nanos/1.4.2/neo/app_1.3.1_key",
        delete="nanos/1.4.2/neo/app_del",
        delete_key="nanos/1.4.2/neo/app_del_key",
        app=app27
    )
    appVer28.providers.add(provider1)
    appVer28.device_versions.add(device_ver5)
    appVer28.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer29 = ApplicationVersion.objects.create(
        name="SSH/GPG Agent",
        version=4,
        display_name="SSH/GPG Agent",
        icon="ssh",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/sshgpg/app_0.0.4",
        firmware_key="nanos/1.4.2/sshgpg/app_0.0.4_key",
        delete="nanos/1.4.2/sshgpg/app_del",
        delete_key="nanos/1.4.2/sshgpg/app_del_key",
        app=app28
    )
    appVer29.providers.add(provider1)
    appVer29.device_versions.add(device_ver5)
    appVer29.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer30 = ApplicationVersion.objects.create(
        name="Passwords Manager",
        version=4,
        display_name="Passwords Manager",
        icon="ssh",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/pwmgr/app_0.0.4",
        firmware_key="nanos/1.4.2/pwmgr/app_0.0.4_key",
        delete="nanos/1.4.2/pwmgr/app_del",
        delete_key="nanos/1.4.2/pwmgr/app_del_key",
        app=app29
    )
    appVer30.providers.add(provider1)
    appVer30.device_versions.add(device_ver5)
    appVer30.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer31 = ApplicationVersion.objects.create(
        name="Stellar",
        version=131328,
        display_name="Stellar",
        icon="stellar",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/stellar/app_2.1.0",
        firmware_key="nanos/1.4.2/stellar/app_2.1.0_key",
        delete="nanos/1.4.2/stellar/app_del",
        delete_key="nanos/1.4.2/stellar/app_del_key",
        app=app30
    )
    appVer31.providers.add(provider1)
    appVer31.device_versions.add(device_ver5)
    appVer31.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer32 = ApplicationVersion.objects.create(
        name="Woleet",
        version=66053,
        display_name="Woleet",
        icon="woleet",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/woleet/app_1.2.5",
        firmware_key="nanos/1.4.2/woleet/app_1.2.5_key",
        delete="nanos/1.4.2/woleet/app_del",
        delete_key="nanos/1.4.2/woleet/app_del_key",
        app=app31
    )
    appVer32.providers.add(provider1)
    appVer32.device_versions.add(device_ver5)
    appVer32.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer33 = ApplicationVersion.objects.create(
        name="Monero",
        version=65536,
        display_name="Monero",
        icon="monero",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/monero/app_1.0.0",
        firmware_key="nanos/1.4.2/monero/app_1.0.0_key",
        delete="nanos/1.4.2/monero/app_del",
        delete_key="nanos/1.4.2/monero/app_del_key",
        app=app32
    )
    appVer33.providers.add(provider1)
    appVer33.device_versions.add(device_ver5)
    appVer33.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer34 = ApplicationVersion.objects.create(
        name="Hello",
        version=65537,
        display_name="Hello",
        icon="hello",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/hello/app_1.0.1",
        firmware_key="nanos/1.4.2/hello/app_1.0.1_key",
        delete="nanos/1.4.2/hello/app_del",
        delete_key="nanos/1.4.2/hello/app_del_key",
        app=app33
    )
    appVer34.providers.add(provider1)
    appVer34.device_versions.add(device_ver5)
    appVer34.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer35 = ApplicationVersion.objects.create(
        name="Open PGP",
        version=66049,
        display_name="Open PGP",
        icon="gnupg",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/openpgp/app_1.2.1",
        firmware_key="nanos/1.4.2/openpgp/app_1.2.1_key",
        delete="nanos/1.4.2/openpgp/app_del",
        delete_key="nanos/1.4.2/openpgp/app_del_key",
        app=app34
    )
    appVer35.providers.add(provider1)
    appVer35.device_versions.add(device_ver5)
    appVer35.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer36 = ApplicationVersion.objects.create(
        name="Nano",
        version=65536,
        display_name="Nano",
        icon="nano",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/nano/app_1.0.0",
        firmware_key="nanos/1.4.2/nano/app_1.0.0_key",
        delete="nanos/1.4.2/nano/app_del",
        delete_key="nanos/1.4.2/nano/app_del_key",
        app=app35
    )
    appVer36.providers.add(provider1)
    appVer36.device_versions.add(device_ver5)
    appVer36.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer37 = ApplicationVersion.objects.create(
        name="Nimiq",
        version=257,
        display_name="Nimiq",
        icon="nimiq",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/nimiq/app_0.1.1",
        firmware_key="nanos/1.4.2/nimiq/app_0.1.1_key",
        delete="nanos/1.4.2/nimiq/app_del",
        delete_key="nanos/1.4.2/nimiq/app_del_key",
        app=app36
    )
    appVer37.providers.add(provider1)
    appVer37.device_versions.add(device_ver5)
    appVer37.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer38 = ApplicationVersion.objects.create(
        name="DasCoin",
        version=65794,
        display_name="DasCoin",
        icon="dascoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2-das/dascoin/app_1.1.2",
        firmware_key="nanos/1.4.2-das/dascoin/app_1.1.2_key",
        delete="nanos/1.4.2-das/dascoin/app_del",
        delete_key="nanos/1.4.2-das/dascoin/app_del_key",
        app=app37
    )
    appVer38.providers.add(provider2)
    appVer38.device_versions.add(device_ver5)
    appVer38.se_firmware_final_versions.add(firmware_final_ver4)
    # nanos-1.4 ,
    appVer39 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=66053,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin/app_1.2.5",
        firmware_key="nanos/1.4.2/bitcoin/app_1.2.5_key",
        delete="nanos/1.4.2/bitcoin/app_del",
        delete_key="nanos/1.4.2/bitcoin/app_del_key",
        app=app0
    )
    appVer39.providers.add(provider1, provider2)
    appVer39.device_versions.add(device_ver5)
    appVer39.se_firmware_final_versions.add(
        firmware_final_ver3, firmware_final_ver4)
    # nanos-1.4 ,
    appVer40 = ApplicationVersion.objects.create(
        name="Bitcoin Cash",
        version=66053,
        display_name="Bitcoin Cash",
        icon="bitcoin_cash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_cash/app_1.2.5",
        firmware_key="nanos/1.4.2/bitcoin_cash/app_1.2.5_key",
        delete="nanos/1.4.2/bitcoin_cash/app_del",
        delete_key="nanos/1.4.2/bitcoin_cash/app_del_key",
        app=app1
    )
    appVer40.providers.add(provider1, provider2)
    appVer40.device_versions.add(device_ver5)
    appVer40.se_firmware_final_versions.add(
        firmware_final_ver3, firmware_final_ver4)
    # nanos-1.4 ,
    appVer43 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=66052,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/bitcoin/app_1.2.4",
        firmware_key="nanos/1.4.1/bitcoin/app_1.2.4_key",
        delete="nanos/1.4.1/bitcoin/app_del",
        delete_key="nanos/1.4.1/bitcoin/app_del_key",
        app=app0
    )
    appVer43.providers.add(provider1)
    appVer43.device_versions.add(device_ver5)
    appVer43.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer44 = ApplicationVersion.objects.create(
        name="Bitcoin Cash",
        version=66052,
        display_name="Bitcoin Cash",
        icon="bitcoin_cash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/bitcoin_cash/app_1.2.4",
        firmware_key="nanos/1.4.1/bitcoin_cash/app_1.2.4_key",
        delete="nanos/1.4.1/bitcoin_cash/app_del",
        delete_key="nanos/1.4.1/bitcoin_cash/app_del_key",
        app=app1
    )
    appVer44.providers.add(provider1)
    appVer44.device_versions.add(device_ver5)
    appVer44.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer45 = ApplicationVersion.objects.create(
        name="Bitcoin Gold",
        version=66052,
        display_name="Bitcoin Gold",
        icon="bitcoin_gold",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/bitcoin_gold/app_1.2.4",
        firmware_key="nanos/1.4.1/bitcoin_gold/app_1.2.4_key",
        delete="nanos/1.4.1/bitcoin_gold/app_del",
        delete_key="nanos/1.4.1/bitcoin_gold/app_del_key",
        app=app2
    )
    appVer45.providers.add(provider1)
    appVer45.device_versions.add(device_ver5)
    appVer45.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer46 = ApplicationVersion.objects.create(
        name="Bitcoin testnet",
        version=66052,
        display_name="Bitcoin testnet",
        icon="bitcoin_testnet",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/bitcoin_testnet/app_1.2.4",
        firmware_key="nanos/1.4.1/bitcoin_testnet/app_1.2.4_key",
        delete="nanos/1.4.1/bitcoin_testnet/app_del",
        delete_key="nanos/1.4.1/bitcoin_testnet/app_del_key",
        app=app4
    )
    appVer46.providers.add(provider1)
    appVer46.device_versions.add(device_ver5)
    appVer46.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer47 = ApplicationVersion.objects.create(
        name="Digibyte",
        version=66052,
        display_name="Digibyte",
        icon="digibyte",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/digibyte/app_1.2.4",
        firmware_key="nanos/1.4.1/digibyte/app_1.2.4_key",
        delete="nanos/1.4.1/digibyte/app_del",
        delete_key="nanos/1.4.1/digibyte/app_del_key",
        app=app5
    )
    appVer47.providers.add(provider1)
    appVer47.device_versions.add(device_ver5)
    appVer47.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer48 = ApplicationVersion.objects.create(
        name="HCash",
        version=66052,
        display_name="HCash",
        icon="hcash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/hcash/app_1.2.4",
        firmware_key="nanos/1.4.1/hcash/app_1.2.4_key",
        delete="nanos/1.4.1/hcash/app_del",
        delete_key="nanos/1.4.1/hcash/app_del_key",
        app=app6
    )
    appVer48.providers.add(provider1)
    appVer48.device_versions.add(device_ver5)
    appVer48.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer49 = ApplicationVersion.objects.create(
        name="Qtum",
        version=66052,
        display_name="Qtum",
        icon="qtum",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/qtum/app_1.2.4",
        firmware_key="nanos/1.4.1/qtum/app_1.2.4_key",
        delete="nanos/1.4.1/qtum/app_del",
        delete_key="nanos/1.4.1/qtum/app_del_key",
        app=app7
    )
    appVer49.providers.add(provider1)
    appVer49.device_versions.add(device_ver5)
    appVer49.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer50 = ApplicationVersion.objects.create(
        name="PIVX",
        version=66052,
        display_name="PIVX",
        icon="pivx",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/pivx/app_1.2.4",
        firmware_key="nanos/1.4.1/pivx/app_1.2.4_key",
        delete="nanos/1.4.1/pivx/app_del",
        delete_key="nanos/1.4.1/pivx/app_del_key",
        app=app8
    )
    appVer50.providers.add(provider1)
    appVer50.device_versions.add(device_ver5)
    appVer50.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer51 = ApplicationVersion.objects.create(
        name="Stealthcoin",
        version=66052,
        display_name="Stealthcoin",
        icon="stealthcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/stealthcoin/app_1.2.4",
        firmware_key="nanos/1.4.1/stealthcoin/app_1.2.4_key",
        delete="nanos/1.4.1/stealthcoin/app_del",
        delete_key="nanos/1.4.1/stealthcoin/app_del_key",
        app=app38
    )
    appVer51.providers.add(provider1)
    appVer51.device_versions.add(device_ver5)
    appVer51.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer52 = ApplicationVersion.objects.create(
        name="Vertcoin",
        version=66052,
        display_name="Vertcoin",
        icon="vertcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/vertcoin/app_1.2.4",
        firmware_key="nanos/1.4.1/vertcoin/app_1.2.4_key",
        delete="nanos/1.4.1/vertcoin/app_del",
        delete_key="nanos/1.4.1/vertcoin/app_del_key",
        app=app10
    )
    appVer52.providers.add(provider1)
    appVer52.device_versions.add(device_ver5)
    appVer52.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer53 = ApplicationVersion.objects.create(
        name="Viacoin",
        version=66052,
        display_name="Viacoin",
        icon="viacoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/viacoin/app_1.2.4",
        firmware_key="nanos/1.4.1/viacoin/app_1.2.4_key",
        delete="nanos/1.4.1/viacoin/app_del",
        delete_key="nanos/1.4.1/viacoin/app_del_key",
        app=app11
    )
    appVer53.providers.add(provider1)
    appVer53.device_versions.add(device_ver5)
    appVer53.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer54 = ApplicationVersion.objects.create(
        name="Ubiq",
        version=65558,
        display_name="Ubiq",
        icon="ubiq",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/ubiq/app_1.0.22",
        firmware_key="nanos/1.4.1/ubiq/app_1.0.22_key",
        delete="nanos/1.4.1/ubiq/app_del",
        delete_key="nanos/1.4.1/ubiq/app_del_key",
        app=app12
    )
    appVer54.providers.add(provider1)
    appVer54.device_versions.add(device_ver5)
    appVer54.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer55 = ApplicationVersion.objects.create(
        name="Expanse",
        version=65558,
        display_name="Expanse",
        icon="expanse",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/expanse/app_1.0.22",
        firmware_key="nanos/1.4.1/expanse/app_1.0.22_key",
        delete="nanos/1.4.1/expanse/app_del",
        delete_key="nanos/1.4.1/expanse/app_del_key",
        app=app13
    )
    appVer55.providers.add(provider1)
    appVer55.device_versions.add(device_ver5)
    appVer55.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer56 = ApplicationVersion.objects.create(
        name="Dash",
        version=66052,
        display_name="Dash",
        icon="dash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/dash/app_1.2.4",
        firmware_key="nanos/1.4.1/dash/app_1.2.4_key",
        delete="nanos/1.4.1/dash/app_del",
        delete_key="nanos/1.4.1/dash/app_del_key",
        app=app14
    )
    appVer56.providers.add(provider1)
    appVer56.device_versions.add(device_ver5)
    appVer56.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer57 = ApplicationVersion.objects.create(
        name="Dogecoin",
        version=66052,
        display_name="Dogecoin",
        icon="dogecoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/dogecoin/app_1.2.4",
        firmware_key="nanos/1.4.1/dogecoin/app_1.2.4_key",
        delete="nanos/1.4.1/dogecoin/app_del",
        delete_key="nanos/1.4.1/dogecoin/app_del_key",
        app=app15
    )
    appVer57.providers.add(provider1)
    appVer57.device_versions.add(device_ver5)
    appVer57.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer58 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65558,
        display_name="Ethereum",
        icon="ethereum",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/ethereum/app_1.0.22",
        firmware_key="nanos/1.4.1/ethereum/app_1.0.22_key",
        delete="nanos/1.4.1/ethereum/app_del",
        delete_key="nanos/1.4.1/ethereum/app_del_key",
        app=app16
    )
    appVer58.providers.add(provider1)
    appVer58.device_versions.add(device_ver5)
    appVer58.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer59 = ApplicationVersion.objects.create(
        name="Fido U2F",
        version=66051,
        display_name="Fido U2F",
        icon="fido",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/u2f/app_1.2.3",
        firmware_key="nanos/1.4.1/u2f/app_1.2.3_key",
        delete="nanos/1.4.1/u2f/app_del",
        delete_key="nanos/1.4.1/u2f/app_del_key",
        app=app17
    )
    appVer59.providers.add(provider1)
    appVer59.device_versions.add(device_ver5)
    appVer59.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer60 = ApplicationVersion.objects.create(
        name="Litecoin",
        version=66052,
        display_name="Litecoin",
        icon="litecoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/litecoin/app_1.2.4",
        firmware_key="nanos/1.4.1/litecoin/app_1.2.4_key",
        delete="nanos/1.4.1/litecoin/app_del",
        delete_key="nanos/1.4.1/litecoin/app_del_key",
        app=app18
    )
    appVer60.providers.add(provider1)
    appVer60.device_versions.add(device_ver5)
    appVer60.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer61 = ApplicationVersion.objects.create(
        name="Stratis",
        version=66052,
        display_name="Stratis",
        icon="stratis",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/stratis/app_1.2.4",
        firmware_key="nanos/1.4.1/stratis/app_1.2.4_key",
        delete="nanos/1.4.1/stratis/app_del",
        delete_key="nanos/1.4.1/stratis/app_del_key",
        app=app19
    )
    appVer61.providers.add(provider1)
    appVer61.device_versions.add(device_ver5)
    appVer61.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer62 = ApplicationVersion.objects.create(
        name="Ripple",
        version=65539,
        display_name="Ripple",
        icon="ripple",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/ripple/app_1.0.3",
        firmware_key="nanos/1.4.1/ripple/app_1.0.3_key",
        delete="nanos/1.4.1/ripple/app_del",
        delete_key="nanos/1.4.1/ripple/app_del_key",
        app=app20
    )
    appVer62.providers.add(provider1)
    appVer62.device_versions.add(device_ver5)
    appVer62.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer63 = ApplicationVersion.objects.create(
        name="Zcash",
        version=66052,
        display_name="Zcash",
        icon="zcash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/zcash/app_1.2.4",
        firmware_key="nanos/1.4.1/zcash/app_1.2.4_key",
        delete="nanos/1.4.1/zcash/app_del",
        delete_key="nanos/1.4.1/zcash/app_del_key",
        app=app21
    )
    appVer63.providers.add(provider1)
    appVer63.device_versions.add(device_ver5)
    appVer63.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer64 = ApplicationVersion.objects.create(
        name="Komodo",
        version=66052,
        display_name="Komodo",
        icon="komodo",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/komodo/app_1.2.4",
        firmware_key="nanos/1.4.1/komodo/app_1.2.4_key",
        delete="nanos/1.4.1/komodo/app_del",
        delete_key="nanos/1.4.1/komodo/app_del_key",
        app=app23
    )
    appVer64.providers.add(provider1)
    appVer64.device_versions.add(device_ver5)
    appVer64.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer65 = ApplicationVersion.objects.create(
        name="SSH/GPG Agent",
        version=3,
        display_name="SSH/GPG Agent",
        icon="ssh",
        hash="9b52a2b0532c3bbb058a6c817b02963174f32b3d41314f7b507623f163d71b65",
        perso="perso_11",
        firmware="nanos/1.3.1/sshgpg/st31_gpg_0.0.3",
        firmware_key="nanos/1.3.1/sshgpg/st31_gpg_0.0.3_key",
        delete="nanos/1.3.1/sshgpg/st31_gpg_del",
        delete_key="nanos/1.3.1/sshgpg/st31_gpg_del_key",
        app=app28
    )
    appVer65.providers.add(provider1)
    appVer65.device_versions.add(device_ver5)
    appVer65.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer66 = ApplicationVersion.objects.create(
        name="PoSW",
        version=66052,
        display_name="PoSW",
        icon="posw",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/posw/app_1.2.4",
        firmware_key="nanos/1.4.1/posw/app_1.2.4_key",
        delete="nanos/1.4.1/posw/app_del",
        delete_key="nanos/1.4.1/posw/app_del_key",
        app=app25
    )
    appVer66.providers.add(provider1)
    appVer66.device_versions.add(device_ver5)
    appVer66.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer67 = ApplicationVersion.objects.create(
        name="Ark",
        version=258,
        display_name="Ark",
        icon="ark",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/ark/app_0.1.2",
        firmware_key="nanos/1.4.1/ark/app_0.1.2_key",
        delete="nanos/1.4.1/ark/app_del",
        delete_key="nanos/1.4.1/ark/app_del_key",
        app=app26
    )
    appVer67.providers.add(provider1)
    appVer67.device_versions.add(device_ver5)
    appVer67.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer68 = ApplicationVersion.objects.create(
        name="Neo",
        version=65794,
        display_name="Neo",
        icon="neo",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/neo/app_1.1.2",
        firmware_key="nanos/1.4.1/neo/app_1.1.2_key",
        delete="nanos/1.4.1/neo/app_del",
        delete_key="nanos/1.4.1/neo/app_del_key",
        app=app27
    )
    appVer68.providers.add(provider1)
    appVer68.device_versions.add(device_ver5)
    appVer68.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer69 = ApplicationVersion.objects.create(
        name="SSH/GPG Agent",
        version=4,
        display_name="SSH/GPG Agent",
        icon="ssh",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/sshgpg/app_0.0.4",
        firmware_key="nanos/1.4.1/sshgpg/app_0.0.4_key",
        delete="nanos/1.4.1/sshgpg/app_del",
        delete_key="nanos/1.4.1/sshgpg/app_del_key",
        app=app28
    )
    appVer69.providers.add(provider1)
    appVer69.device_versions.add(device_ver5)
    appVer69.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer70 = ApplicationVersion.objects.create(
        name="Passwords Manager",
        version=3,
        display_name="Passwords Manager",
        icon="ssh",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/pwmgr/app_0.0.3",
        firmware_key="nanos/1.4.1/pwmgr/app_0.0.3_key",
        delete="nanos/1.4.1/pwmgr/app_del",
        delete_key="nanos/1.4.1/pwmgr/app_del_key",
        app=app29
    )
    appVer70.providers.add(provider1)
    appVer70.device_versions.add(device_ver5)
    appVer70.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer71 = ApplicationVersion.objects.create(
        name="Stellar",
        version=131074,
        display_name="Stellar",
        icon="stellar",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/stellar/app_2.0.2",
        firmware_key="nanos/1.4.1/stellar/app_2.0.2_key",
        delete="nanos/1.4.1/stellar/app_del",
        delete_key="nanos/1.4.1/stellar/app_del_key",
        app=app30
    )
    appVer71.providers.add(provider1)
    appVer71.device_versions.add(device_ver5)
    appVer71.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer72 = ApplicationVersion.objects.create(
        name="Monero",
        version=3073,
        display_name="Monero",
        icon="monero",
        hash="174830b370d3a9d00fb1998fded757f4bff2abdf2110bcbe953d9d9c3b9531a8",
        perso="perso_11",
        firmware="nanos/1.4.1/monero/app_0.12.1",
        firmware_key="nanos/1.4.1/monero/app_0.12.1_key",
        delete="nanos/1.4.1/monero/app_del",
        delete_key="nanos/1.4.1/monero/app_del_key",
        app=app32
    )
    appVer72.providers.add(provider1)
    appVer72.device_versions.add(device_ver5)
    appVer72.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer73 = ApplicationVersion.objects.create(
        name="Open PGP",
        version=65793,
        display_name="Open PGP",
        icon="gnupg",
        hash="174830b370d3a9d00fb1998fded757f4bff2abdf2110bcbe953d9d9c3b9531a8",
        perso="perso_11",
        firmware="nanos/1.4.1/openpgp/app_1.1.1",
        firmware_key="nanos/1.4.1/openpgp/app_1.1.1_key",
        delete="nanos/1.4.1/openpgp/app_del",
        delete_key="nanos/1.4.1/openpgp/app_del_key",
        app=app34
    )
    appVer73.providers.add(provider1)
    appVer73.device_versions.add(device_ver5)
    appVer73.se_firmware_final_versions.add(firmware_final_ver2)
    # blue_2 ,
    appVer74 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=65810,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="26a8fb14fabce93792d43674fe7bbb4c41c7aa75ff4aacb4c9be87a1f3bf0866",
        perso="perso_11",
        firmware="blue/2.0/bitcoin/app_1.1.18",
        firmware_key="blue/2.0/bitcoin/app_1.1.18_key",
        delete="blue/2.0/bitcoin/st31_bitcoin_del",
        delete_key="blue/2.0/bitcoin/st31_bitcoin_del_key",
        app=app0
    )
    appVer74.providers.add(provider1)
    appVer74.device_versions.add(device_ver2)
    appVer74.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer75 = ApplicationVersion.objects.create(
        name="Bitcoin Cash",
        version=65800,
        display_name="Bitcoin Cash",
        icon="bitcoin_cash",
        hash="6954e8a37e6d22c703ed5bfd090b4726dbdacaf034a53d51bb80611f11e2218e",
        perso="perso_11",
        firmware="blue/2.0/bitcoin_cash/app_1.1.8",
        firmware_key="blue/2.0/bitcoin_cash/app_1.1.8_key",
        delete="blue/2.0/bitcoin_cash/app_del",
        delete_key="blue/2.0/bitcoin_cash/app_del_key",
        app=app1
    )
    appVer75.providers.add(provider1)
    appVer75.device_versions.add(device_ver2)
    appVer75.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer76 = ApplicationVersion.objects.create(
        name="Dash",
        version=65795,
        display_name="Dash",
        icon="dash",
        hash="db5daa27dc0e1c1c1a12804bc76c7ddf6cf629b197b903fd33a30912c48b6b63",
        perso="perso_11",
        firmware="blue/2.0/dash/st31_dash_1.1.3",
        firmware_key="blue/2.0/dash/st31_dash_1.1.3_key",
        delete="blue/2.0/dash/st31_dash_del",
        delete_key="blue/2.0/dash/st31_dash_del_key",
        app=app14
    )
    appVer76.providers.add(provider1)
    appVer76.device_versions.add(device_ver2)
    appVer76.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer77 = ApplicationVersion.objects.create(
        name="Dogecoin",
        version=65795,
        display_name="Dogecoin",
        icon="dogecoin",
        hash="2d1b29dea559480c33ddaf748cea7a87b76218de45abb148a34a789cb6c002f5",
        perso="perso_11",
        firmware="blue/2.0/dogecoin/st31_dogecoin_1.1.3",
        firmware_key="blue/2.0/dogecoin/st31_dogecoin_1.1.3_key",
        delete="blue/2.0/dogecoin/st31_dogecoin_del",
        delete_key="blue/2.0/dogecoin/st31_dogecoin_del_key",
        app=app15
    )
    appVer77.providers.add(provider1)
    appVer77.device_versions.add(device_ver2)
    appVer77.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer78 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65558,
        display_name="Ethereum",
        icon="ethereum",
        hash="2c3b61f253450da4b3667ba6645dbd98b5d2c60d0cad62d71a08e0021692b011",
        perso="perso_11",
        firmware="blue/2.0/ethereum/app_1.0.22",
        firmware_key="blue/2.0/ethereum/app_1.0.22_key",
        delete="blue/2.0/ethereum/st31_etc_del",
        delete_key="blue/2.0/ethereum/st31_etc_del_key",
        app=app16
    )
    appVer78.providers.add(provider1)
    appVer78.device_versions.add(device_ver2)
    appVer78.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer79 = ApplicationVersion.objects.create(
        name="Fido U2F",
        version=65792,
        display_name="Fido U2F",
        icon="fido",
        hash="ed9d338f59504b332b90d730cc7ef77674fb5adbb1bd420d890cfe3b5c45e6d3",
        perso="perso_11",
        firmware="blue/2.0/fido_u2f/st31_fido_u2f_1.1.0",
        firmware_key="blue/2.0/fido_u2f/st31_fido_u2f_1.1.0_key",
        delete="blue/2.0/fido_u2f/st31_fido_u2f_del",
        delete_key="blue/2.0/fido_u2f/st31_fido_u2f_del_key",
        app=app17
    )
    appVer79.providers.add(provider1)
    appVer79.device_versions.add(device_ver2)
    appVer79.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer80 = ApplicationVersion.objects.create(
        name="Litecoin",
        version=65801,
        display_name="Litecoin",
        icon="litecoin",
        hash="5312d11011eb31c7ffd9196c40c1385a508649e53d1b65fd95cea6c9231aad81",
        perso="perso_11",
        firmware="blue/2.0/litecoin/app_1.1.9",
        firmware_key="blue/2.0/litecoin/app_1.1.9_key",
        delete="blue/2.0/litecoin/st31_litecoin_del",
        delete_key="blue/2.0/litecoin/st31_litecoin_del_key",
        app=app18
    )
    appVer80.providers.add(provider1)
    appVer80.device_versions.add(device_ver2)
    appVer80.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer81 = ApplicationVersion.objects.create(
        name="Stratis",
        version=65795,
        display_name="Stratis",
        icon="stratis",
        hash="e39aab3f6062a8b9a567bfd358b8500ff3272caad02e3422d6093fe5b833e853",
        perso="perso_11",
        firmware="blue/2.0/stratis/st31_stratis_1.1.3",
        firmware_key="blue/2.0/stratis/st31_stratis_1.1.3_key",
        delete="blue/2.0/stratis/st31_stratis_del",
        delete_key="blue/2.0/stratis/st31_stratis_del_key",
        app=app19
    )
    appVer81.providers.add(provider1)
    appVer81.device_versions.add(device_ver2)
    appVer81.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer82 = ApplicationVersion.objects.create(
        name="Zcash",
        version=65795,
        display_name="Zcash",
        icon="zcash",
        hash="b01de65cc1f8db466c9d872d866aa7672c30fc6cc90b5fc4cd0ff26f29ceefdb",
        perso="perso_11",
        firmware="blue/2.0/zcash/st31_zcash_1.1.3",
        firmware_key="blue/2.0/zcash/st31_zcash_1.1.3_key",
        delete="blue/2.0/zcash/st31_zcash_del",
        delete_key="blue/2.0/zcash/st31_zcash_del_key",
        app=app21
    )
    appVer82.providers.add(provider1)
    appVer82.device_versions.add(device_ver2)
    appVer82.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer83 = ApplicationVersion.objects.create(
        name="Ripple",
        version=65539,
        display_name="Ripple",
        icon="ripple",
        hash="609db324fd55e570aa4e342d748694518ff6497e3e1fa9acaed1413077b0e6dd",
        perso="perso_11",
        firmware="blue/2.0/ripple/app_1.0.3",
        firmware_key="blue/2.0/ripple/app_1.0.3_key",
        delete="blue/2.0/ripple/app_del",
        delete_key="blue/2.0/ripple/app_del_key",
        app=app20
    )
    appVer83.providers.add(provider1)
    appVer83.device_versions.add(device_ver2)
    appVer83.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer84 = ApplicationVersion.objects.create(
        name="PoSW",
        version=65810,
        display_name="PoSW",
        icon="posw",
        hash="db36cbd73ce71a2e27a88f9491053c14def9553014c3d60059bea3dc810f1e72",
        perso="perso_11",
        firmware="blue/2.0/posw/app_1.1.18",
        firmware_key="blue/2.0/posw/app_1.1.18_key",
        delete="blue/2.0/posw/app_del",
        delete_key="blue/2.0/posw/app_del_key",
        app=app25
    )
    appVer84.providers.add(provider1)
    appVer84.device_versions.add(device_ver2)
    appVer84.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer85 = ApplicationVersion.objects.create(
        name="Ubiq",
        version=65558,
        display_name="Ubiq",
        icon="ubiq",
        hash="4479fc4c73b5b7ed8e992ed7bbd5341bc51998c7062d705027bede1d33dad8cb",
        perso="perso_11",
        firmware="blue/2.0/ubiq/app_1.0.22",
        firmware_key="blue/2.0/ubiq/app_1.0.22_key",
        delete="blue/2.0/ubiq/app_del",
        delete_key="blue/2.0/ubiq/app_del_key",
        app=app12
    )
    appVer85.providers.add(provider1)
    appVer85.device_versions.add(device_ver2)
    appVer85.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer86 = ApplicationVersion.objects.create(
        name="Expanse",
        version=65556,
        display_name="Expanse",
        icon="expanse",
        hash="4479fc4c73b5b7ed8e992ed7bbd5341bc51998c7062d705027bede1d33dad8cb",
        perso="perso_11",
        firmware="blue/2.0/expanse/app_1.0.20",
        firmware_key="blue/2.0/expanse/app_1.0.20_key",
        delete="blue/2.0/expanse/app_del",
        delete_key="blue/2.0/expanse/app_del_key",
        app=app13
    )
    appVer86.providers.add(provider1)
    appVer86.device_versions.add(device_ver2)
    appVer86.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer87 = ApplicationVersion.objects.create(
        name="PIVX",
        version=65804,
        display_name="PIVX",
        icon="pivx",
        hash="edd14efe02989581eac13cf0d59cdde8d9a697078ac48d45926c7229eb02323a",
        perso="perso_11",
        firmware="blue/2.0/pivx/app_1.1.12",
        firmware_key="blue/2.0/pivx/app_1.1.12_key",
        delete="blue/2.0/pivx/app_del",
        delete_key="blue/2.0/pivx/app_del_key",
        app=app8
    )
    appVer87.providers.add(provider1)
    appVer87.device_versions.add(device_ver2)
    appVer87.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer88 = ApplicationVersion.objects.create(
        name="Stealthcoin",
        version=65802,
        display_name="Stealthcoin",
        icon="stealthcoin",
        hash="603a135af8d8b222cc55e3f47f0ee96ec9ab84afabfe4b0a0c194568a1e9e2f1",
        perso="perso_11",
        firmware="blue/2.0/stealthcoin/app_1.1.10",
        firmware_key="blue/2.0/stealthcoin/app_1.1.10_key",
        delete="blue/2.0/stealthcoin/app_del",
        delete_key="blue/2.0/stealthcoin/app_del_key",
        app=app38
    )
    appVer88.providers.add(provider1)
    appVer88.device_versions.add(device_ver2)
    appVer88.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer89 = ApplicationVersion.objects.create(
        name="Vertcoin",
        version=65802,
        display_name="Vertcoin",
        icon="vertcoin",
        hash="1660611c2116ebba45473e6e29a697f5440c7fcf65eae70caa9c4a49f1bb253b",
        perso="perso_11",
        firmware="blue/2.0/vertcoin/app_1.1.10",
        firmware_key="blue/2.0/vertcoin/app_1.1.10_key",
        delete="blue/2.0/vertcoin/app_del",
        delete_key="blue/2.0/vertcoin/app_del_key",
        app=app10
    )
    appVer89.providers.add(provider1)
    appVer89.device_versions.add(device_ver2)
    appVer89.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer90 = ApplicationVersion.objects.create(
        name="Viacoin",
        version=65802,
        display_name="Viacoin",
        icon="viacoin",
        hash="4479fc4c73b5b7ed8e992ed7bbd5341bc51998c7062d705027bede1d33dad8cb",
        perso="perso_11",
        firmware="blue/2.0/viacoin/app_1.1.10",
        firmware_key="blue/2.0/viacoin/app_1.1.10_key",
        delete="blue/2.0/viacoin/app_del",
        delete_key="blue/2.0/viacoin/app_del_key",
        app=app11
    )
    appVer90.providers.add(provider1)
    appVer90.device_versions.add(device_ver2)
    appVer90.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer91 = ApplicationVersion.objects.create(
        name="Komodo",
        version=65804,
        display_name="Komodo",
        icon="komodo",
        hash="c547ddf5cd48af469ecffef224e159560d97b151a4f9c74af22420e56aa59fa0",
        perso="perso_11",
        firmware="blue/2.0/komodo/app_1.1.12",
        firmware_key="blue/2.0/komodo/app_1.1.12_key",
        delete="blue/2.0/komodo/app_del",
        delete_key="blue/2.0/komodo/app_del_key",
        app=app23
    )
    appVer91.providers.add(provider1)
    appVer91.device_versions.add(device_ver2)
    appVer91.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer92 = ApplicationVersion.objects.create(
        name="Bitcoin Gold",
        version=65808,
        display_name="Bitcoin Gold",
        icon="bitcoin_gold",
        hash="c547ddf5cd48af469ecffef224e159560d97b151a4f9c74af22420e56aa59fa0",
        perso="perso_11",
        firmware="blue/2.0/bitcoin_gold/app_1.1.16",
        firmware_key="blue/2.0/bitcoin_gold/app_1.1.16_key",
        delete="blue/2.0/bitcoin_gold/app_del",
        delete_key="blue/2.0/bitcoin_gold/app_del_key",
        app=app2
    )
    appVer92.providers.add(provider1)
    appVer92.device_versions.add(device_ver2)
    appVer92.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer93 = ApplicationVersion.objects.create(
        name="Digibyte",
        version=65809,
        display_name="Digibyte",
        icon="digibyte",
        hash="7a92fc61e579ad757bae8f12ecfdb371aedd1a2e15eacea1a21c44024f90d709",
        perso="perso_11",
        firmware="blue/2.0/digibyte/app_1.1.17",
        firmware_key="blue/2.0/digibyte/app_1.1.17_key",
        delete="blue/2.0/digibyte/app_del",
        delete_key="blue/2.0/digibyte/app_del_key",
        app=app5
    )
    appVer93.providers.add(provider1)
    appVer93.device_versions.add(device_ver2)
    appVer93.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer94 = ApplicationVersion.objects.create(
        name="HCash",
        version=65809,
        display_name="HCash",
        icon="hcash",
        hash="7a92fc61e579ad757bae8f12ecfdb371aedd1a2e15eacea1a21c44024f90d709",
        perso="perso_11",
        firmware="blue/2.0/hcash/app_1.1.17",
        firmware_key="blue/2.0/hcash/app_1.1.17_key",
        delete="blue/2.0/hcash/app_del",
        delete_key="blue/2.0/hcash/app_del_key",
        app=app6
    )
    appVer94.providers.add(provider1)
    appVer94.device_versions.add(device_ver2)
    appVer94.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer95 = ApplicationVersion.objects.create(
        name="Qtum",
        version=65809,
        display_name="Qtum",
        icon="qtum",
        hash="7a92fc61e579ad757bae8f12ecfdb371aedd1a2e15eacea1a21c44024f90d709",
        perso="perso_11",
        firmware="blue/2.0/qtum/app_1.1.17",
        firmware_key="blue/2.0/qtum/app_1.1.17_key",
        delete="blue/2.0/qtum/app_del",
        delete_key="blue/2.0/qtum/app_del_key",
        app=app7
    )
    appVer95.providers.add(provider1)
    appVer95.device_versions.add(device_ver2)
    appVer95.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer96 = ApplicationVersion.objects.create(
        name="Neo",
        version=65794,
        display_name="Neo",
        icon="neo",
        hash="aebc6e90441df100e985ad53243f86271f5073bd69fddb5dacb8c748466523e5",
        perso="perso_11",
        firmware="blue/2.0/neo/app_1.1.2",
        firmware_key="blue/2.0/neo/app_1.1.2_key",
        delete="blue/2.0/neo/app_del",
        delete_key="blue/2.0/neo/app_del_key",
        app=app27
    )
    appVer96.providers.add(provider1)
    appVer96.device_versions.add(device_ver2)
    appVer96.se_firmware_final_versions.add(firmware_final_ver0)
    # blue_2 ,
    appVer97 = ApplicationVersion.objects.create(
        name="Stellar",
        version=131074,
        display_name="Stellar",
        icon="stellar",
        hash="aebc6e90441df100e985ad53243f86271f5073bd69fddb5dacb8c748466523e5",
        perso="perso_11",
        firmware="blue/2.0/stellar/app_2.0.2",
        firmware_key="blue/2.0/stellar/app_2.0.2_key",
        delete="blue/2.0/stellar/app_del",
        delete_key="blue/2.0/stellar/app_del_key",
        app=app30
    )
    appVer97.providers.add(provider1)
    appVer97.device_versions.add(device_ver2)
    appVer97.se_firmware_final_versions.add(firmware_final_ver0)
    # nanos ,
    appVer98 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=65810,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="00a56bce3651ad87092721ef3626866ca3413b334e9a392e2561ee9d4150f956",
        perso="perso_11",
        firmware="nanos/1.3.1/bitcoin/app_1.1.18",
        firmware_key="nanos/1.3.1/bitcoin/app_1.1.18_key",
        delete="nanos/1.3.1/bitcoin/st31_bitcoin_del",
        delete_key="nanos/1.3.1/bitcoin/st31_bitcoin_del_key",
        app=app0
    )
    appVer98.providers.add(provider1)
    appVer98.device_versions.add(device_ver1)
    appVer98.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer99 = ApplicationVersion.objects.create(
        name="Bitcoin Cash",
        version=65800,
        display_name="Bitcoin Cash",
        icon="bitcoin_cash",
        hash="a7b1d4f91ff90697c2a532bfed60b85e5f4ff55bbfc92fe9d3d13994fe0a8cbf",
        perso="perso_11",
        firmware="nanos/1.3.1/bitcoin_cash/app_1.1.8",
        firmware_key="nanos/1.3.1/bitcoin_cash/app_1.1.8_key",
        delete="nanos/1.3.1/bitcoin_cash/app_del",
        delete_key="nanos/1.3.1/bitcoin_cash/app_del_key",
        app=app1
    )
    appVer99.providers.add(provider1, provider2)
    appVer99.device_versions.add(device_ver1)
    appVer99.se_firmware_final_versions.add(
        firmware_final_ver1, firmware_final_ver5)
    # nanos ,
    appVer100 = ApplicationVersion.objects.create(
        name="Dash",
        version=65797,
        display_name="Dash",
        icon="dash",
        hash="3d15fb18db1f258c8b20b549b7fb4bf3e6d79c84e4c973081674b039440b34cf",
        perso="perso_11",
        firmware="nanos/1.3.1/dash/st31_dash_1.1.5",
        firmware_key="nanos/1.3.1/dash/st31_dash_1.1.5_key",
        delete="nanos/1.3.1/dash/st31_dash_del",
        delete_key="nanos/1.3.1/dash/st31_dash_del_key",
        app=app14
    )
    appVer100.providers.add(provider1)
    appVer100.device_versions.add(device_ver1)
    appVer100.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer101 = ApplicationVersion.objects.create(
        name="Dogecoin",
        version=65797,
        display_name="Dogecoin",
        icon="dogecoin",
        hash="46b6a0903b1e6c72bd9a258a32fb47596406c98778631d56f5be4f6a437697f0",
        perso="perso_11",
        firmware="nanos/1.3.1/dogecoin/st31_dogecoin_1.1.5",
        firmware_key="nanos/1.3.1/dogecoin/st31_dogecoin_1.1.5_key",
        delete="nanos/1.3.1/dogecoin/st31_dogecoin_del",
        delete_key="nanos/1.3.1/dogecoin/st31_dogecoin_del_key",
        app=app15
    )
    appVer101.providers.add(provider1)
    appVer101.device_versions.add(device_ver1)
    appVer101.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer102 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65558,
        display_name="Ethereum",
        icon="ethereum",
        hash="ec12c2b7bd6d6809c3e11d5a078c39f7d60ccd2e67a07341e0bf1b3861849444",
        perso="perso_11",
        firmware="nanos/1.3.1/ethereum/app_1.0.22",
        firmware_key="nanos/1.3.1/ethereum/app_1.0.22_key",
        delete="nanos/1.3.1/ethereum/st31_etc_del",
        delete_key="nanos/1.3.1/ethereum/st31_etc_del_key",
        app=app16
    )
    appVer102.providers.add(provider1)
    appVer102.device_versions.add(device_ver1)
    appVer102.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer103 = ApplicationVersion.objects.create(
        name="Fido U2F",
        version=66049,
        display_name="Fido U2F",
        icon="fido",
        hash="ea3dd20fea3828a3ea3f05452a239f6bda2af1946e43c65cbf406a14a24ec73f",
        perso="perso_11",
        firmware="nanos/1.3.1/fido_u2f/st31_fido_u2f_1.2.1",
        firmware_key="nanos/1.3.1/fido_u2f/st31_fido_u2f_1.2.1_key",
        delete="nanos/1.3.1/fido_u2f/st31_fido_u2f_del",
        delete_key="nanos/1.3.1/fido_u2f/st31_fido_u2f_del_key",
        app=app17
    )
    appVer103.providers.add(provider1)
    appVer103.device_versions.add(device_ver1)
    appVer103.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer104 = ApplicationVersion.objects.create(
        name="Komodo",
        version=65797,
        display_name="Komodo",
        icon="komodo",
        hash="723b170ba1d8f8f65278fe73f8514f056ef67c91dd4a41e2caa17ba33bd92903",
        perso="perso_11",
        firmware="nanos/1.3.1/komodo/st31_komodo_1.1.5",
        firmware_key="nanos/1.3.1/komodo/st31_komodo_1.1.5_key",
        delete="nanos/1.3.1/komodo/st31_komodo_del",
        delete_key="nanos/1.3.1/komodo/st31_komodo_del_key",
        app=app23
    )
    appVer104.providers.add(provider1)
    appVer104.device_versions.add(device_ver1)
    appVer104.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer105 = ApplicationVersion.objects.create(
        name="Litecoin",
        version=65801,
        display_name="Litecoin",
        icon="litecoin",
        hash="9cbd9f0916ddb2fc915ba7ca97fb8427a6ba160e3b2d083df966c039d68ea5ab",
        perso="perso_11",
        firmware="nanos/1.3.1/litecoin/app_1.1.9",
        firmware_key="nanos/1.3.1/litecoin/app_1.1.9_key",
        delete="nanos/1.3.1/litecoin/st31_litecoin_del",
        delete_key="nanos/1.3.1/litecoin/st31_litecoin_del_key",
        app=app18
    )
    appVer105.providers.add(provider1)
    appVer105.device_versions.add(device_ver1)
    appVer105.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer106 = ApplicationVersion.objects.create(
        name="Stratis",
        version=65797,
        display_name="Stratis",
        icon="stratis",
        hash="17899eeadf9e4dd12fc2a362b2ba1f8fde140072112ebbb0171b0735bab4dba5",
        perso="perso_11",
        firmware="nanos/1.3.1/stratis/st31_stratis_1.1.5",
        firmware_key="nanos/1.3.1/stratis/st31_stratis_1.1.5_key",
        delete="nanos/1.3.1/stratis/st31_stratis_del",
        delete_key="nanos/1.3.1/stratis/st31_stratis_del_key",
        app=app19
    )
    appVer106.providers.add(provider1)
    appVer106.device_versions.add(device_ver1)
    appVer106.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer107 = ApplicationVersion.objects.create(
        name="Zcash",
        version=65797,
        display_name="Zcash",
        icon="zcash",
        hash="4cdfe945337afd00ff75c82dbb526e086e514892447fdcc046e4e80ac68cc155",
        perso="perso_11",
        firmware="nanos/1.3.1/zcash/st31_zcash_1.1.5",
        firmware_key="nanos/1.3.1/zcash/st31_zcash_1.1.5_key",
        delete="nanos/1.3.1/zcash/st31_zcash_del",
        delete_key="nanos/1.3.1/zcash/st31_zcash_del_key",
        app=app21
    )
    appVer107.providers.add(provider1)
    appVer107.device_versions.add(device_ver1)
    appVer107.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer108 = ApplicationVersion.objects.create(
        name="SSH/GPG Agent",
        version=3,
        display_name="SSH/GPG Agent",
        icon="ssh",
        hash="9b52a2b0532c3bbb058a6c817b02963174f32b3d41314f7b507623f163d71b65",
        perso="perso_11",
        firmware="nanos/1.3.1/ssh-agent/st31_gpg_0.0.3",
        firmware_key="nanos/1.3.1/ssh-agent/st31_gpg_0.0.3_key",
        delete="nanos/1.3.1/ssh-agent/st31_gpg_del",
        delete_key="nanos/1.3.1/ssh-agent/st31_gpg_del_key",
        app=app28
    )
    appVer108.providers.add(provider1)
    appVer108.device_versions.add(device_ver1)
    appVer108.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer109 = ApplicationVersion.objects.create(
        name="Passwords Manager",
        version=3,
        display_name="Passwords Manager",
        icon="passwords",
        hash="153245e3a042ef467bfe2553bc2d6e0f54cadbd0c519f7a46808237ace1ce507",
        perso="perso_11",
        firmware="nanos/1.3.1/pwmgr/app_0.0.3",
        firmware_key="nanos/1.3.1/pwmgr/app_0.0.3_key",
        delete="nanos/1.3.1/pwmgr/app_del",
        delete_key="nanos/1.3.1/pwmgr/app_del_key",
        app=app29
    )
    appVer109.providers.add(provider1)
    appVer109.device_versions.add(device_ver1)
    appVer109.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer110 = ApplicationVersion.objects.create(
        name="Open PGP",
        version=65792,
        display_name="Open PGP",
        icon="gnupg",
        hash="174830b370d3a9d00fb1998fded757f4bff2abdf2110bcbe953d9d9c3b9531a8",
        perso="perso_11",
        firmware="nanos/1.3.1/openpgp/app_1.1.0",
        firmware_key="nanos/1.3.1/openpgp/app_1.1.0_key",
        delete="nanos/1.3.1/openpgp/app_del",
        delete_key="nanos/1.3.1/openpgp/app_del_key",
        app=app34
    )
    appVer110.providers.add(provider1)
    appVer110.device_versions.add(device_ver1)
    appVer110.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer111 = ApplicationVersion.objects.create(
        name="Hello",
        version=65536,
        display_name="Hello",
        icon="hello",
        hash="f01bfbaa19e01ada00688eeb01aaadaf74e929e0b22bc788f95b1f012463f0de",
        perso="perso_11",
        firmware="nanos/1.3.1/hello/app_1.0.0",
        firmware_key="nanos/1.3.1/hello/app_1.0.0_key",
        delete="nanos/1.3.1/hello/app_del",
        delete_key="nanos/1.3.1/hello/app_del_key",
        app=app33
    )
    appVer111.providers.add(provider1)
    appVer111.device_versions.add(device_ver1)
    appVer111.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer112 = ApplicationVersion.objects.create(
        name="Ripple",
        version=65539,
        display_name="Ripple",
        icon="ripple",
        hash="ec52db93529d63e19d9870692b0faff77b3dc49e86c81dcec90cddf6e1493f0d",
        perso="perso_11",
        firmware="nanos/1.3.1/ripple/app_1.0.3",
        firmware_key="nanos/1.3.1/ripple/app_1.0.3_key",
        delete="nanos/1.3.1/ripple/app_del",
        delete_key="nanos/1.3.1/ripple/app_del_key",
        app=app20
    )
    appVer112.providers.add(provider1, provider2)
    appVer112.device_versions.add(device_ver1)
    appVer112.se_firmware_final_versions.add(
        firmware_final_ver1, firmware_final_ver5)
    # nanos ,
    appVer113 = ApplicationVersion.objects.create(
        name="PoSW",
        version=65799,
        display_name="PoSW",
        icon="posw",
        hash="2bc0a8e0bc0c0ecd5cebd35a0f6943dd5f097ca99879096f961d639cfb57f3e8",
        perso="perso_11",
        firmware="nanos/1.3.1/posw/app_1.1.7",
        firmware_key="nanos/1.3.1/posw/app_1.1.7_key",
        delete="nanos/1.3.1/posw/app_del",
        delete_key="nanos/1.3.1/posw/app_del_key",
        app=app25
    )
    appVer113.providers.add(provider1)
    appVer113.device_versions.add(device_ver1)
    appVer113.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer114 = ApplicationVersion.objects.create(
        name="Ark",
        version=257,
        display_name="Ark",
        icon="ark",
        hash="213116583dd15e1e7aeb1ea1891ec6dbd9f357da5d979ff23313a21ba5455ad0",
        perso="perso_11",
        firmware="nanos/1.3.1/ark/app_0.1.1",
        firmware_key="nanos/1.3.1/ark/app_0.1.1_key",
        delete="nanos/1.3.1/ark/app_del",
        delete_key="nanos/1.3.1/ark/app_del_key",
        app=app26
    )
    appVer114.providers.add(provider1)
    appVer114.device_versions.add(device_ver1)
    appVer114.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer115 = ApplicationVersion.objects.create(
        name="Ubiq",
        version=65558,
        display_name="Ubiq",
        icon="ubiq",
        hash="5b89eedd5135a55a69396c4f9f94d280262d171fade6f368b09c6a6011741944",
        perso="perso_11",
        firmware="nanos/1.3.1/ubiq/app_1.0.22",
        firmware_key="nanos/1.3.1/ubiq/app_1.0.22_key",
        delete="nanos/1.3.1/ubiq/app_del",
        delete_key="nanos/1.3.1/ubiq/app_del_key",
        app=app12
    )
    appVer115.providers.add(provider1)
    appVer115.device_versions.add(device_ver1)
    appVer115.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer116 = ApplicationVersion.objects.create(
        name="Expanse",
        version=65556,
        display_name="Expanse",
        icon="expanse",
        hash="5b89eedd5135a55a69396c4f9f94d280262d171fade6f368b09c6a6011741944",
        perso="perso_11",
        firmware="nanos/1.3.1/expanse/app_1.0.20",
        firmware_key="nanos/1.3.1/expanse/app_1.0.20_key",
        delete="nanos/1.3.1/expanse/app_del",
        delete_key="nanos/1.3.1/expanse/app_del_key",
        app=app13
    )
    appVer116.providers.add(provider1)
    appVer116.device_versions.add(device_ver1)
    appVer116.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer117 = ApplicationVersion.objects.create(
        name="PIVX",
        version=65804,
        display_name="PIVX",
        icon="pivx",
        hash="b4e1e81987cab9933994f440eaff6035a62f622aa36d3c2b97f0e1a4990e7bfb",
        perso="perso_11",
        firmware="nanos/1.3.1/pivx/app_1.1.12",
        firmware_key="nanos/1.3.1/pivx/app_1.1.12_key",
        delete="nanos/1.3.1/pivx/app_del",
        delete_key="nanos/1.3.1/pivx/app_del_key",
        app=app8
    )
    appVer117.providers.add(provider1)
    appVer117.device_versions.add(device_ver1)
    appVer117.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer118 = ApplicationVersion.objects.create(
        name="Stealthcoin",
        version=65802,
        display_name="Stealthcoin",
        icon="stealthcoin",
        hash="9fa6e9971aa884d117f5e16db80e8f897b39b0e30728389cc74acd680439ebb1",
        perso="perso_11",
        firmware="nanos/1.3.1/stealthcoin/app_1.1.10",
        firmware_key="nanos/1.3.1/stealthcoin/app_1.1.10_key",
        delete="nanos/1.3.1/stealthcoin/app_del",
        delete_key="nanos/1.3.1/stealthcoin/app_del_key",
        app=app38
    )
    appVer118.providers.add(provider1)
    appVer118.device_versions.add(device_ver1)
    appVer118.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer119 = ApplicationVersion.objects.create(
        name="Vertcoin",
        version=65802,
        display_name="Vertcoin",
        icon="vertcoin",
        hash="aebc6e90441df100e985ad53243f86271f5073bd69fddb5dacb8c748466523e5",
        perso="perso_11",
        firmware="nanos/1.3.1/vertcoin/app_1.1.10",
        firmware_key="nanos/1.3.1/vertcoin/app_1.1.10_key",
        delete="nanos/1.3.1/vertcoin/app_del",
        delete_key="nanos/1.3.1/vertcoin/app_del_key",
        app=app10
    )
    appVer119.providers.add(provider1)
    appVer119.device_versions.add(device_ver1)
    appVer119.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer120 = ApplicationVersion.objects.create(
        name="Viacoin",
        version=65802,
        display_name="Viacoin",
        icon="viacoin",
        hash="5b89eedd5135a55a69396c4f9f94d280262d171fade6f368b09c6a6011741944",
        perso="perso_11",
        firmware="nanos/1.3.1/viacoin/app_1.1.10",
        firmware_key="nanos/1.3.1/viacoin/app_1.1.10_key",
        delete="nanos/1.3.1/viacoin/app_del",
        delete_key="nanos/1.3.1/viacoin/app_del_key",
        app=app11
    )
    appVer120.providers.add(provider1)
    appVer120.device_versions.add(device_ver1)
    appVer120.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer121 = ApplicationVersion.objects.create(
        name="Bitcoin testnet",
        version=65802,
        display_name="Bitcoin testnet",
        icon="bitcoin_testnet",
        hash="7a92fc61e579ad757bae8f12ecfdb371aedd1a2e15eacea1a21c44024f90d709",
        perso="perso_11",
        firmware="nanos/1.3.1/bitcoin_testnet/app_1.1.10",
        firmware_key="nanos/1.3.1/bitcoin_testnet/app_1.1.10_key",
        delete="nanos/1.3.1/bitcoin_testnet/app_del",
        delete_key="nanos/1.3.1/bitcoin_testnet/app_del_key",
        app=app4
    )
    appVer121.providers.add(provider1)
    appVer121.device_versions.add(device_ver1)
    appVer121.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer122 = ApplicationVersion.objects.create(
        name="Neo",
        version=65793,
        display_name="Neo",
        icon="neo",
        hash="aebc6e90441df100e985ad53243f86271f5073bd69fddb5dacb8c748466523e5",
        perso="perso_11",
        firmware="nanos/1.3.1/neo/app_1.1.1",
        firmware_key="nanos/1.3.1/neo/app_1.1.1_key",
        delete="nanos/1.3.1/neo/app_del",
        delete_key="nanos/1.3.1/neo/app_del_key",
        app=app27
    )
    appVer122.providers.add(provider1)
    appVer122.device_versions.add(device_ver1)
    appVer122.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer123 = ApplicationVersion.objects.create(
        name="Bitcoin Gold",
        version=65808,
        display_name="Bitcoin Gold",
        icon="bitcoin_gold",
        hash="9fa6e9971aa884d117f5e16db80e8f897b39b0e30728389cc74acd680439ebb1",
        perso="perso_11",
        firmware="nanos/1.3.1/bitcoin_gold/app_1.1.16",
        firmware_key="nanos/1.3.1/bitcoin_gold/app_1.1.16_key",
        delete="nanos/1.3.1/bitcoin_gold/app_del",
        delete_key="nanos/1.3.1/bitcoin_gold/app_del_key",
        app=app2
    )
    appVer123.providers.add(provider1)
    appVer123.device_versions.add(device_ver1)
    appVer123.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer124 = ApplicationVersion.objects.create(
        name="Stellar",
        version=131072,
        display_name="Stellar",
        icon="stellar",
        hash="9fa6e9971aa884d117f5e16db80e8f897b39b0e30728389cc74acd680439ebb1",
        perso="perso_11",
        firmware="nanos/1.3.1/stellar/app_2.0.0",
        firmware_key="nanos/1.3.1/stellar/app_2.0.0_key",
        delete="nanos/1.3.1/stellar/app_del",
        delete_key="nanos/1.3.1/stellar/app_del_key",
        app=app30
    )
    appVer124.providers.add(provider1)
    appVer124.device_versions.add(device_ver1)
    appVer124.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer125 = ApplicationVersion.objects.create(
        name="Digibyte",
        version=65809,
        display_name="Digibyte",
        icon="digibyte",
        hash="7a92fc61e579ad757bae8f12ecfdb371aedd1a2e15eacea1a21c44024f90d709",
        perso="perso_11",
        firmware="nanos/1.3.1/digibyte/app_1.1.17",
        firmware_key="nanos/1.3.1/digibyte/app_1.1.17_key",
        delete="nanos/1.3.1/digibyte/app_del",
        delete_key="nanos/1.3.1/digibyte/app_del_key",
        app=app5
    )
    appVer125.providers.add(provider1)
    appVer125.device_versions.add(device_ver1)
    appVer125.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer126 = ApplicationVersion.objects.create(
        name="HCash",
        version=65809,
        display_name="HCash",
        icon="hcash",
        hash="7a92fc61e579ad757bae8f12ecfdb371aedd1a2e15eacea1a21c44024f90d709",
        perso="perso_11",
        firmware="nanos/1.3.1/hcash/app_1.1.17",
        firmware_key="nanos/1.3.1/hcash/app_1.1.17_key",
        delete="nanos/1.3.1/hcash/app_del",
        delete_key="nanos/1.3.1/hcash/app_del_key",
        app=app6
    )
    appVer126.providers.add(provider1)
    appVer126.device_versions.add(device_ver1)
    appVer126.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer127 = ApplicationVersion.objects.create(
        name="Qtum",
        version=65809,
        display_name="Qtum",
        icon="qtum",
        hash="7a92fc61e579ad757bae8f12ecfdb371aedd1a2e15eacea1a21c44024f90d709",
        perso="perso_11",
        firmware="nanos/1.3.1/qtum/app_1.1.17",
        firmware_key="nanos/1.3.1/qtum/app_1.1.17_key",
        delete="nanos/1.3.1/qtum/app_del",
        delete_key="nanos/1.3.1/qtum/app_del_key",
        app=app7
    )
    appVer127.providers.add(provider1)
    appVer127.device_versions.add(device_ver1)
    appVer127.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer128 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=65801,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="c6a1400a5d28bba6fb666a1b2c8901526b78d314f3d4b030f9cd31e88b9ab609",
        perso="perso_club_10",
        firmware="nanos/1.3.1/bitcoin/app_1.1.9",
        firmware_key="nanos/1.3.1/bitcoin/app_1.1.9_key",
        delete="nanos/1.3.1/bitcoin/st31_bitcoin_del",
        delete_key="nanos/1.3.1/bitcoin/st31_bitcoin_del_key",
        app=app0
    )
    appVer128.providers.add(provider3)
    appVer128.device_versions.add(device_ver0)
    appVer128.se_firmware_final_versions.add(firmware_final_ver6)
    # nanos ,
    appVer129 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65554,
        display_name="Ethereum",
        icon="ethereum",
        hash="326dae4cb72f3b1c3dd82c1f5b5e8d40d5efaf85ca2fea01cd7f03e8d9a61f59",
        perso="perso_club_10",
        firmware="nanos/1.3.1/ethereum/app_1.0.18",
        firmware_key="nanos/1.3.1/ethereum/app_1.0.18_key",
        delete="nanos/1.3.1/ethereum/st31_etc_del",
        delete_key="nanos/1.3.1/ethereum/st31_etc_del_key",
        app=app16
    )
    appVer129.providers.add(provider3)
    appVer129.device_versions.add(device_ver0)
    appVer129.se_firmware_final_versions.add(firmware_final_ver6)
    # nanos ,
    appVer130 = ApplicationVersion.objects.create(
        name="Clubcoin",
        version=65805,
        display_name="Clubcoin",
        icon="clubcoin",
        hash="213116583dd15e1e7aeb1ea1891ec6dbd9f357da5d979ff23313a21ba5455ad0",
        perso="perso_club_10",
        firmware="nanos/1.3.1-club/clubcoin/app_1.1.13",
        firmware_key="nanos/1.3.1-club/clubcoin/app_1.1.13_key",
        delete="nanos/1.3.1-club/clubcoin/app_del",
        delete_key="nanos/1.3.1-club/clubcoin/app_del_key",
        app=app39
    )
    appVer130.providers.add(provider3)
    appVer130.device_versions.add(device_ver0)
    appVer130.se_firmware_final_versions.add(firmware_final_ver6)
    # nanos ,
    appVer131 = ApplicationVersion.objects.create(
        name="Zcash",
        version=65797,
        display_name="Zcash",
        icon="zcash",
        hash="4cdfe945337afd00ff75c82dbb526e086e514892447fdcc046e4e80ac68cc155",
        perso="perso_club_10",
        firmware="nanos/1.3.1/zcash/st31_zcash_1.1.5",
        firmware_key="nanos/1.3.1/zcash/st31_zcash_1.1.5_key",
        delete="nanos/1.3.1/zcash/st31_zcash_del",
        delete_key="nanos/1.3.1/zcash/st31_zcash_del_key",
        app=app21
    )
    appVer131.providers.add(provider3)
    appVer131.device_versions.add(device_ver0)
    appVer131.se_firmware_final_versions.add(firmware_final_ver6)
    # nanos ,
    appVer132 = ApplicationVersion.objects.create(
        name="Fido U2F",
        version=66049,
        display_name="Fido U2F",
        icon="fido",
        hash="ea3dd20fea3828a3ea3f05452a239f6bda2af1946e43c65cbf406a14a24ec73f",
        perso="perso_club_10",
        firmware="nanos/1.3.1/fido_u2f/st31_fido_u2f_1.2.1",
        firmware_key="nanos/1.3.1/fido_u2f/st31_fido_u2f_1.2.1_key",
        delete="nanos/1.3.1/fido_u2f/st31_fido_u2f_del",
        delete_key="nanos/1.3.1/fido_u2f/st31_fido_u2f_del_key",
        app=app17
    )
    appVer132.providers.add(provider3)
    appVer132.device_versions.add(device_ver0)
    appVer132.se_firmware_final_versions.add(firmware_final_ver6)
    # nanos ,
    appVer133 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=65801,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="c6a1400a5d28bba6fb666a1b2c8901526b78d314f3d4b030f9cd31e88b9ab609",
        perso="perso_11",
        firmware="nanos/1.3.1/bitcoin/app_1.1.9",
        firmware_key="nanos/1.3.1/bitcoin/app_1.1.9_key",
        delete="nanos/1.3.1/bitcoin/st31_bitcoin_del",
        delete_key="nanos/1.3.1/bitcoin/st31_bitcoin_del_key",
        app=app0
    )
    appVer133.providers.add(provider1, provider2)
    appVer133.device_versions.add(device_ver1)
    appVer133.se_firmware_final_versions.add(
        firmware_final_ver1, firmware_final_ver5)
    # nanos ,
    appVer135 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65554,
        display_name="Ethereum",
        icon="ethereum",
        hash="326dae4cb72f3b1c3dd82c1f5b5e8d40d5efaf85ca2fea01cd7f03e8d9a61f59",
        perso="perso_11",
        firmware="nanos/1.3.1/ethereum/app_1.0.18",
        firmware_key="nanos/1.3.1/ethereum/app_1.0.18_key",
        delete="nanos/1.3.1/ethereum/st31_etc_del",
        delete_key="nanos/1.3.1/ethereum/st31_etc_del_key",
        app=app16
    )
    appVer135.providers.add(provider1, provider2)
    appVer135.device_versions.add(device_ver1)
    appVer135.se_firmware_final_versions.add(
        firmware_final_ver1, firmware_final_ver5)
    # nanos ,
    appVer136 = ApplicationVersion.objects.create(
        name="Ripple",
        version=65539,
        display_name="Ripple",
        icon="ripple",
        hash="ec52db93529d63e19d9870692b0faff77b3dc49e86c81dcec90cddf6e1493f0d",
        perso="perso_11",
        firmware="nanos/1.3.1/ripple/app_1.0.3",
        firmware_key="nanos/1.3.1/ripple/app_1.0.3_key",
        delete="nanos/1.3.1/ripple/app_del",
        delete_key="nanos/1.3.1/ripple/app_del_key",
        app=app20
    )
    appVer136.providers.add(provider1)
    appVer136.device_versions.add(device_ver1)
    appVer136.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer137 = ApplicationVersion.objects.create(
        name="DasCoin",
        version=65793,
        display_name="DasCoin",
        icon="dascoin",
        hash="ac1bdc72608937fa9e3b1f7039d9631b116df3e97eb817e6347d4a489ce9496c",
        perso="perso_11",
        firmware="nanos/1.3.1-das/dascoin/app_1.1.1",
        firmware_key="nanos/1.3.1-das/dascoin/app_1.1.1_key",
        delete="nanos/1.3.1-das/dascoin/app_del",
        delete_key="nanos/1.3.1-das/dascoin/app_del_key",
        app=app37
    )
    appVer137.providers.add(provider2)
    appVer137.device_versions.add(device_ver1)
    appVer137.se_firmware_final_versions.add(firmware_final_ver5)
    # nanos ,
    appVer138 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=65796,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="a742419f96166f1fa5a06d671f35cec05cbbfa6233892dcd56220d0177204c6e",
        perso="perso_11",
        firmware="nanos/1.3/bitcoin/st31_bitcoin_1.1.4",
        firmware_key="nanos/1.3/bitcoin/st31_bitcoin_1.1.4_key",
        delete="nanos/1.3/bitcoin/st31_bitcoin_del",
        delete_key="nanos/1.3/bitcoin/st31_bitcoin_del_key",
        app=app0
    )
    appVer138.providers.add(provider1)
    appVer138.device_versions.add(device_ver1)
    appVer138.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer139 = ApplicationVersion.objects.create(
        name="Dash",
        version=65796,
        display_name="Dash",
        icon="dash",
        hash="d46d728b7a399b5945dd0e01dfdfd47125ac37553e1720a05370149a470d27be",
        perso="perso_11",
        firmware="nanos/1.3/dash/st31_dash_1.1.4",
        firmware_key="nanos/1.3/dash/st31_dash_1.1.4_key",
        delete="nanos/1.3/dash/st31_dash_del",
        delete_key="nanos/1.3/dash/st31_dash_del_key",
        app=app14
    )
    appVer139.providers.add(provider1)
    appVer139.device_versions.add(device_ver1)
    appVer139.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer140 = ApplicationVersion.objects.create(
        name="Dogecoin",
        version=65796,
        display_name="Dogecoin",
        icon="dogecoin",
        hash="794f822247f387401ce24931089abdf9a3fc14681dd9d1779f9df5e9f7a59df4",
        perso="perso_11",
        firmware="nanos/1.3/dogecoin/st31_dogecoin_1.1.4",
        firmware_key="nanos/1.3/dogecoin/st31_dogecoin_1.1.4_key",
        delete="nanos/1.3/dogecoin/st31_dogecoin_del",
        delete_key="nanos/1.3/dogecoin/st31_dogecoin_del_key",
        app=app15
    )
    appVer140.providers.add(provider1)
    appVer140.device_versions.add(device_ver1)
    appVer140.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer141 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65543,
        display_name="Ethereum",
        icon="ethereum",
        hash="fa323523f59e4b6ca20af334c6757eeb06c9b0fdaf782440964db39984234810",
        perso="perso_11",
        firmware="nanos/1.3/ethereum/st31_etc_1.0.7",
        firmware_key="nanos/1.3/ethereum/st31_etc_1.0.7_key",
        delete="nanos/1.3/ethereum/st31_etc_del",
        delete_key="nanos/1.3/ethereum/st31_etc_del_key",
        app=app16
    )
    appVer141.providers.add(provider1)
    appVer141.device_versions.add(device_ver1)
    appVer141.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer142 = ApplicationVersion.objects.create(
        name="Fido U2F",
        version=66048,
        display_name="Fido U2F",
        icon="fido",
        hash="01bbc8d906a2dd6cb989783c0e4d51225e958cec48c545056b041b9e4735a9d5",
        perso="perso_11",
        firmware="nanos/1.3/fido_u2f/st31_fido_u2f_1.2.0",
        firmware_key="nanos/1.3/fido_u2f/st31_fido_u2f_1.2.0_key",
        delete="nanos/1.3/fido_u2f/st31_fido_u2f_del",
        delete_key="nanos/1.3/fido_u2f/st31_fido_u2f_del_key",
        app=app17
    )
    appVer142.providers.add(provider1)
    appVer142.device_versions.add(device_ver1)
    appVer142.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer143 = ApplicationVersion.objects.create(
        name="Litecoin",
        version=65796,
        display_name="Litecoin",
        icon="litecoin",
        hash="cdbbf26c69a4f4ce84b0ae6a8426b2cb80ba724c3eb42a20673f07fcc810eecf",
        perso="perso_11",
        firmware="nanos/1.3/litecoin/st31_litecoin_1.1.4",
        firmware_key="nanos/1.3/litecoin/st31_litecoin_1.1.4_key",
        delete="nanos/1.3/litecoin/st31_litecoin_del",
        delete_key="nanos/1.3/litecoin/st31_litecoin_del_key",
        app=app18
    )
    appVer143.providers.add(provider1)
    appVer143.device_versions.add(device_ver1)
    appVer143.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer144 = ApplicationVersion.objects.create(
        name="Stratis",
        version=65796,
        display_name="Stratis",
        icon="stratis",
        hash="f985829680ab4e27c201cfe862db7fa821b33c0684b766e1e46a633248fe554b",
        perso="perso_11",
        firmware="nanos/1.3/stratis/st31_stratis_1.1.4",
        firmware_key="nanos/1.3/stratis/st31_stratis_1.1.4_key",
        delete="nanos/1.3/stratis/st31_stratis_del",
        delete_key="nanos/1.3/stratis/st31_stratis_del_key",
        app=app19
    )
    appVer144.providers.add(provider1)
    appVer144.device_versions.add(device_ver1)
    appVer144.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer145 = ApplicationVersion.objects.create(
        name="Zcash",
        version=65796,
        display_name="Zcash",
        icon="zcash",
        hash="0a6cd53a2d737abf47c74747167526699cfd80f7c2a27ba47c9265fc8f5e06ce",
        perso="perso_11",
        firmware="nanos/1.3/zcash/st31_zcash_1.1.4",
        firmware_key="nanos/1.3/zcash/st31_zcash_1.1.4_key",
        delete="nanos/1.3/zcash/st31_zcash_del",
        delete_key="nanos/1.3/zcash/st31_zcash_del_key",
        app=app21
    )
    appVer145.providers.add(provider1)
    appVer145.device_versions.add(device_ver1)
    appVer145.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer146 = ApplicationVersion.objects.create(
        name="SSH/GPG Agent",
        version=2,
        display_name="SSH/GPG Agent",
        icon="ssh",
        hash="818fa91da1c658b47f0d6c7da6f8e7523d8b9ad1706ed3e9bbec9b87a6eb5fce",
        perso="perso_11",
        firmware="nanos/1.3/sshgpg/st31_gpg_0.0.2",
        firmware_key="nanos/1.3/sshgpg/st31_gpg_0.0.2_key",
        delete="nanos/1.3/sshgpg/st31_gpg_del",
        delete_key="nanos/1.3/sshgpg/st31_gpg_del_key",
        app=app28
    )
    appVer146.providers.add(provider1)
    appVer146.device_versions.add(device_ver1)
    appVer146.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer147 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=65795,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="bbde9da7af3b82676af2ddaacb58e284f077c0a3d9e671e7373575deab08089e",
        perso="perso_11",
        firmware="nanos/1.2/bitcoin/st31_bitcoin_1.1.3",
        firmware_key="nanos/1.2/bitcoin/st31_bitcoin_1.1.3_key",
        delete="nanos/1.2/bitcoin/st31_bitcoin_del",
        delete_key="nanos/1.2/bitcoin/st31_bitcoin_del_key",
        app=app0
    )
    appVer147.providers.add(provider1)
    appVer147.device_versions.add(device_ver1)
    appVer147.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer148 = ApplicationVersion.objects.create(
        name="Bitcoin Beta",
        version=65794,
        display_name="Bitcoin Beta",
        icon="bitcoin",
        hash="undefined",
        perso="perso_11",
        firmware="nanos_12/st31_btc_112",
        firmware_key="nanos_12/st31_btc_112_key",
        delete="undefined",
        delete_key="undefined",
        app=app40
    )
    appVer148.providers.add(provider1)
    appVer148.device_versions.add(device_ver1)
    appVer148.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer149 = ApplicationVersion.objects.create(
        name="Dash",
        version=65795,
        display_name="Dash",
        icon="dash",
        hash="7ab683d791b09f81ccc7b4e9a3a7d5ec2bb1a91d3baccd61794d5a9b55282283",
        perso="perso_11",
        firmware="nanos/1.2/dash/st31_dash_1.1.3",
        firmware_key="nanos/1.2/dash/st31_dash_1.1.3_key",
        delete="nanos/1.2/dash/st31_dash_del",
        delete_key="nanos/1.2/dash/st31_dash_del_key",
        app=app14
    )
    appVer149.providers.add(provider1)
    appVer149.device_versions.add(device_ver1)
    appVer149.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer150 = ApplicationVersion.objects.create(
        name="Dogecoin",
        version=65795,
        display_name="Dogecoin",
        icon="dogecoin",
        hash="228a3ac0ba170b3220f169949a8f315593dc02a41c00077ca4d21aa4a9e7c565",
        perso="perso_11",
        firmware="nanos/1.2/dogecoin/st31_dogecoin_1.1.3",
        firmware_key="nanos/1.2/dogecoin/st31_dogecoin_1.1.3_key",
        delete="nanos/1.2/dogecoin/st31_dogecoin_del",
        delete_key="nanos/1.2/dogecoin/st31_dogecoin_del_key",
        app=app15
    )
    appVer150.providers.add(provider1)
    appVer150.device_versions.add(device_ver1)
    appVer150.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer151 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65541,
        display_name="Ethereum",
        icon="ethereum",
        hash="6a9c2ed9159085f89e9396da7a60c78e0b7dce9c946d3f5d78a415a3ea3063b9",
        perso="perso_11",
        firmware="nanos/1.2/ethereum/st31_etc_1.0.5",
        firmware_key="nanos/1.2/ethereum/st31_etc_1.0.5_key",
        delete="nanos/1.2/ethereum/st31_etc_del",
        delete_key="nanos/1.2/ethereum/st31_etc_del_key",
        app=app16
    )
    appVer151.providers.add(provider1)
    appVer151.device_versions.add(device_ver1)
    appVer151.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer152 = ApplicationVersion.objects.create(
        name="Fido U2F",
        version=65792,
        display_name="Fido U2F",
        icon="fido",
        hash="f60dd45356506a636c68f457ade1743285ab2981d1a626f70b0d9127636ce859",
        perso="perso_11",
        firmware="nanos/1.2/fido_u2f/st31_fido_u2f_1.1.0",
        firmware_key="nanos/1.2/fido_u2f/st31_fido_u2f_1.1.0_key",
        delete="nanos/1.2/fido_u2f/st31_fido_u2f_del",
        delete_key="nanos/1.2/fido_u2f/st31_fido_u2f_del_key",
        app=app17
    )
    appVer152.providers.add(provider1)
    appVer152.device_versions.add(device_ver1)
    appVer152.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer153 = ApplicationVersion.objects.create(
        name="Litecoin",
        version=65795,
        display_name="Litecoin",
        icon="litecoin",
        hash="95e2f6151cfe8fca53affabdf8bf710fc40465fe54954d79736f39c425dade30",
        perso="perso_11",
        firmware="nanos/1.2/litecoin/st31_litecoin_1.1.3",
        firmware_key="nanos/1.2/litecoin/st31_litecoin_1.1.3_key",
        delete="nanos/1.2/litecoin/st31_litecoin_del",
        delete_key="nanos/1.2/litecoin/st31_litecoin_del_key",
        app=app18
    )
    appVer153.providers.add(provider1)
    appVer153.device_versions.add(device_ver1)
    appVer153.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer154 = ApplicationVersion.objects.create(
        name="SSH/GPG Agent",
        version=1,
        display_name="SSH/GPG Agent",
        icon="ssh",
        hash="undefined",
        perso="perso_11",
        firmware="nanos_12/st31_gpg",
        firmware_key="nanos_12/st31_gpg_key",
        delete="undefined",
        delete_key="undefined",
        app=app28
    )
    appVer154.providers.add(provider1)
    appVer154.device_versions.add(device_ver1)
    appVer154.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer155 = ApplicationVersion.objects.create(
        name="Stratis",
        version=65795,
        display_name="Stratis",
        icon="stratis",
        hash="c522f288c7b7417b1559b52cf019d9eca6e1d3036ef9180fb3f2cecaa974f2f0",
        perso="perso_11",
        firmware="nanos/1.2/stratis/st31_stratis_1.1.3",
        firmware_key="nanos/1.2/stratis/st31_stratis_1.1.3_key",
        delete="nanos/1.2/stratis/st31_stratis_del",
        delete_key="nanos/1.2/stratis/st31_stratis_del_key",
        app=app19
    )
    appVer155.providers.add(provider1)
    appVer155.device_versions.add(device_ver1)
    appVer155.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer156 = ApplicationVersion.objects.create(
        name="Zcash",
        version=65795,
        display_name="Zcash",
        icon="zcash",
        hash="2d12214b922fae80654f57ecf132eaa7d686b0ee42135089c3acc275e2343838",
        perso="perso_11",
        firmware="nanos/1.2/zcash/st31_zcash_1.1.3",
        firmware_key="nanos/1.2/zcash/st31_zcash_1.1.3_key",
        delete="nanos/1.2/zcash/st31_zcash_del",
        delete_key="nanos/1.2/zcash/st31_zcash_del_key",
        app=app21
    )
    appVer156.providers.add(provider1)
    appVer156.device_versions.add(device_ver1)
    appVer156.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer157 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=65536,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="15be34a21090e22203d0de1f827867eedda4a9be85b393dc7086b73e75d4a58c",
        perso="perso_11",
        firmware="st31_btc",
        firmware_key="st31_btc_key",
        delete="undefined",
        delete_key="undefined",
        app=app0
    )
    appVer157.providers.add(provider1)
    appVer157.device_versions.add(device_ver1)
    appVer157.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer158 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65536,
        display_name="Ethereum",
        icon="ethereum",
        hash="6b8d252262ed7568784c30e1f816681d595b5f0c173e6670415aa8b5043ef7c5",
        perso="perso_11",
        firmware="st31_etc",
        firmware_key="st31_etc_key",
        delete="undefined",
        delete_key="undefined",
        app=app16
    )
    appVer158.providers.add(provider1)
    appVer158.device_versions.add(device_ver1)
    appVer158.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer159 = ApplicationVersion.objects.create(
        name="Fido U2F",
        version=65536,
        display_name="Fido U2F",
        icon="fido",
        hash="cb0a184f635859d5d54e21aa57878627c7880903cfb53b91450d8fc89f8c3693",
        perso="perso_11",
        firmware="st31_fido_u2f",
        firmware_key="st31_fido_u2f_key",
        delete="undefined",
        delete_key="undefined",
        app=app17
    )
    appVer159.providers.add(provider1)
    appVer159.device_versions.add(device_ver1)
    appVer159.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer160 = ApplicationVersion.objects.create(
        name="Litecoin",
        version=65536,
        display_name="Litecoin",
        icon="litecoin",
        hash="fa5a37103b9fe5049fbf6ceb2fe424cd90cc3770d34720df0393e3a958a5ebc2",
        perso="perso_11",
        firmware="st31_ltc",
        firmware_key="st31_ltc_key",
        delete="undefined",
        delete_key="undefined",
        app=app18
    )
    appVer160.providers.add(provider1)
    appVer160.device_versions.add(device_ver1)
    appVer160.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer161 = ApplicationVersion.objects.create(
        name="SSH/GPG Agent",
        version=1,
        display_name="SSH/GPG Agent",
        icon="ssh",
        hash="0cd8553b3a7d1341ad4d9dda8f7f9b380dcc473a0f6c1db1c1acc66180106311",
        perso="perso_11",
        firmware="st31_gpg",
        firmware_key="st31_gpg_key",
        delete="undefined",
        delete_key="undefined",
        app=app28
    )
    appVer161.providers.add(provider1)
    appVer161.device_versions.add(device_ver1)
    appVer161.se_firmware_final_versions.add(firmware_final_ver1)
