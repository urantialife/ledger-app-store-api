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
    device_ver6 = DeviceVersion.objects.create(
        name="blue_2hw10",
        target_id=822083588,
        device=device2
    )
    device_ver6.providers.add(provider1)
    device_ver7 = DeviceVersion.objects.create(
        name="blue_2hw15",
        target_id=822149124,
        device=device2
    )
    device_ver7.providers.add(provider1)

    print("Devices created")

    # FIRMWARE CREATION
    firmware0 = SeFirmware.objects.create(name="Ledger blue firmware")
    firmware0.providers.add(provider1)
    firmware = SeFirmware.objects.create(name="Ledger nano S firmware")
    firmware.providers.add(provider1)
    firmware2 = SeFirmware.objects.create(name="DAS firmware")
    firmware2.providers.add(provider2)
    firmware3 = SeFirmware.objects.create(name="Bitclub firmware")
    firmware3.providers.add(provider3)

    # FIRMWARE FINAL CREATION
    # BLUE
    firmware_final_ver0 = SeFirmwareFinalVersion.objects.create(
        name="2.0.1",
        version=int.from_bytes(bytes([0, 2, 0, 1]), 'big'),
        perso="perso_11",
        firmware="",
        firmware_key="",
        hash="",
        se_firmware=firmware0
    )
    firmware_final_ver0.device_versions.add(device_ver2)
    firmware_final_ver0.providers.add(provider1)

    firmware_final_ver8 = SeFirmwareFinalVersion.objects.create(
        name="2.0.0",
        version=int.from_bytes(bytes([0, 2, 0, 0]), 'big'),
        perso="perso_11",
        firmware="",
        firmware_key="",
        hash="",
        se_firmware=firmware0
    )
    firmware_final_ver8.device_versions.add(device_ver2)
    firmware_final_ver8.providers.add(provider1)

    firmware_final_ver9 = SeFirmwareFinalVersion.objects.create(
        name="2.1.1",
        version=int.from_bytes(bytes([0, 2, 1, 1]), 'big'),
        perso="perso_11",
        firmware="blue/2.1.1/from_2.0-hw10/upgrade_2.1.1",
        firmware_key="blue/2.1.1/from_2.0-hw10/upgrade_2.1.1_key",
        hash="60fe0168a775ab96093a012b08a50df42980ed2a5696aeb764e906677c9d6151",
        se_firmware=firmware0
    )
    firmware_final_ver9.device_versions.add(device_ver6)
    firmware_final_ver9.providers.add(provider1)

    firmware_final_ver10 = SeFirmwareFinalVersion.objects.create(
        name="2.1.1",
        version=int.from_bytes(bytes([0, 2, 1, 1]), 'big'),
        perso="perso_11",
        firmware="blue/2.1.1/from_2.0.1ngs-hw15/upgrade_2.1.1",
        firmware_key="blue/2.1.1/from_2.0.1ngs-hw15/upgrade_2.1.1_key",
        hash="54bbdadac9e6ef8e6c502f159777307ff1e23b7d042a2a82d9d8a386d6883c9c",
        se_firmware=firmware0
    )
    firmware_final_ver10.device_versions.add(device_ver7)
    firmware_final_ver10.providers.add(provider1)

    firmware_final_ver11 = SeFirmwareFinalVersion.objects.create(
        name="2.1.0",
        version=int.from_bytes(bytes([0, 2, 1, 0]), 'big'),
        perso="perso_11",
        firmware="",
        firmware_key="",
        hash="",
        se_firmware=firmware0
    )
    firmware_final_ver11.device_versions.add(device_ver6)
    firmware_final_ver11.providers.add(provider1)

    firmware_final_ver12 = SeFirmwareFinalVersion.objects.create(
        name="2.1.0",
        version=int.from_bytes(bytes([0, 2, 1, 0]), 'big'),
        perso="perso_11",
        firmware="",
        firmware_key="",
        hash="",
        se_firmware=firmware0
    )
    firmware_final_ver12.device_versions.add(device_ver7)
    firmware_final_ver12.providers.add(provider1)

    # NANO S
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

    firmware_final_ver1_2 = SeFirmwareFinalVersion.objects.create(
        name="1.2.0",
        version=int.from_bytes(bytes([0, 1, 2, 0]), 'big'),
        perso="perso_11",
        firmware="",
        firmware_key="",
        hash="",
        se_firmware=firmware
    )
    firmware_final_ver1_2.device_versions.add(device_ver1)
    firmware_final_ver1_2.providers.add(provider1)

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

    print("Firmwares created")
    # MCU CREATION
    mcu = Mcu.objects.create(name="Ledger")

    mcu10 = McuVersion.objects.create(
        name="1.0",
        mcu=mcu,
        from_bootloader_version=""
    )
    mcu10.device_versions.add(device_ver1, device_ver0)
    mcu10.se_firmware_final_versions.add(
        firmware_final_ver1, firmware_final_ver5, firmware_final_ver6, firmware_final_ver7, firmware_final_ver8)

    mcu11 = McuVersion.objects.create(
        name="1.1",
        mcu=mcu,
        from_bootloader_version=""
    )
    mcu11.device_versions.add(device_ver1, device_ver0)
    mcu11.se_firmware_final_versions.add(
        firmware_final_ver1, firmware_final_ver5, firmware_final_ver6, firmware_final_ver7, firmware_final_ver8)

    mcu15 = McuVersion.objects.create(
        name="1.5",
        mcu=mcu,
        from_bootloader_version="0.6.0"
    )
    mcu15.device_versions.add(device_ver5)
    mcu15.se_firmware_final_versions.add(
        firmware_final_ver3, firmware_final_ver4)

    mcu06 = McuVersion.objects.create(
        name="0.6",
        mcu=mcu,
        from_bootloader_version="0.0.0"
    )
    print("MCU created")

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
    print("OSU created")

    # CATEGORY
    cat1 = Category.objects.create(name="Currencies")
    cat2 = Category.objects.create(name="Developer tools")

    # APP CREATION
    app0 = Application.objects.create(name="Bitcoin", category=cat1)
    app0.providers.add(provider2, provider3, provider1)
    app1 = Application.objects.create(name="Bitcoin Cash", category=cat1)
    app1.providers.add(provider2, provider1)
    app2 = Application.objects.create(name="Bitcoin Gold", category=cat1)
    app2.providers.add(provider1)
    app3 = Application.objects.create(name="Bitcoin Private", category=cat1)
    app3.providers.add(provider1)
    app4 = Application.objects.create(name="Bitcoin testnet", category=cat2)
    app4.providers.add(provider1)
    app5 = Application.objects.create(name="Digibyte", category=cat1)
    app5.providers.add(provider1)
    app6 = Application.objects.create(name="HCash", category=cat1)
    app6.providers.add(provider1)
    app7 = Application.objects.create(name="Qtum", category=cat1)
    app7.providers.add(provider1)
    app8 = Application.objects.create(name="PIVX", category=cat1)
    app8.providers.add(provider1)
    app9 = Application.objects.create(name="Stealth", category=cat1)
    app9.providers.add(provider1)
    app10 = Application.objects.create(name="Vertcoin", category=cat1)
    app10.providers.add(provider1)
    app11 = Application.objects.create(name="Peercoin", category=cat1)
    app11.providers.add(provider1)
    app12 = Application.objects.create(name="Viacoin", category=cat1)
    app12.providers.add(provider1)
    app13 = Application.objects.create(name="Ubiq", category=cat1)
    app13.providers.add(provider1)
    app14 = Application.objects.create(name="Expanse", category=cat1)
    app14.providers.add(provider1)
    app15 = Application.objects.create(name="Dash", category=cat1)
    app15.providers.add(provider1)
    app16 = Application.objects.create(name="Dogecoin", category=cat1)
    app16.providers.add(provider1)
    app17 = Application.objects.create(name="Ethereum", category=cat1)
    app17.providers.add(provider2, provider3, provider1)
    app18 = Application.objects.create(name="Fido U2F")
    app18.providers.add(provider3, provider1)
    app19 = Application.objects.create(name="Litecoin", category=cat1)
    app19.providers.add(provider1)
    app20 = Application.objects.create(name="Stratis", category=cat1)
    app20.providers.add(provider1)
    app21 = Application.objects.create(name="Ripple", category=cat1)
    app21.providers.add(provider2, provider1)
    app22 = Application.objects.create(name="Zcash", category=cat1)
    app22.providers.add(provider3, provider1)
    app23 = Application.objects.create(name="ZenCash", category=cat1)
    app23.providers.add(provider1)
    app24 = Application.objects.create(name="Komodo", category=cat1)
    app24.providers.add(provider1)
    app25 = Application.objects.create(name="PoSW", category=cat1)
    app25.providers.add(provider1)
    app26 = Application.objects.create(name="Stellar", category=cat1)
    app26.providers.add(provider1)
    app27 = Application.objects.create(name="Stealthcoin", category=cat1)
    app27.providers.add(provider1)
    app28 = Application.objects.create(name="Neo", category=cat1)
    app28.providers.add(provider1)
    app29 = Application.objects.create(name="SSH/PGP Agent", category=cat2)
    app29.providers.add(provider1)
    app30 = Application.objects.create(name="Passwords Manager", category=cat2)
    app30.providers.add(provider1)
    app31 = Application.objects.create(name="Open PGP", category=cat2)
    app31.providers.add(provider1)
    app32 = Application.objects.create(name="Hello")
    app32.providers.add(provider1)
    app33 = Application.objects.create(name="Ark", category=cat1)
    app33.providers.add(provider1)
    app34 = Application.objects.create(name="Clubcoin", category=cat1)
    app34.providers.add(provider3)
    app35 = Application.objects.create(name="DasCoin", category=cat1)
    app35.providers.add(provider2)
    app36 = Application.objects.create(name="Bitcoin Beta", category=cat2)
    app36.providers.add(provider1)
    app37 = Application.objects.create(name="SSH/GPG Agent", category=cat2)
    app37.providers.add(provider1)
    app38 = Application.objects.create(name="Woleet", category=cat1)
    app38.providers.add(provider1)
    app39 = Application.objects.create(name="Monero", category=cat2)
    app39.providers.add(provider1)
    app40 = Application.objects.create(name="Nano", category=cat1)
    app40.providers.add(provider1)
    app41 = Application.objects.create(name="Nimiq", category=cat1)
    app41.providers.add(provider1)
    app42 = Application.objects.create(name="Tezos Baking", category=cat2)
    app42.providers.add(provider1)
    app43 = Application.objects.create(name="Tezos Wallet", category=cat2)
    app43.providers.add(provider1)
    app44 = Application.objects.create(name="Tron", category=cat1)
    app44.providers.add(provider1)
    app45 = Application.objects.create(name="Zcoin", category=cat1)
    app45.providers.add(provider1)
    app46 = Application.objects.create(name="Dascoin", category=cat1)
    app46.providers.add(provider2)
    # blue_2hw15 ,
    appVer1 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=66055,
        display_name="Bitcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/bitcoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/bitcoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/bitcoin/app_del",
        delete_key="blue/2.1.0-hw15/bitcoin/app_del_key",
        app=app0
    )
    appVer1.providers.add(provider1)
    appVer1.device_versions.add(device_ver7)
    appVer1.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer2 = ApplicationVersion.objects.create(
        name="Bitcoin Cash",
        version=66055,
        display_name="Bitcoin Cash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/bitcoin_cash/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/bitcoin_cash/app_1.2.7_key",
        delete="blue/2.1.0-hw15/bitcoin_cash/app_del",
        delete_key="blue/2.1.0-hw15/bitcoin_cash/app_del_key",
        app=app1
    )
    appVer2.providers.add(provider1)
    appVer2.device_versions.add(device_ver7)
    appVer2.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer3 = ApplicationVersion.objects.create(
        name="Bitcoin Gold",
        version=66055,
        display_name="Bitcoin Gold",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/bitcoin_gold/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/bitcoin_gold/app_1.2.7_key",
        delete="blue/2.1.0-hw15/bitcoin_gold/app_del",
        delete_key="blue/2.1.0-hw15/bitcoin_gold/app_del_key",
        app=app2
    )
    appVer3.providers.add(provider1)
    appVer3.device_versions.add(device_ver7)
    appVer3.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer4 = ApplicationVersion.objects.create(
        name="Bitcoin Private",
        version=66055,
        display_name="Bitcoin Private",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/bitcoin_private/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/bitcoin_private/app_1.2.7_key",
        delete="blue/2.1.0-hw15/bitcoin_private/app_del",
        delete_key="blue/2.1.0-hw15/bitcoin_private/app_del_key",
        app=app3
    )
    appVer4.providers.add(provider1)
    appVer4.device_versions.add(device_ver7)
    appVer4.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer5 = ApplicationVersion.objects.create(
        name="Bitcoin testnet",
        version=66055,
        display_name="Bitcoin testnet",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/bitcoin_testnet/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/bitcoin_testnet/app_1.2.7_key",
        delete="blue/2.1.0-hw15/bitcoin_testnet/app_del",
        delete_key="blue/2.1.0-hw15/bitcoin_testnet/app_del_key",
        app=app4
    )
    appVer5.providers.add(provider1)
    appVer5.device_versions.add(device_ver7)
    appVer5.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer6 = ApplicationVersion.objects.create(
        name="Digibyte",
        version=66055,
        display_name="Digibyte",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/digibyte/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/digibyte/app_1.2.7_key",
        delete="blue/2.1.0-hw15/digibyte/app_del",
        delete_key="blue/2.1.0-hw15/digibyte/app_del_key",
        app=app5
    )
    appVer6.providers.add(provider1)
    appVer6.device_versions.add(device_ver7)
    appVer6.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer7 = ApplicationVersion.objects.create(
        name="HCash",
        version=66055,
        display_name="HCash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/hcash/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/hcash/app_1.2.7_key",
        delete="blue/2.1.0-hw15/hcash/app_del",
        delete_key="blue/2.1.0-hw15/hcash/app_del_key",
        app=app6
    )
    appVer7.providers.add(provider1)
    appVer7.device_versions.add(device_ver7)
    appVer7.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer8 = ApplicationVersion.objects.create(
        name="Qtum",
        version=66055,
        display_name="Qtum",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/qtum/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/qtum/app_1.2.7_key",
        delete="blue/2.1.0-hw15/qtum/app_del",
        delete_key="blue/2.1.0-hw15/qtum/app_del_key",
        app=app7
    )
    appVer8.providers.add(provider1)
    appVer8.device_versions.add(device_ver7)
    appVer8.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer9 = ApplicationVersion.objects.create(
        name="PIVX",
        version=66055,
        display_name="PIVX",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/pivx/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/pivx/app_1.2.7_key",
        delete="blue/2.1.0-hw15/pivx/app_del",
        delete_key="blue/2.1.0-hw15/pivx/app_del_key",
        app=app8
    )
    appVer9.providers.add(provider1)
    appVer9.device_versions.add(device_ver7)
    appVer9.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer10 = ApplicationVersion.objects.create(
        name="Stealth",
        version=66055,
        display_name="Stealth",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/stealthcoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/stealthcoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/stealthcoin/app_del",
        delete_key="blue/2.1.0-hw15/stealthcoin/app_del_key",
        app=app9
    )
    appVer10.providers.add(provider1)
    appVer10.device_versions.add(device_ver7)
    appVer10.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer11 = ApplicationVersion.objects.create(
        name="Vertcoin",
        version=66055,
        display_name="Vertcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/vertcoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/vertcoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/vertcoin/app_del",
        delete_key="blue/2.1.0-hw15/vertcoin/app_del_key",
        app=app10
    )
    appVer11.providers.add(provider1)
    appVer11.device_versions.add(device_ver7)
    appVer11.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer12 = ApplicationVersion.objects.create(
        name="Peercoin",
        version=66055,
        display_name="Peercoin",
        icon="peercoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/peercoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/peercoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/peercoin/app_del",
        delete_key="blue/2.1.0-hw15/peercoin/app_del_key",
        app=app11
    )
    appVer12.providers.add(provider1)
    appVer12.device_versions.add(device_ver7)
    appVer12.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer13 = ApplicationVersion.objects.create(
        name="Viacoin",
        version=66055,
        display_name="Viacoin",
        icon="viacoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/viacoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/viacoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/viacoin/app_del",
        delete_key="blue/2.1.0-hw15/viacoin/app_del_key",
        app=app12
    )
    appVer13.providers.add(provider1)
    appVer13.device_versions.add(device_ver7)
    appVer13.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer14 = ApplicationVersion.objects.create(
        name="Ubiq",
        version=65793,
        display_name="Ubiq",
        icon="ubiq",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/ubiq/app_1.1.1",
        firmware_key="blue/2.1.0-hw15/ubiq/app_1.1.1_key",
        delete="blue/2.1.0-hw15/ubiq/app_del",
        delete_key="blue/2.1.0-hw15/ubiq/app_del_key",
        app=app13
    )
    appVer14.providers.add(provider1)
    appVer14.device_versions.add(device_ver7)
    appVer14.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer15 = ApplicationVersion.objects.create(
        name="Expanse",
        version=65793,
        display_name="Expanse",
        icon="expanse",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/expanse/app_1.1.1",
        firmware_key="blue/2.1.0-hw15/expanse/app_1.1.1_key",
        delete="blue/2.1.0-hw15/expanse/app_del",
        delete_key="blue/2.1.0-hw15/expanse/app_del_key",
        app=app14
    )
    appVer15.providers.add(provider1)
    appVer15.device_versions.add(device_ver7)
    appVer15.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer16 = ApplicationVersion.objects.create(
        name="Dash",
        version=66055,
        display_name="Dash",
        icon="dash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/dash/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/dash/app_1.2.7_key",
        delete="blue/2.1.0-hw15/dash/app_del",
        delete_key="blue/2.1.0-hw15/dash/app_del_key",
        app=app15
    )
    appVer16.providers.add(provider1)
    appVer16.device_versions.add(device_ver7)
    appVer16.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer17 = ApplicationVersion.objects.create(
        name="Dogecoin",
        version=66055,
        display_name="Dogecoin",
        icon="dogecoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/dogecoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/dogecoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/dogecoin/app_del",
        delete_key="blue/2.1.0-hw15/dogecoin/app_del_key",
        app=app16
    )
    appVer17.providers.add(provider1)
    appVer17.device_versions.add(device_ver7)
    appVer17.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer18 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65793,
        display_name="Ethereum",
        icon="ethereum",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/ethereum/app_1.1.1",
        firmware_key="blue/2.1.0-hw15/ethereum/app_1.1.1_key",
        delete="blue/2.1.0-hw15/ethereum/app_del",
        delete_key="blue/2.1.0-hw15/ethereum/app_del_key",
        app=app17
    )
    appVer18.providers.add(provider1)
    appVer18.device_versions.add(device_ver7)
    appVer18.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer19 = ApplicationVersion.objects.create(
        name="Fido U2F",
        version=66053,
        display_name="Fido U2F",
        icon="fido",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/u2f/app_1.2.5",
        firmware_key="blue/2.1.0-hw15/u2f/app_1.2.5_key",
        delete="blue/2.1.0-hw15/u2f/app_del",
        delete_key="blue/2.1.0-hw15/u2f/app_del_key",
        app=app18
    )
    appVer19.providers.add(provider1)
    appVer19.device_versions.add(device_ver7)
    appVer19.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer20 = ApplicationVersion.objects.create(
        name="Litecoin",
        version=66055,
        display_name="Litecoin",
        icon="litecoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/litecoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/litecoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/litecoin/app_del",
        delete_key="blue/2.1.0-hw15/litecoin/app_del_key",
        app=app19
    )
    appVer20.providers.add(provider1)
    appVer20.device_versions.add(device_ver7)
    appVer20.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer21 = ApplicationVersion.objects.create(
        name="Stratis",
        version=66055,
        display_name="Stratis",
        icon="stratis",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/stratis/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/stratis/app_1.2.7_key",
        delete="blue/2.1.0-hw15/stratis/app_del",
        delete_key="blue/2.1.0-hw15/stratis/app_del_key",
        app=app20
    )
    appVer21.providers.add(provider1)
    appVer21.device_versions.add(device_ver7)
    appVer21.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer22 = ApplicationVersion.objects.create(
        name="Ripple",
        version=65541,
        display_name="Ripple",
        icon="ripple",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/ripple/app_1.0.5",
        firmware_key="blue/2.1.0-hw15/ripple/app_1.0.5_key",
        delete="blue/2.1.0-hw15/ripple/app_del",
        delete_key="blue/2.1.0-hw15/ripple/app_del_key",
        app=app21
    )
    appVer22.providers.add(provider1)
    appVer22.device_versions.add(device_ver7)
    appVer22.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer23 = ApplicationVersion.objects.create(
        name="Zcash",
        version=66052,
        display_name="Zcash",
        icon="zcash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/zcash/app_1.2.4",
        firmware_key="blue/2.1.0-hw15/zcash/app_1.2.4_key",
        delete="blue/2.1.0-hw15/zcash/app_del",
        delete_key="blue/2.1.0-hw15/zcash/app_del_key",
        app=app22
    )
    appVer23.providers.add(provider1)
    appVer23.device_versions.add(device_ver7)
    appVer23.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer24 = ApplicationVersion.objects.create(
        name="ZenCash",
        version=66052,
        display_name="ZenCash",
        icon="zencash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/zencash/app_1.2.4",
        firmware_key="blue/2.1.0-hw15/zencash/app_1.2.4_key",
        delete="blue/2.1.0-hw15/zencash/app_del",
        delete_key="blue/2.1.0-hw15/zencash/app_del_key",
        app=app23
    )
    appVer24.providers.add(provider1)
    appVer24.device_versions.add(device_ver7)
    appVer24.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer25 = ApplicationVersion.objects.create(
        name="Komodo",
        version=66055,
        display_name="Komodo",
        icon="komodo",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/komodo/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/komodo/app_1.2.7_key",
        delete="blue/2.1.0-hw15/komodo/app_del",
        delete_key="blue/2.1.0-hw15/komodo/app_del_key",
        app=app24
    )
    appVer25.providers.add(provider1)
    appVer25.device_versions.add(device_ver7)
    appVer25.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer26 = ApplicationVersion.objects.create(
        name="PoSW",
        version=66055,
        display_name="PoSW",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/posw/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/posw/app_1.2.7_key",
        delete="blue/2.1.0-hw15/posw/app_del",
        delete_key="blue/2.1.0-hw15/posw/app_del_key",
        app=app25
    )
    appVer26.providers.add(provider1)
    appVer26.device_versions.add(device_ver7)
    appVer26.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw15 ,
    appVer27 = ApplicationVersion.objects.create(
        name="Stellar",
        version=196608,
        display_name="Stellar",
        icon="stellar",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/stellar/app_3.0.0",
        firmware_key="blue/2.1.0-hw15/stellar/app_3.0.0_key",
        delete="blue/2.1.0-hw15/stellar/app_del",
        delete_key="blue/2.1.0-hw15/stellar/app_del_key",
        app=app26
    )
    appVer27.providers.add(provider1)
    appVer27.device_versions.add(device_ver7)
    appVer27.se_firmware_final_versions.add(
        firmware_final_ver10, firmware_final_ver12)
    # blue_2hw10 ,
    appVer28 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=66055,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/bitcoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/bitcoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/bitcoin/app_del",
        delete_key="blue/2.1.0-hw15/bitcoin/app_del_key",
        app=app0
    )
    appVer28.providers.add(provider1)
    appVer28.device_versions.add(device_ver6)
    appVer28.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer29 = ApplicationVersion.objects.create(
        name="Bitcoin Cash",
        version=66055,
        display_name="Bitcoin Cash",
        icon="bitcoin_cash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/bitcoin_cash/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/bitcoin_cash/app_1.2.7_key",
        delete="blue/2.1.0-hw15/bitcoin_cash/app_del",
        delete_key="blue/2.1.0-hw15/bitcoin_cash/app_del_key",
        app=app1
    )
    appVer29.providers.add(provider1)
    appVer29.device_versions.add(device_ver6)
    appVer29.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer30 = ApplicationVersion.objects.create(
        name="Bitcoin Gold",
        version=66055,
        display_name="Bitcoin Gold",
        icon="bitcoin_gold",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/bitcoin_gold/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/bitcoin_gold/app_1.2.7_key",
        delete="blue/2.1.0-hw15/bitcoin_gold/app_del",
        delete_key="blue/2.1.0-hw15/bitcoin_gold/app_del_key",
        app=app2
    )
    appVer30.providers.add(provider1)
    appVer30.device_versions.add(device_ver6)
    appVer30.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer31 = ApplicationVersion.objects.create(
        name="Bitcoin Private",
        version=66055,
        display_name="Bitcoin Private",
        icon="bitcoin_private",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/bitcoin_private/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/bitcoin_private/app_1.2.7_key",
        delete="blue/2.1.0-hw15/bitcoin_private/app_del",
        delete_key="blue/2.1.0-hw15/bitcoin_private/app_del_key",
        app=app3
    )
    appVer31.providers.add(provider1)
    appVer31.device_versions.add(device_ver6)
    appVer31.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer32 = ApplicationVersion.objects.create(
        name="Bitcoin testnet",
        version=66055,
        display_name="Bitcoin testnet",
        icon="bitcoin_testnet",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/bitcoin_testnet/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/bitcoin_testnet/app_1.2.7_key",
        delete="blue/2.1.0-hw15/bitcoin_testnet/app_del",
        delete_key="blue/2.1.0-hw15/bitcoin_testnet/app_del_key",
        app=app4
    )
    appVer32.providers.add(provider1)
    appVer32.device_versions.add(device_ver6)
    appVer32.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer33 = ApplicationVersion.objects.create(
        name="Digibyte",
        version=66055,
        display_name="Digibyte",
        icon="digibyte",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/digibyte/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/digibyte/app_1.2.7_key",
        delete="blue/2.1.0-hw15/digibyte/app_del",
        delete_key="blue/2.1.0-hw15/digibyte/app_del_key",
        app=app5
    )
    appVer33.providers.add(provider1)
    appVer33.device_versions.add(device_ver6)
    appVer33.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer34 = ApplicationVersion.objects.create(
        name="HCash",
        version=66055,
        display_name="HCash",
        icon="hcash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/hcash/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/hcash/app_1.2.7_key",
        delete="blue/2.1.0-hw15/hcash/app_del",
        delete_key="blue/2.1.0-hw15/hcash/app_del_key",
        app=app6
    )
    appVer34.providers.add(provider1)
    appVer34.device_versions.add(device_ver6)
    appVer34.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer35 = ApplicationVersion.objects.create(
        name="Qtum",
        version=66055,
        display_name="Qtum",
        icon="qtum",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/qtum/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/qtum/app_1.2.7_key",
        delete="blue/2.1.0-hw15/qtum/app_del",
        delete_key="blue/2.1.0-hw15/qtum/app_del_key",
        app=app7
    )
    appVer35.providers.add(provider1)
    appVer35.device_versions.add(device_ver6)
    appVer35.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer36 = ApplicationVersion.objects.create(
        name="PIVX",
        version=66055,
        display_name="PIVX",
        icon="pivx",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/pivx/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/pivx/app_1.2.7_key",
        delete="blue/2.1.0-hw15/pivx/app_del",
        delete_key="blue/2.1.0-hw15/pivx/app_del_key",
        app=app8
    )
    appVer36.providers.add(provider1)
    appVer36.device_versions.add(device_ver6)
    appVer36.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer37 = ApplicationVersion.objects.create(
        name="Stealth",
        version=66055,
        display_name="Stealth",
        icon="stealthcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/stealthcoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/stealthcoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/stealthcoin/app_del",
        delete_key="blue/2.1.0-hw15/stealthcoin/app_del_key",
        app=app9
    )
    appVer37.providers.add(provider1)
    appVer37.device_versions.add(device_ver6)
    appVer37.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer38 = ApplicationVersion.objects.create(
        name="Vertcoin",
        version=66055,
        display_name="Vertcoin",
        icon="vertcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/vertcoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/vertcoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/vertcoin/app_del",
        delete_key="blue/2.1.0-hw15/vertcoin/app_del_key",
        app=app10
    )
    appVer38.providers.add(provider1)
    appVer38.device_versions.add(device_ver6)
    appVer38.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer39 = ApplicationVersion.objects.create(
        name="Peercoin",
        version=66055,
        display_name="Peercoin",
        icon="peercoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/peercoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/peercoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/peercoin/app_del",
        delete_key="blue/2.1.0-hw15/peercoin/app_del_key",
        app=app11
    )
    appVer39.providers.add(provider1)
    appVer39.device_versions.add(device_ver6)
    appVer39.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer40 = ApplicationVersion.objects.create(
        name="Viacoin",
        version=66055,
        display_name="Viacoin",
        icon="viacoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/viacoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/viacoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/viacoin/app_del",
        delete_key="blue/2.1.0-hw15/viacoin/app_del_key",
        app=app12
    )
    appVer40.providers.add(provider1)
    appVer40.device_versions.add(device_ver6)
    appVer40.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer41 = ApplicationVersion.objects.create(
        name="Ubiq",
        version=65793,
        display_name="Ubiq",
        icon="ubiq",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/ubiq/app_1.1.1",
        firmware_key="blue/2.1.0-hw15/ubiq/app_1.1.1_key",
        delete="blue/2.1.0-hw15/ubiq/app_del",
        delete_key="blue/2.1.0-hw15/ubiq/app_del_key",
        app=app13
    )
    appVer41.providers.add(provider1)
    appVer41.device_versions.add(device_ver6)
    appVer41.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer42 = ApplicationVersion.objects.create(
        name="Expanse",
        version=65793,
        display_name="Expanse",
        icon="expanse",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/expanse/app_1.1.1",
        firmware_key="blue/2.1.0-hw15/expanse/app_1.1.1_key",
        delete="blue/2.1.0-hw15/expanse/app_del",
        delete_key="blue/2.1.0-hw15/expanse/app_del_key",
        app=app14
    )
    appVer42.providers.add(provider1)
    appVer42.device_versions.add(device_ver6)
    appVer42.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer43 = ApplicationVersion.objects.create(
        name="Dash",
        version=66055,
        display_name="Dash",
        icon="dash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/dash/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/dash/app_1.2.7_key",
        delete="blue/2.1.0-hw15/dash/app_del",
        delete_key="blue/2.1.0-hw15/dash/app_del_key",
        app=app15
    )
    appVer43.providers.add(provider1)
    appVer43.device_versions.add(device_ver6)
    appVer43.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer44 = ApplicationVersion.objects.create(
        name="Dogecoin",
        version=66055,
        display_name="Dogecoin",
        icon="dogecoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/dogecoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/dogecoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/dogecoin/app_del",
        delete_key="blue/2.1.0-hw15/dogecoin/app_del_key",
        app=app16
    )
    appVer44.providers.add(provider1)
    appVer44.device_versions.add(device_ver6)
    appVer44.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer45 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65793,
        display_name="Ethereum",
        icon="ethereum",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/ethereum/app_1.1.1",
        firmware_key="blue/2.1.0-hw15/ethereum/app_1.1.1_key",
        delete="blue/2.1.0-hw15/ethereum/app_del",
        delete_key="blue/2.1.0-hw15/ethereum/app_del_key",
        app=app17
    )
    appVer45.providers.add(provider1)
    appVer45.device_versions.add(device_ver6)
    appVer45.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer46 = ApplicationVersion.objects.create(
        name="Fido U2F",
        version=66053,
        display_name="Fido U2F",
        icon="fido",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/u2f/app_1.2.5",
        firmware_key="blue/2.1.0-hw15/u2f/app_1.2.5_key",
        delete="blue/2.1.0-hw15/u2f/app_del",
        delete_key="blue/2.1.0-hw15/u2f/app_del_key",
        app=app18
    )
    appVer46.providers.add(provider1)
    appVer46.device_versions.add(device_ver6)
    appVer46.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer47 = ApplicationVersion.objects.create(
        name="Litecoin",
        version=66055,
        display_name="Litecoin",
        icon="litecoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/litecoin/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/litecoin/app_1.2.7_key",
        delete="blue/2.1.0-hw15/litecoin/app_del",
        delete_key="blue/2.1.0-hw15/litecoin/app_del_key",
        app=app19
    )
    appVer47.providers.add(provider1)
    appVer47.device_versions.add(device_ver6)
    appVer47.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer48 = ApplicationVersion.objects.create(
        name="Stratis",
        version=66055,
        display_name="Stratis",
        icon="stratis",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/stratis/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/stratis/app_1.2.7_key",
        delete="blue/2.1.0-hw15/stratis/app_del",
        delete_key="blue/2.1.0-hw15/stratis/app_del_key",
        app=app20
    )
    appVer48.providers.add(provider1)
    appVer48.device_versions.add(device_ver6)
    appVer48.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer49 = ApplicationVersion.objects.create(
        name="Ripple",
        version=65541,
        display_name="Ripple",
        icon="ripple",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/ripple/app_1.0.5",
        firmware_key="blue/2.1.0-hw15/ripple/app_1.0.5_key",
        delete="blue/2.1.0-hw15/ripple/app_del",
        delete_key="blue/2.1.0-hw15/ripple/app_del_key",
        app=app21
    )
    appVer49.providers.add(provider1)
    appVer49.device_versions.add(device_ver6)
    appVer49.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer50 = ApplicationVersion.objects.create(
        name="Zcash",
        version=66052,
        display_name="Zcash",
        icon="zcash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/zcash/app_1.2.4",
        firmware_key="blue/2.1.0-hw15/zcash/app_1.2.4_key",
        delete="blue/2.1.0-hw15/zcash/app_del",
        delete_key="blue/2.1.0-hw15/zcash/app_del_key",
        app=app22
    )
    appVer50.providers.add(provider1)
    appVer50.device_versions.add(device_ver6)
    appVer50.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer51 = ApplicationVersion.objects.create(
        name="ZenCash",
        version=66052,
        display_name="ZenCash",
        icon="zencash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/zencash/app_1.2.4",
        firmware_key="blue/2.1.0-hw15/zencash/app_1.2.4_key",
        delete="blue/2.1.0-hw15/zencash/app_del",
        delete_key="blue/2.1.0-hw15/zencash/app_del_key",
        app=app23
    )
    appVer51.providers.add(provider1)
    appVer51.device_versions.add(device_ver6)
    appVer51.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer52 = ApplicationVersion.objects.create(
        name="Komodo",
        version=66055,
        display_name="Komodo",
        icon="komodo",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/komodo/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/komodo/app_1.2.7_key",
        delete="blue/2.1.0-hw15/komodo/app_del",
        delete_key="blue/2.1.0-hw15/komodo/app_del_key",
        app=app24
    )
    appVer52.providers.add(provider1)
    appVer52.device_versions.add(device_ver6)
    appVer52.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer53 = ApplicationVersion.objects.create(
        name="PoSW",
        version=66055,
        display_name="PoSW",
        icon="posw",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/posw/app_1.2.7",
        firmware_key="blue/2.1.0-hw15/posw/app_1.2.7_key",
        delete="blue/2.1.0-hw15/posw/app_del",
        delete_key="blue/2.1.0-hw15/posw/app_del_key",
        app=app25
    )
    appVer53.providers.add(provider1)
    appVer53.device_versions.add(device_ver6)
    appVer53.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2hw10 ,
    appVer54 = ApplicationVersion.objects.create(
        name="Stellar",
        version=196608,
        display_name="Stellar",
        icon="stellar",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/stellar/app_3.0.0",
        firmware_key="blue/2.1.0-hw15/stellar/app_3.0.0_key",
        delete="blue/2.1.0-hw15/stellar/app_del",
        delete_key="blue/2.1.0-hw15/stellar/app_del_key",
        app=app26
    )
    appVer54.providers.add(provider1)
    appVer54.device_versions.add(device_ver6)
    appVer54.se_firmware_final_versions.add(
        firmware_final_ver9, firmware_final_ver11)
    # blue_2 ,
    appVer55 = ApplicationVersion.objects.create(
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
    appVer55.providers.add(provider1)
    appVer55.device_versions.add(device_ver2)
    appVer55.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer56 = ApplicationVersion.objects.create(
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
    appVer56.providers.add(provider1)
    appVer56.device_versions.add(device_ver2)
    appVer56.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer57 = ApplicationVersion.objects.create(
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
        app=app15
    )
    appVer57.providers.add(provider1)
    appVer57.device_versions.add(device_ver2)
    appVer57.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer58 = ApplicationVersion.objects.create(
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
        app=app16
    )
    appVer58.providers.add(provider1)
    appVer58.device_versions.add(device_ver2)
    appVer58.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer59 = ApplicationVersion.objects.create(
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
        app=app17
    )
    appVer59.providers.add(provider1)
    appVer59.device_versions.add(device_ver2)
    appVer59.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer60 = ApplicationVersion.objects.create(
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
        app=app19
    )
    appVer60.providers.add(provider1)
    appVer60.device_versions.add(device_ver2)
    appVer60.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer61 = ApplicationVersion.objects.create(
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
        app=app20
    )
    appVer61.providers.add(provider1)
    appVer61.device_versions.add(device_ver2)
    appVer61.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer62 = ApplicationVersion.objects.create(
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
        app=app22
    )
    appVer62.providers.add(provider1)
    appVer62.device_versions.add(device_ver2)
    appVer62.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer63 = ApplicationVersion.objects.create(
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
        app=app21
    )
    appVer63.providers.add(provider1)
    appVer63.device_versions.add(device_ver2)
    appVer63.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer64 = ApplicationVersion.objects.create(
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
    appVer64.providers.add(provider1)
    appVer64.device_versions.add(device_ver2)
    appVer64.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer65 = ApplicationVersion.objects.create(
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
        app=app13
    )
    appVer65.providers.add(provider1)
    appVer65.device_versions.add(device_ver2)
    appVer65.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer66 = ApplicationVersion.objects.create(
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
        app=app14
    )
    appVer66.providers.add(provider1)
    appVer66.device_versions.add(device_ver2)
    appVer66.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer67 = ApplicationVersion.objects.create(
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
    appVer67.providers.add(provider1)
    appVer67.device_versions.add(device_ver2)
    appVer67.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer68 = ApplicationVersion.objects.create(
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
        app=app27
    )
    appVer68.providers.add(provider1)
    appVer68.device_versions.add(device_ver2)
    appVer68.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer69 = ApplicationVersion.objects.create(
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
    appVer69.providers.add(provider1)
    appVer69.device_versions.add(device_ver2)
    appVer69.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer70 = ApplicationVersion.objects.create(
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
        app=app12
    )
    appVer70.providers.add(provider1)
    appVer70.device_versions.add(device_ver2)
    appVer70.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer71 = ApplicationVersion.objects.create(
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
        app=app24
    )
    appVer71.providers.add(provider1)
    appVer71.device_versions.add(device_ver2)
    appVer71.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer72 = ApplicationVersion.objects.create(
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
    appVer72.providers.add(provider1)
    appVer72.device_versions.add(device_ver2)
    appVer72.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer73 = ApplicationVersion.objects.create(
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
    appVer73.providers.add(provider1)
    appVer73.device_versions.add(device_ver2)
    appVer73.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer74 = ApplicationVersion.objects.create(
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
    appVer74.providers.add(provider1)
    appVer74.device_versions.add(device_ver2)
    appVer74.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer75 = ApplicationVersion.objects.create(
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
    appVer75.providers.add(provider1)
    appVer75.device_versions.add(device_ver2)
    appVer75.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer76 = ApplicationVersion.objects.create(
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
        app=app28
    )
    appVer76.providers.add(provider1)
    appVer76.device_versions.add(device_ver2)
    appVer76.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # blue_2 ,
    appVer77 = ApplicationVersion.objects.create(
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
        app=app26
    )
    appVer77.providers.add(provider1)
    appVer77.device_versions.add(device_ver2)
    appVer77.se_firmware_final_versions.add(
        firmware_final_ver0, firmware_final_ver8)
    # nanos ,
    appVer78 = ApplicationVersion.objects.create(
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
    appVer78.providers.add(provider1)
    appVer78.device_versions.add(device_ver1)
    appVer78.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer79 = ApplicationVersion.objects.create(
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
    appVer79.providers.add(provider1)
    appVer79.device_versions.add(device_ver1)
    appVer79.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer80 = ApplicationVersion.objects.create(
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
        app=app15
    )
    appVer80.providers.add(provider1)
    appVer80.device_versions.add(device_ver1)
    appVer80.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer81 = ApplicationVersion.objects.create(
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
        app=app16
    )
    appVer81.providers.add(provider1)
    appVer81.device_versions.add(device_ver1)
    appVer81.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer82 = ApplicationVersion.objects.create(
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
        app=app17
    )
    appVer82.providers.add(provider1)
    appVer82.device_versions.add(device_ver1)
    appVer82.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer83 = ApplicationVersion.objects.create(
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
        app=app18
    )
    appVer83.providers.add(provider1)
    appVer83.device_versions.add(device_ver1)
    appVer83.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer84 = ApplicationVersion.objects.create(
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
        app=app24
    )
    appVer84.providers.add(provider1)
    appVer84.device_versions.add(device_ver1)
    appVer84.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer85 = ApplicationVersion.objects.create(
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
        app=app19
    )
    appVer85.providers.add(provider1)
    appVer85.device_versions.add(device_ver1)
    appVer85.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer86 = ApplicationVersion.objects.create(
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
        app=app20
    )
    appVer86.providers.add(provider1)
    appVer86.device_versions.add(device_ver1)
    appVer86.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer87 = ApplicationVersion.objects.create(
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
        app=app22
    )
    appVer87.providers.add(provider1)
    appVer87.device_versions.add(device_ver1)
    appVer87.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer88 = ApplicationVersion.objects.create(
        name="SSH/PGP Agent",
        version=3,
        display_name="SSH/PGP Agent",
        icon="ssh",
        hash="9b52a2b0532c3bbb058a6c817b02963174f32b3d41314f7b507623f163d71b65",
        perso="perso_11",
        firmware="nanos/1.3.1/ssh-agent/st31_gpg_0.0.3",
        firmware_key="nanos/1.3.1/ssh-agent/st31_gpg_0.0.3_key",
        delete="nanos/1.3.1/ssh-agent/st31_gpg_del",
        delete_key="nanos/1.3.1/ssh-agent/st31_gpg_del_key",
        app=app29
    )
    appVer88.providers.add(provider1)
    appVer88.device_versions.add(device_ver1)
    appVer88.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer89 = ApplicationVersion.objects.create(
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
        app=app30
    )
    appVer89.providers.add(provider1)
    appVer89.device_versions.add(device_ver1)
    appVer89.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer90 = ApplicationVersion.objects.create(
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
        app=app31
    )
    appVer90.providers.add(provider1)
    appVer90.device_versions.add(device_ver1)
    appVer90.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer91 = ApplicationVersion.objects.create(
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
        app=app32
    )
    appVer91.providers.add(provider1)
    appVer91.device_versions.add(device_ver1)
    appVer91.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer92 = ApplicationVersion.objects.create(
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
        app=app21
    )
    appVer92.providers.add(provider1)
    appVer92.device_versions.add(device_ver1)
    appVer92.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer93 = ApplicationVersion.objects.create(
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
    appVer93.providers.add(provider1)
    appVer93.device_versions.add(device_ver1)
    appVer93.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer94 = ApplicationVersion.objects.create(
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
        app=app33
    )
    appVer94.providers.add(provider1)
    appVer94.device_versions.add(device_ver1)
    appVer94.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer95 = ApplicationVersion.objects.create(
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
        app=app13
    )
    appVer95.providers.add(provider1)
    appVer95.device_versions.add(device_ver1)
    appVer95.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer96 = ApplicationVersion.objects.create(
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
        app=app14
    )
    appVer96.providers.add(provider1)
    appVer96.device_versions.add(device_ver1)
    appVer96.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer97 = ApplicationVersion.objects.create(
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
    appVer97.providers.add(provider1)
    appVer97.device_versions.add(device_ver1)
    appVer97.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer98 = ApplicationVersion.objects.create(
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
        app=app27
    )
    appVer98.providers.add(provider1)
    appVer98.device_versions.add(device_ver1)
    appVer98.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer99 = ApplicationVersion.objects.create(
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
    appVer99.providers.add(provider1)
    appVer99.device_versions.add(device_ver1)
    appVer99.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer100 = ApplicationVersion.objects.create(
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
        app=app12
    )
    appVer100.providers.add(provider1)
    appVer100.device_versions.add(device_ver1)
    appVer100.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer101 = ApplicationVersion.objects.create(
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
    appVer101.providers.add(provider1)
    appVer101.device_versions.add(device_ver1)
    appVer101.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer102 = ApplicationVersion.objects.create(
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
        app=app28
    )
    appVer102.providers.add(provider1)
    appVer102.device_versions.add(device_ver1)
    appVer102.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer103 = ApplicationVersion.objects.create(
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
    appVer103.providers.add(provider1)
    appVer103.device_versions.add(device_ver1)
    appVer103.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer104 = ApplicationVersion.objects.create(
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
        app=app26
    )
    appVer104.providers.add(provider1)
    appVer104.device_versions.add(device_ver1)
    appVer104.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer105 = ApplicationVersion.objects.create(
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
    appVer105.providers.add(provider1)
    appVer105.device_versions.add(device_ver1)
    appVer105.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer106 = ApplicationVersion.objects.create(
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
    appVer106.providers.add(provider1)
    appVer106.device_versions.add(device_ver1)
    appVer106.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer107 = ApplicationVersion.objects.create(
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
    appVer107.providers.add(provider1)
    appVer107.device_versions.add(device_ver1)
    appVer107.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer108 = ApplicationVersion.objects.create(
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
    appVer108.providers.add(provider3)
    appVer108.device_versions.add(device_ver1)
    appVer108.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer109 = ApplicationVersion.objects.create(
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
        app=app17
    )
    appVer109.providers.add(provider3)
    appVer109.device_versions.add(device_ver1)
    appVer109.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer110 = ApplicationVersion.objects.create(
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
        app=app34
    )
    appVer110.providers.add(provider3)
    appVer110.device_versions.add(device_ver1)
    appVer110.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer111 = ApplicationVersion.objects.create(
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
        app=app22
    )
    appVer111.providers.add(provider3)
    appVer111.device_versions.add(device_ver1)
    appVer111.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer112 = ApplicationVersion.objects.create(
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
        app=app18
    )
    appVer112.providers.add(provider3)
    appVer112.device_versions.add(device_ver1)
    appVer112.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer113 = ApplicationVersion.objects.create(
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
    appVer113.providers.add(provider2)
    appVer113.device_versions.add(device_ver1)
    appVer113.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer114 = ApplicationVersion.objects.create(
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
    appVer114.providers.add(provider2)
    appVer114.device_versions.add(device_ver1)
    appVer114.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer115 = ApplicationVersion.objects.create(
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
        app=app17
    )
    appVer115.providers.add(provider2)
    appVer115.device_versions.add(device_ver1)
    appVer115.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer116 = ApplicationVersion.objects.create(
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
        app=app21
    )
    appVer116.providers.add(provider2)
    appVer116.device_versions.add(device_ver1)
    appVer116.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer117 = ApplicationVersion.objects.create(
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
        app=app35
    )
    appVer117.providers.add(provider2)
    appVer117.device_versions.add(device_ver1)
    appVer117.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer118 = ApplicationVersion.objects.create(
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
    appVer118.providers.add(provider1)
    appVer118.device_versions.add(device_ver1)
    appVer118.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer119 = ApplicationVersion.objects.create(
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
        app=app15
    )
    appVer119.providers.add(provider1)
    appVer119.device_versions.add(device_ver1)
    appVer119.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer120 = ApplicationVersion.objects.create(
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
        app=app16
    )
    appVer120.providers.add(provider1)
    appVer120.device_versions.add(device_ver1)
    appVer120.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer121 = ApplicationVersion.objects.create(
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
        app=app17
    )
    appVer121.providers.add(provider1)
    appVer121.device_versions.add(device_ver1)
    appVer121.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer122 = ApplicationVersion.objects.create(
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
        app=app19
    )
    appVer122.providers.add(provider1)
    appVer122.device_versions.add(device_ver1)
    appVer122.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer123 = ApplicationVersion.objects.create(
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
        app=app20
    )
    appVer123.providers.add(provider1)
    appVer123.device_versions.add(device_ver1)
    appVer123.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer124 = ApplicationVersion.objects.create(
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
        app=app22
    )
    appVer124.providers.add(provider1)
    appVer124.device_versions.add(device_ver1)
    appVer124.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer125 = ApplicationVersion.objects.create(
        name="SSH/PGP Agent",
        version=2,
        display_name="SSH/PGP Agent",
        icon="ssh",
        hash="818fa91da1c658b47f0d6c7da6f8e7523d8b9ad1706ed3e9bbec9b87a6eb5fce",
        perso="perso_11",
        firmware="nanos/1.3/sshgpg/st31_gpg_0.0.2",
        firmware_key="nanos/1.3/sshgpg/st31_gpg_0.0.2_key",
        delete="nanos/1.3/sshgpg/st31_gpg_del",
        delete_key="nanos/1.3/sshgpg/st31_gpg_del_key",
        app=app29
    )
    appVer125.providers.add(provider1)
    appVer125.device_versions.add(device_ver1)
    appVer125.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer126 = ApplicationVersion.objects.create(
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
    appVer126.providers.add(provider1)
    appVer126.device_versions.add(device_ver1)
    appVer126.se_firmware_final_versions.add(firmware_final_ver1_2)
    # nanos ,
    appVer127 = ApplicationVersion.objects.create(
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
        app=app36
    )
    appVer127.providers.add(provider1)
    appVer127.device_versions.add(device_ver1)
    appVer127.se_firmware_final_versions.add(firmware_final_ver1_2)
    # nanos ,
    appVer128 = ApplicationVersion.objects.create(
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
        app=app15
    )
    appVer128.providers.add(provider1)
    appVer128.device_versions.add(device_ver1)
    appVer128.se_firmware_final_versions.add(firmware_final_ver1_2)
    # nanos ,
    appVer129 = ApplicationVersion.objects.create(
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
        app=app16
    )
    appVer129.providers.add(provider1)
    appVer129.device_versions.add(device_ver1)
    appVer129.se_firmware_final_versions.add(firmware_final_ver1_2)
    # nanos ,
    appVer130 = ApplicationVersion.objects.create(
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
        app=app17
    )
    appVer130.providers.add(provider1)
    appVer130.device_versions.add(device_ver1)
    appVer130.se_firmware_final_versions.add(firmware_final_ver1_2)
    # nanos ,
    appVer131 = ApplicationVersion.objects.create(
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
        app=app19
    )
    appVer131.providers.add(provider1)
    appVer131.device_versions.add(device_ver1)
    appVer131.se_firmware_final_versions.add(firmware_final_ver1_2)
    # nanos ,
    appVer132 = ApplicationVersion.objects.create(
        name="SSH/PGP Agent",
        version=1,
        display_name="SSH/PGP Agent",
        icon="ssh",
        hash="undefined",
        perso="perso_11",
        firmware="nanos_12/st31_gpg",
        firmware_key="nanos_12/st31_gpg_key",
        delete="undefined",
        delete_key="undefined",
        app=app29
    )
    appVer132.providers.add(provider1)
    appVer132.device_versions.add(device_ver1)
    appVer132.se_firmware_final_versions.add(firmware_final_ver1_2)
    # nanos ,
    appVer133 = ApplicationVersion.objects.create(
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
        app=app20
    )
    appVer133.providers.add(provider1)
    appVer133.device_versions.add(device_ver1)
    appVer133.se_firmware_final_versions.add(firmware_final_ver1_2)
    # nanos ,
    appVer134 = ApplicationVersion.objects.create(
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
        app=app22
    )
    appVer134.providers.add(provider1)
    appVer134.device_versions.add(device_ver1)
    appVer134.se_firmware_final_versions.add(firmware_final_ver1_2)
    # nanos ,
    appVer135 = ApplicationVersion.objects.create(
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
    appVer135.providers.add(provider1)
    appVer135.device_versions.add(device_ver1)
    appVer135.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer136 = ApplicationVersion.objects.create(
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
        app=app17
    )
    appVer136.providers.add(provider1)
    appVer136.device_versions.add(device_ver1)
    appVer136.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer137 = ApplicationVersion.objects.create(
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
        app=app18
    )
    appVer137.providers.add(provider1)
    appVer137.device_versions.add(device_ver1)
    appVer137.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer138 = ApplicationVersion.objects.create(
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
        app=app19
    )
    appVer138.providers.add(provider1)
    appVer138.device_versions.add(device_ver1)
    appVer138.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos ,
    appVer139 = ApplicationVersion.objects.create(
        name="SSH/PGP Agent",
        version=1,
        display_name="SSH/PGP Agent",
        icon="ssh",
        hash="0cd8553b3a7d1341ad4d9dda8f7f9b380dcc473a0f6c1db1c1acc66180106311",
        perso="perso_11",
        firmware="st31_gpg",
        firmware_key="st31_gpg_key",
        delete="undefined",
        delete_key="undefined",
        app=app29
    )
    appVer139.providers.add(provider1)
    appVer139.device_versions.add(device_ver1)
    appVer139.se_firmware_final_versions.add(firmware_final_ver1)
    # nanos-1.4 ,
    appVer140 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=66056,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin/app_1.2.8",
        firmware_key="nanos/1.4.2/bitcoin/app_1.2.8_key",
        delete="nanos/1.4.2/bitcoin/app_del",
        delete_key="nanos/1.4.2/bitcoin/app_del_key",
        app=app0
    )
    appVer140.providers.add(provider1)
    appVer140.device_versions.add(device_ver5)
    appVer140.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer141 = ApplicationVersion.objects.create(
        name="Bitcoin Cash",
        version=66056,
        display_name="Bitcoin Cash",
        icon="bitcoin_cash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_cash/app_1.2.8",
        firmware_key="nanos/1.4.2/bitcoin_cash/app_1.2.8_key",
        delete="nanos/1.4.2/bitcoin_cash/app_del",
        delete_key="nanos/1.4.2/bitcoin_cash/app_del_key",
        app=app1
    )
    appVer141.providers.add(provider1)
    appVer141.device_versions.add(device_ver5)
    appVer141.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer142 = ApplicationVersion.objects.create(
        name="Bitcoin Gold",
        version=66056,
        display_name="Bitcoin Gold",
        icon="bitcoin_gold",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_gold/app_1.2.8",
        firmware_key="nanos/1.4.2/bitcoin_gold/app_1.2.8_key",
        delete="nanos/1.4.2/bitcoin_gold/app_del",
        delete_key="nanos/1.4.2/bitcoin_gold/app_del_key",
        app=app2
    )
    appVer142.providers.add(provider1)
    appVer142.device_versions.add(device_ver5)
    appVer142.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer143 = ApplicationVersion.objects.create(
        name="Bitcoin Private",
        version=66056,
        display_name="Bitcoin Private",
        icon="bitcoin_private",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_private/app_1.2.8",
        firmware_key="nanos/1.4.2/bitcoin_private/app_1.2.8_key",
        delete="nanos/1.4.2/bitcoin_private/app_del",
        delete_key="nanos/1.4.2/bitcoin_private/app_del_key",
        app=app3
    )
    appVer143.providers.add(provider1)
    appVer143.device_versions.add(device_ver5)
    appVer143.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer144 = ApplicationVersion.objects.create(
        name="Bitcoin testnet",
        version=66056,
        display_name="Bitcoin testnet",
        icon="bitcoin_testnet",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_testnet/app_1.2.8",
        firmware_key="nanos/1.4.2/bitcoin_testnet/app_1.2.8_key",
        delete="nanos/1.4.2/bitcoin_testnet/app_del",
        delete_key="nanos/1.4.2/bitcoin_testnet/app_del_key",
        app=app4
    )
    appVer144.providers.add(provider1)
    appVer144.device_versions.add(device_ver5)
    appVer144.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer145 = ApplicationVersion.objects.create(
        name="Digibyte",
        version=66056,
        display_name="Digibyte",
        icon="digibyte",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/digibyte/app_1.2.8",
        firmware_key="nanos/1.4.2/digibyte/app_1.2.8_key",
        delete="nanos/1.4.2/digibyte/app_del",
        delete_key="nanos/1.4.2/digibyte/app_del_key",
        app=app5
    )
    appVer145.providers.add(provider1)
    appVer145.device_versions.add(device_ver5)
    appVer145.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer146 = ApplicationVersion.objects.create(
        name="HCash",
        version=66056,
        display_name="HCash",
        icon="hcash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/hcash/app_1.2.8",
        firmware_key="nanos/1.4.2/hcash/app_1.2.8_key",
        delete="nanos/1.4.2/hcash/app_del",
        delete_key="nanos/1.4.2/hcash/app_del_key",
        app=app6
    )
    appVer146.providers.add(provider1)
    appVer146.device_versions.add(device_ver5)
    appVer146.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer147 = ApplicationVersion.objects.create(
        name="Qtum",
        version=66056,
        display_name="Qtum",
        icon="qtum",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/qtum/app_1.2.8",
        firmware_key="nanos/1.4.2/qtum/app_1.2.8_key",
        delete="nanos/1.4.2/qtum/app_del",
        delete_key="nanos/1.4.2/qtum/app_del_key",
        app=app7
    )
    appVer147.providers.add(provider1)
    appVer147.device_versions.add(device_ver5)
    appVer147.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer148 = ApplicationVersion.objects.create(
        name="PIVX",
        version=66056,
        display_name="PIVX",
        icon="pivx",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/pivx/app_1.2.8",
        firmware_key="nanos/1.4.2/pivx/app_1.2.8_key",
        delete="nanos/1.4.2/pivx/app_del",
        delete_key="nanos/1.4.2/pivx/app_del_key",
        app=app8
    )
    appVer148.providers.add(provider1)
    appVer148.device_versions.add(device_ver5)
    appVer148.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer149 = ApplicationVersion.objects.create(
        name="Stealth",
        version=66056,
        display_name="Stealth",
        icon="stealthcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/stealthcoin/app_1.2.8",
        firmware_key="nanos/1.4.2/stealthcoin/app_1.2.8_key",
        delete="nanos/1.4.2/stealthcoin/app_del",
        delete_key="nanos/1.4.2/stealthcoin/app_del_key",
        app=app9
    )
    appVer149.providers.add(provider1)
    appVer149.device_versions.add(device_ver5)
    appVer149.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer150 = ApplicationVersion.objects.create(
        name="Vertcoin",
        version=66056,
        display_name="Vertcoin",
        icon="vertcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/vertcoin/app_1.2.8",
        firmware_key="nanos/1.4.2/vertcoin/app_1.2.8_key",
        delete="nanos/1.4.2/vertcoin/app_del",
        delete_key="nanos/1.4.2/vertcoin/app_del_key",
        app=app10
    )
    appVer150.providers.add(provider1)
    appVer150.device_versions.add(device_ver5)
    appVer150.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer151 = ApplicationVersion.objects.create(
        name="Viacoin",
        version=66056,
        display_name="Viacoin",
        icon="viacoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/viacoin/app_1.2.8",
        firmware_key="nanos/1.4.2/viacoin/app_1.2.8_key",
        delete="nanos/1.4.2/viacoin/app_del",
        delete_key="nanos/1.4.2/viacoin/app_del_key",
        app=app12
    )
    appVer151.providers.add(provider1)
    appVer151.device_versions.add(device_ver5)
    appVer151.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer152 = ApplicationVersion.objects.create(
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
        app=app13
    )
    appVer152.providers.add(provider1)
    appVer152.device_versions.add(device_ver5)
    appVer152.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer153 = ApplicationVersion.objects.create(
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
        app=app14
    )
    appVer153.providers.add(provider1)
    appVer153.device_versions.add(device_ver5)
    appVer153.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer154 = ApplicationVersion.objects.create(
        name="Dash",
        version=66056,
        display_name="Dash",
        icon="dash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/dash/app_1.2.8",
        firmware_key="nanos/1.4.2/dash/app_1.2.8_key",
        delete="nanos/1.4.2/dash/app_del",
        delete_key="nanos/1.4.2/dash/app_del_key",
        app=app15
    )
    appVer154.providers.add(provider1)
    appVer154.device_versions.add(device_ver5)
    appVer154.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer155 = ApplicationVersion.objects.create(
        name="Dogecoin",
        version=66056,
        display_name="Dogecoin",
        icon="dogecoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/dogecoin/app_1.2.8",
        firmware_key="nanos/1.4.2/dogecoin/app_1.2.8_key",
        delete="nanos/1.4.2/dogecoin/app_del",
        delete_key="nanos/1.4.2/dogecoin/app_del_key",
        app=app16
    )
    appVer155.providers.add(provider1)
    appVer155.device_versions.add(device_ver5)
    appVer155.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer156 = ApplicationVersion.objects.create(
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
        app=app17
    )
    appVer156.providers.add(provider1)
    appVer156.device_versions.add(device_ver5)
    appVer156.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer157 = ApplicationVersion.objects.create(
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
        app=app18
    )
    appVer157.providers.add(provider1)
    appVer157.device_versions.add(device_ver5)
    appVer157.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer158 = ApplicationVersion.objects.create(
        name="Litecoin",
        version=66056,
        display_name="Litecoin",
        icon="litecoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/litecoin/app_1.2.8",
        firmware_key="nanos/1.4.2/litecoin/app_1.2.8_key",
        delete="nanos/1.4.2/litecoin/app_del",
        delete_key="nanos/1.4.2/litecoin/app_del_key",
        app=app19
    )
    appVer158.providers.add(provider1)
    appVer158.device_versions.add(device_ver5)
    appVer158.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer159 = ApplicationVersion.objects.create(
        name="Stratis",
        version=66056,
        display_name="Stratis",
        icon="stratis",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/stratis/app_1.2.8",
        firmware_key="nanos/1.4.2/stratis/app_1.2.8_key",
        delete="nanos/1.4.2/stratis/app_del",
        delete_key="nanos/1.4.2/stratis/app_del_key",
        app=app20
    )
    appVer159.providers.add(provider1)
    appVer159.device_versions.add(device_ver5)
    appVer159.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer160 = ApplicationVersion.objects.create(
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
        app=app21
    )
    appVer160.providers.add(provider1)
    appVer160.device_versions.add(device_ver5)
    appVer160.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer161 = ApplicationVersion.objects.create(
        name="Zcash",
        version=66056,
        display_name="Zcash",
        icon="zcash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/zcash/app_1.2.8",
        firmware_key="nanos/1.4.2/zcash/app_1.2.8_key",
        delete="nanos/1.4.2/zcash/app_del",
        delete_key="nanos/1.4.2/zcash/app_del_key",
        app=app22
    )
    appVer161.providers.add(provider1)
    appVer161.device_versions.add(device_ver5)
    appVer161.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer162 = ApplicationVersion.objects.create(
        name="ZenCash",
        version=66056,
        display_name="ZenCash",
        icon="zencash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/zencash/app_1.2.8",
        firmware_key="nanos/1.4.2/zencash/app_1.2.8_key",
        delete="nanos/1.4.2/zencash/app_del",
        delete_key="nanos/1.4.2/zencash/app_del_key",
        app=app23
    )
    appVer162.providers.add(provider1)
    appVer162.device_versions.add(device_ver5)
    appVer162.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer163 = ApplicationVersion.objects.create(
        name="Komodo",
        version=66056,
        display_name="Komodo",
        icon="komodo",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/komodo/app_1.2.8",
        firmware_key="nanos/1.4.2/komodo/app_1.2.8_key",
        delete="nanos/1.4.2/komodo/app_del",
        delete_key="nanos/1.4.2/komodo/app_del_key",
        app=app24
    )
    appVer163.providers.add(provider1)
    appVer163.device_versions.add(device_ver5)
    appVer163.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer164 = ApplicationVersion.objects.create(
        name="Peercoin",
        version=66056,
        display_name="Peercoin",
        icon="peercoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/peercoin/app_1.2.8",
        firmware_key="nanos/1.4.2/peercoin/app_1.2.8_key",
        delete="nanos/1.4.2/peercoin/app_del",
        delete_key="nanos/1.4.2/peercoin/app_del_key",
        app=app11
    )
    appVer164.providers.add(provider1)
    appVer164.device_versions.add(device_ver5)
    appVer164.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer165 = ApplicationVersion.objects.create(
        name="PoSW",
        version=66056,
        display_name="PoSW",
        icon="posw",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/posw/app_1.2.8",
        firmware_key="nanos/1.4.2/posw/app_1.2.8_key",
        delete="nanos/1.4.2/posw/app_del",
        delete_key="nanos/1.4.2/posw/app_del_key",
        app=app25
    )
    appVer165.providers.add(provider1)
    appVer165.device_versions.add(device_ver5)
    appVer165.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer166 = ApplicationVersion.objects.create(
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
        app=app33
    )
    appVer166.providers.add(provider1)
    appVer166.device_versions.add(device_ver5)
    appVer166.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer167 = ApplicationVersion.objects.create(
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
        app=app28
    )
    appVer167.providers.add(provider1)
    appVer167.device_versions.add(device_ver5)
    appVer167.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer168 = ApplicationVersion.objects.create(
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
        app=app37
    )
    appVer168.providers.add(provider1)
    appVer168.device_versions.add(device_ver5)
    appVer168.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer169 = ApplicationVersion.objects.create(
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
        app=app30
    )
    appVer169.providers.add(provider1)
    appVer169.device_versions.add(device_ver5)
    appVer169.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer170 = ApplicationVersion.objects.create(
        name="Stellar",
        version=196608,
        display_name="Stellar",
        icon="stellar",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/stellar/app_3.0.0",
        firmware_key="nanos/1.4.2/stellar/app_3.0.0_key",
        delete="nanos/1.4.2/stellar/app_del",
        delete_key="nanos/1.4.2/stellar/app_del_key",
        app=app26
    )
    appVer170.providers.add(provider1)
    appVer170.device_versions.add(device_ver5)
    appVer170.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer171 = ApplicationVersion.objects.create(
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
        app=app38
    )
    appVer171.providers.add(provider1)
    appVer171.device_versions.add(device_ver5)
    appVer171.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer172 = ApplicationVersion.objects.create(
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
        app=app39
    )
    appVer172.providers.add(provider1)
    appVer172.device_versions.add(device_ver5)
    appVer172.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer173 = ApplicationVersion.objects.create(
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
        app=app32
    )
    appVer173.providers.add(provider1)
    appVer173.device_versions.add(device_ver5)
    appVer173.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer174 = ApplicationVersion.objects.create(
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
        app=app31
    )
    appVer174.providers.add(provider1)
    appVer174.device_versions.add(device_ver5)
    appVer174.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer175 = ApplicationVersion.objects.create(
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
        app=app40
    )
    appVer175.providers.add(provider1)
    appVer175.device_versions.add(device_ver5)
    appVer175.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer176 = ApplicationVersion.objects.create(
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
        app=app41
    )
    appVer176.providers.add(provider1)
    appVer176.device_versions.add(device_ver5)
    appVer176.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer177 = ApplicationVersion.objects.create(
        name="Tezos Baking",
        version=65536,
        display_name="Tezos Baking",
        icon="tezos_baking",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/tezos_baking/app_1.0.0",
        firmware_key="nanos/1.4.2/tezos_baking/app_1.0.0_key",
        delete="nanos/1.4.2/tezos_baking/app_del",
        delete_key="nanos/1.4.2/tezos_baking/app_del_key",
        app=app42
    )
    appVer177.providers.add(provider1)
    appVer177.device_versions.add(device_ver5)
    appVer177.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer178 = ApplicationVersion.objects.create(
        name="Tezos Wallet",
        version=65536,
        display_name="Tezos Wallet",
        icon="tezos_wallet",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/tezos_wallet/app_1.0.0",
        firmware_key="nanos/1.4.2/tezos_wallet/app_1.0.0_key",
        delete="nanos/1.4.2/tezos_wallet/app_del",
        delete_key="nanos/1.4.2/tezos_wallet/app_del_key",
        app=app43
    )
    appVer178.providers.add(provider1)
    appVer178.device_versions.add(device_ver5)
    appVer178.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer179 = ApplicationVersion.objects.create(
        name="Tron",
        version=66056,
        display_name="Tron",
        icon="tron",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/tron/app_1.2.8",
        firmware_key="nanos/1.4.2/tron/app_1.2.8_key",
        delete="nanos/1.4.2/tron/app_del",
        delete_key="nanos/1.4.2/tron/app_del_key",
        app=app44
    )
    appVer179.providers.add(provider1)
    appVer179.device_versions.add(device_ver5)
    appVer179.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer180 = ApplicationVersion.objects.create(
        name="Zcoin",
        version=66056,
        display_name="Zcoin",
        icon="tron",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/zcoin/app_1.2.8",
        firmware_key="nanos/1.4.2/zcoin/app_1.2.8_key",
        delete="nanos/1.4.2/zcoin/app_del",
        delete_key="nanos/1.4.2/zcoin/app_del_key",
        app=app45
    )
    appVer180.providers.add(provider1)
    appVer180.device_versions.add(device_ver5)
    appVer180.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer181 = ApplicationVersion.objects.create(
        name="Dascoin",
        version=65796,
        display_name="Dascoin",
        icon="dascoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2-das/dascoin/app_1.1.4",
        firmware_key="nanos/1.4.2-das/dascoin/app_1.1.4_key",
        delete="nanos/1.4.2-das/dascoin/app_del",
        delete_key="nanos/1.4.2-das/dascoin/app_del_key",
        app=app46
    )
    appVer181.providers.add(provider2)
    appVer181.device_versions.add(device_ver5)
    appVer181.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer182 = ApplicationVersion.objects.create(
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
    appVer182.providers.add(provider2)
    appVer182.device_versions.add(device_ver5)
    appVer182.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer183 = ApplicationVersion.objects.create(
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
    appVer183.providers.add(provider2)
    appVer183.device_versions.add(device_ver5)
    appVer183.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer184 = ApplicationVersion.objects.create(
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
        app=app17
    )
    appVer184.providers.add(provider2)
    appVer184.device_versions.add(device_ver5)
    appVer184.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer185 = ApplicationVersion.objects.create(
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
        app=app21
    )
    appVer185.providers.add(provider2)
    appVer185.device_versions.add(device_ver5)
    appVer185.se_firmware_final_versions.add(firmware_final_ver3)
    # nanos-1.4 ,
    appVer186 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=66052,
        display_name="Bitcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/bitcoin/app_1.2.4",
        firmware_key="nanos/1.4.1/bitcoin/app_1.2.4_key",
        delete="nanos/1.4.1/bitcoin/app_del",
        delete_key="nanos/1.4.1/bitcoin/app_del_key",
        app=app0
    )
    appVer186.providers.add(provider1)
    appVer186.device_versions.add(device_ver5)
    appVer186.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer187 = ApplicationVersion.objects.create(
        name="Bitcoin Cash",
        version=66052,
        display_name="Bitcoin Cash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/bitcoin_cash/app_1.2.4",
        firmware_key="nanos/1.4.1/bitcoin_cash/app_1.2.4_key",
        delete="nanos/1.4.1/bitcoin_cash/app_del",
        delete_key="nanos/1.4.1/bitcoin_cash/app_del_key",
        app=app1
    )
    appVer187.providers.add(provider1)
    appVer187.device_versions.add(device_ver5)
    appVer187.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer188 = ApplicationVersion.objects.create(
        name="Bitcoin Gold",
        version=66052,
        display_name="Bitcoin Gold",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/bitcoin_gold/app_1.2.4",
        firmware_key="nanos/1.4.1/bitcoin_gold/app_1.2.4_key",
        delete="nanos/1.4.1/bitcoin_gold/app_del",
        delete_key="nanos/1.4.1/bitcoin_gold/app_del_key",
        app=app2
    )
    appVer188.providers.add(provider1)
    appVer188.device_versions.add(device_ver5)
    appVer188.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer189 = ApplicationVersion.objects.create(
        name="Bitcoin testnet",
        version=66052,
        display_name="Bitcoin testnet",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/bitcoin_testnet/app_1.2.4",
        firmware_key="nanos/1.4.1/bitcoin_testnet/app_1.2.4_key",
        delete="nanos/1.4.1/bitcoin_testnet/app_del",
        delete_key="nanos/1.4.1/bitcoin_testnet/app_del_key",
        app=app4
    )
    appVer189.providers.add(provider1)
    appVer189.device_versions.add(device_ver5)
    appVer189.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer190 = ApplicationVersion.objects.create(
        name="Digibyte",
        version=66052,
        display_name="Digibyte",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/digibyte/app_1.2.4",
        firmware_key="nanos/1.4.1/digibyte/app_1.2.4_key",
        delete="nanos/1.4.1/digibyte/app_del",
        delete_key="nanos/1.4.1/digibyte/app_del_key",
        app=app5
    )
    appVer190.providers.add(provider1)
    appVer190.device_versions.add(device_ver5)
    appVer190.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer191 = ApplicationVersion.objects.create(
        name="HCash",
        version=66052,
        display_name="HCash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/hcash/app_1.2.4",
        firmware_key="nanos/1.4.1/hcash/app_1.2.4_key",
        delete="nanos/1.4.1/hcash/app_del",
        delete_key="nanos/1.4.1/hcash/app_del_key",
        app=app6
    )
    appVer191.providers.add(provider1)
    appVer191.device_versions.add(device_ver5)
    appVer191.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer192 = ApplicationVersion.objects.create(
        name="Qtum",
        version=66052,
        display_name="Qtum",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/qtum/app_1.2.4",
        firmware_key="nanos/1.4.1/qtum/app_1.2.4_key",
        delete="nanos/1.4.1/qtum/app_del",
        delete_key="nanos/1.4.1/qtum/app_del_key",
        app=app7
    )
    appVer192.providers.add(provider1)
    appVer192.device_versions.add(device_ver5)
    appVer192.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer193 = ApplicationVersion.objects.create(
        name="PIVX",
        version=66052,
        display_name="PIVX",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/pivx/app_1.2.4",
        firmware_key="nanos/1.4.1/pivx/app_1.2.4_key",
        delete="nanos/1.4.1/pivx/app_del",
        delete_key="nanos/1.4.1/pivx/app_del_key",
        app=app8
    )
    appVer193.providers.add(provider1)
    appVer193.device_versions.add(device_ver5)
    appVer193.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer194 = ApplicationVersion.objects.create(
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
        app=app27
    )
    appVer194.providers.add(provider1)
    appVer194.device_versions.add(device_ver5)
    appVer194.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer195 = ApplicationVersion.objects.create(
        name="Vertcoin",
        version=66052,
        display_name="Vertcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/vertcoin/app_1.2.4",
        firmware_key="nanos/1.4.1/vertcoin/app_1.2.4_key",
        delete="nanos/1.4.1/vertcoin/app_del",
        delete_key="nanos/1.4.1/vertcoin/app_del_key",
        app=app10
    )
    appVer195.providers.add(provider1)
    appVer195.device_versions.add(device_ver5)
    appVer195.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer196 = ApplicationVersion.objects.create(
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
        app=app12
    )
    appVer196.providers.add(provider1)
    appVer196.device_versions.add(device_ver5)
    appVer196.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer197 = ApplicationVersion.objects.create(
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
        app=app13
    )
    appVer197.providers.add(provider1)
    appVer197.device_versions.add(device_ver5)
    appVer197.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer198 = ApplicationVersion.objects.create(
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
        app=app14
    )
    appVer198.providers.add(provider1)
    appVer198.device_versions.add(device_ver5)
    appVer198.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer199 = ApplicationVersion.objects.create(
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
        app=app15
    )
    appVer199.providers.add(provider1)
    appVer199.device_versions.add(device_ver5)
    appVer199.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer200 = ApplicationVersion.objects.create(
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
        app=app16
    )
    appVer200.providers.add(provider1)
    appVer200.device_versions.add(device_ver5)
    appVer200.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer201 = ApplicationVersion.objects.create(
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
        app=app17
    )
    appVer201.providers.add(provider1)
    appVer201.device_versions.add(device_ver5)
    appVer201.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer202 = ApplicationVersion.objects.create(
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
        app=app18
    )
    appVer202.providers.add(provider1)
    appVer202.device_versions.add(device_ver5)
    appVer202.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer203 = ApplicationVersion.objects.create(
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
        app=app19
    )
    appVer203.providers.add(provider1)
    appVer203.device_versions.add(device_ver5)
    appVer203.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer204 = ApplicationVersion.objects.create(
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
        app=app20
    )
    appVer204.providers.add(provider1)
    appVer204.device_versions.add(device_ver5)
    appVer204.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer205 = ApplicationVersion.objects.create(
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
        app=app21
    )
    appVer205.providers.add(provider1)
    appVer205.device_versions.add(device_ver5)
    appVer205.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer206 = ApplicationVersion.objects.create(
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
        app=app22
    )
    appVer206.providers.add(provider1)
    appVer206.device_versions.add(device_ver5)
    appVer206.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer207 = ApplicationVersion.objects.create(
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
        app=app24
    )
    appVer207.providers.add(provider1)
    appVer207.device_versions.add(device_ver5)
    appVer207.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer208 = ApplicationVersion.objects.create(
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
    appVer208.providers.add(provider1)
    appVer208.device_versions.add(device_ver5)
    appVer208.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer209 = ApplicationVersion.objects.create(
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
        app=app33
    )
    appVer209.providers.add(provider1)
    appVer209.device_versions.add(device_ver5)
    appVer209.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer210 = ApplicationVersion.objects.create(
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
        app=app28
    )
    appVer210.providers.add(provider1)
    appVer210.device_versions.add(device_ver5)
    appVer210.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer211 = ApplicationVersion.objects.create(
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
        app=app37
    )
    appVer211.providers.add(provider1)
    appVer211.device_versions.add(device_ver5)
    appVer211.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer212 = ApplicationVersion.objects.create(
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
        app=app30
    )
    appVer212.providers.add(provider1)
    appVer212.device_versions.add(device_ver5)
    appVer212.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer213 = ApplicationVersion.objects.create(
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
        app=app26
    )
    appVer213.providers.add(provider1)
    appVer213.device_versions.add(device_ver5)
    appVer213.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer214 = ApplicationVersion.objects.create(
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
        app=app39
    )
    appVer214.providers.add(provider1)
    appVer214.device_versions.add(device_ver5)
    appVer214.se_firmware_final_versions.add(firmware_final_ver2)
    # nanos-1.4 ,
    appVer215 = ApplicationVersion.objects.create(
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
        app=app31
    )
    appVer215.providers.add(provider1)
    appVer215.device_versions.add(device_ver5)
    appVer215.se_firmware_final_versions.add(firmware_final_ver2)
