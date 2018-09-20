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
    provider5 = Provider.objects.create(name="vault")

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
    device_ver5.providers.add(provider1, provider2, provider4)
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
    firmware0.providers.add(provider1, provider4)
    firmware = SeFirmware.objects.create(name="Ledger nano S firmware")
    firmware.providers.add(provider1, provider4)
    firmware2 = SeFirmware.objects.create(name="DAS firmware")
    firmware2.providers.add(provider2)
    firmware3 = SeFirmware.objects.create(name="Bitclub firmware")
    firmware3.providers.add(provider3)
    firmware4 = SeFirmware.objects.create(name="Vault firmware")
    firmware4.providers.add(provider5, provider4)

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
    firmware_final_ver9.providers.add(provider1, provider4)

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
    firmware_final_ver10.providers.add(provider1, provider4)

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
    firmware_final_ver3.providers.add(provider1, provider4)

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

    firmware_final_ver8 = SeFirmwareFinalVersion.objects.create(
        name="2.1.1-ee",
        version=int.from_bytes(bytes([0, 2, 1, 1]), 'big'),
        perso="perso_11",
        firmware="",
        firmware_key="",
        hash="",
        se_firmware=firmware4
    )
    firmware_final_ver8.device_versions.add(device_ver6, device_ver7)
    firmware_final_ver8.providers.add(provider5, provider4)

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
    firmware_osu_ver4.providers.add(provider1, provider4)

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
    app1 = Application.objects.create(name="Bitcoin", category=cat1) 
    app1.providers.add(1,2,3,4) 
    app2 = Application.objects.create(name="Bitcoin Cash", category=cat1) 
    app2.providers.add(1,2) 
    app3 = Application.objects.create(name="Bitcoin Gold", category=cat1) 
    app3.providers.add(1) 
    app4 = Application.objects.create(name="Bitcoin Private", category=cat1) 
    app4.providers.add(1) 
    app5 = Application.objects.create(name="Bitcoin testnet", category=cat2) 
    app5.providers.add(1,4) 
    app6 = Application.objects.create(name="Digibyte", category=cat1) 
    app6.providers.add(1) 
    app7 = Application.objects.create(name="HCash", category=cat1) 
    app7.providers.add(1) 
    app8 = Application.objects.create(name="Qtum", category=cat1) 
    app8.providers.add(1) 
    app9 = Application.objects.create(name="PivX", category=cat1) 
    app9.providers.add(1) 
    app10 = Application.objects.create(name="Stealth", category=cat1) 
    app10.providers.add(1) 
    app11 = Application.objects.create(name="Vertcoin", category=cat1) 
    app11.providers.add(1) 
    app12 = Application.objects.create(name="Peercoin", category=cat1) 
    app12.providers.add(1) 
    app13 = Application.objects.create(name="Viacoin", category=cat1) 
    app13.providers.add(1) 
    app14 = Application.objects.create(name="Ubiq", category=cat1) 
    app14.providers.add(1) 
    app15 = Application.objects.create(name="Expanse", category=cat1) 
    app15.providers.add(1) 
    app16 = Application.objects.create(name="Dash", category=cat1) 
    app16.providers.add(1) 
    app17 = Application.objects.create(name="Dogecoin", category=cat1) 
    app17.providers.add(1) 
    app18 = Application.objects.create(name="Ethereum", category=cat1) 
    app18.providers.add(1,2,3) 
    app19 = Application.objects.create(name="Fido U2F")
    app19.providers.add(1,3) 
    app20 = Application.objects.create(name="Litecoin", category=cat1) 
    app20.providers.add(1) 
    app21 = Application.objects.create(name="Stratis", category=cat1) 
    app21.providers.add(1) 
    app22 = Application.objects.create(name="Ripple", category=cat1) 
    app22.providers.add(1,2) 
    app23 = Application.objects.create(name="Zcash", category=cat1) 
    app23.providers.add(1,3) 
    app24 = Application.objects.create(name="ZenCash", category=cat1) 
    app24.providers.add(1) 
    app25 = Application.objects.create(name="Komodo", category=cat1) 
    app25.providers.add(1) 
    app26 = Application.objects.create(name="PoSW", category=cat1) 
    app26.providers.add(1) 
    app27 = Application.objects.create(name="Stellar", category=cat1) 
    app27.providers.add(1) 
    app28 = Application.objects.create(name="Stealthcoin", category=cat1) 
    app28.providers.add(1) 
    app29 = Application.objects.create(name="Neo", category=cat1) 
    app29.providers.add(1) 
    app30 = Application.objects.create(name="SSH/PGP Agent", category=cat2) 
    app30.providers.add(1) 
    app31 = Application.objects.create(name="Passwords Manager", category=cat2) 
    app31.providers.add(1,4) 
    app32 = Application.objects.create(name="Open PGP", category=cat2) 
    app32.providers.add(1) 
    app33 = Application.objects.create(name="Hello") 
    app33.providers.add(1) 
    app34 = Application.objects.create(name="Ark", category=cat1) 
    app34.providers.add(1) 
    app35 = Application.objects.create(name="Clubcoin", category=cat1) 
    app35.providers.add(3) 
    app36 = Application.objects.create(name="DasCoin", category=cat1) 
    app36.providers.add(2) 
    app37 = Application.objects.create(name="Bitcoin Beta", category=cat2) 
    app37.providers.add(1) 
    app38 = Application.objects.create(name="SSH/GPG Agent", category=cat2) 
    app38.providers.add(1) 
    app39 = Application.objects.create(name="Woleet", category=cat1) 
    app39.providers.add(1) 
    app40 = Application.objects.create(name="Monero", category=cat1) 
    app40.providers.add(1) 
    app41 = Application.objects.create(name="Nano", category=cat1) 
    app41.providers.add(1) 
    app42 = Application.objects.create(name="Nimiq", category=cat1) 
    app42.providers.add(1) 
    app43 = Application.objects.create(name="Tezos Baking", category=cat2) 
    app43.providers.add(1) 
    app44 = Application.objects.create(name="Tezos Wallet", category=cat2) 
    app44.providers.add(1) 
    app45 = Application.objects.create(name="Tron", category=cat1) 
    app45.providers.add(1) 
    app46 = Application.objects.create(name="Zcoin", category=cat1) 
    app46.providers.add(1) 
    app47 = Application.objects.create(name="Dascoin", category=cat1) 
    app47.providers.add(2) 
    app48 = Application.objects.create(name="HODL") 
    app48.providers.add(1) 
    app49 = Application.objects.create(name="Recovery Check") 
    app49.providers.add(1) 
    app50 = Application.objects.create(name="Vault") 
    app50.providers.add(5) 
    app51 = Application.objects.create(name="ICON", category=cat1) 
    app51.providers.add(1) 
    app52 = Application.objects.create(name="kUSD", category=cat1) 
    app52.providers.add(1) 
    app53 = Application.objects.create(name="Ontology", category=cat1) 
    app53.providers.add(1) 
    app54 = Application.objects.create(name="Particl", category=cat1) 
    app54.providers.add(1) 
    app55 = Application.objects.create(name="POA", category=cat1) 
    app55.providers.add(1) 
    app56 = Application.objects.create(name="RSK", category=cat1) 
    app56.providers.add(1) 
    app57 = Application.objects.create(name="VeChain", category=cat1) 
    app57.providers.add(1) 
    app58 = Application.objects.create(name="Wanchain", category=cat1) 
    app58.providers.add(1) 
    app59 = Application.objects.create(name="Ethereum Classic", category=cat1) 
    app59.providers.add(1) 
    app60 = Application.objects.create(name="RSK Test", category=cat2) 
    app60.providers.add(1) 
    app61 = Application.objects.create(name="ICON Test", category=cat2) 
    app61.providers.add(1) 
    app62 = Application.objects.create(name="EOS", category=cat1) 
    app62.providers.add(1,4) 
    app63 = Application.objects.create(name="Lisk", category=cat2) 
    app63.providers.add(1,4) 
    app64 = Application.objects.create(name="FIC", category=cat1) 
    app64.providers.add(1) 
    app65 = Application.objects.create(name="Rise", category=cat1) 
    app65.providers.add(1,4) 
    app66 = Application.objects.create(name="Aion", category=cat2) 
    app66.providers.add(1,4) 
    app67 = Application.objects.create(name="Pirl", category=cat1) 
    app67.providers.add(1,4) 
    app68 = Application.objects.create(name="Waves", category=cat1) 
    app68.providers.add(1,4) 
    app69 = Application.objects.create(name="Hycon", category=cat1) 
    app69.providers.add(1,4) 
    app70 = Application.objects.create(name="Akroma", category=cat1) 
    app70.providers.add(1,4) 
    app71 = Application.objects.create(name="Horizen", category=cat1) 
    app71.providers.add(1,4) 
    app72 = Application.objects.create(name="XRP", category=cat1) 
    app72.providers.add(1,4) 
    # 1 , 
    appVer1 = ApplicationVersion.objects.create(
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
        app_id=1
    )
    appVer1.providers.add(1)
    appVer1.device_versions.add(8)
    appVer1.se_firmware_final_versions.add(4,6)
    # 2 , 
    appVer2 = ApplicationVersion.objects.create(
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
        app_id=2
    )
    appVer2.providers.add(1)
    appVer2.device_versions.add(8)
    appVer2.se_firmware_final_versions.add(4,6)
    # 3 , 
    appVer3 = ApplicationVersion.objects.create(
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
        app_id=3
    )
    appVer3.providers.add(1)
    appVer3.device_versions.add(8)
    appVer3.se_firmware_final_versions.add(4,6)
    # 4 , 
    appVer4 = ApplicationVersion.objects.create(
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
        app_id=4
    )
    appVer4.providers.add(1)
    appVer4.device_versions.add(8)
    appVer4.se_firmware_final_versions.add(4,6)
    # 5 , 
    appVer5 = ApplicationVersion.objects.create(
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
        app_id=5
    )
    appVer5.providers.add(1)
    appVer5.device_versions.add(8)
    appVer5.se_firmware_final_versions.add(4,6)
    # 6 , 
    appVer6 = ApplicationVersion.objects.create(
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
        app_id=6
    )
    appVer6.providers.add(1)
    appVer6.device_versions.add(8)
    appVer6.se_firmware_final_versions.add(4,6)
    # 7 , 
    appVer7 = ApplicationVersion.objects.create(
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
        app_id=7
    )
    appVer7.providers.add(1)
    appVer7.device_versions.add(8)
    appVer7.se_firmware_final_versions.add(4,6)
    # 8 , 
    appVer8 = ApplicationVersion.objects.create(
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
        app_id=8
    )
    appVer8.providers.add(1)
    appVer8.device_versions.add(8)
    appVer8.se_firmware_final_versions.add(4,6)
    # 9 , 
    appVer9 = ApplicationVersion.objects.create(
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
        app_id=9
    )
    appVer9.providers.add(1)
    appVer9.device_versions.add(8)
    appVer9.se_firmware_final_versions.add(4,6)
    # 10 , 
    appVer10 = ApplicationVersion.objects.create(
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
        app_id=10
    )
    appVer10.providers.add(1)
    appVer10.device_versions.add(8)
    appVer10.se_firmware_final_versions.add(4,6)
    # 11 , 
    appVer11 = ApplicationVersion.objects.create(
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
        app_id=11
    )
    appVer11.providers.add(1)
    appVer11.device_versions.add(8)
    appVer11.se_firmware_final_versions.add(4,6)
    # 12 , 
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
        app_id=12
    )
    appVer12.providers.add(1)
    appVer12.device_versions.add(8)
    appVer12.se_firmware_final_versions.add(4,6)
    # 13 , 
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
        app_id=13
    )
    appVer13.providers.add(1)
    appVer13.device_versions.add(8)
    appVer13.se_firmware_final_versions.add(4,6)
    # 14 , 
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
        app_id=14
    )
    appVer14.providers.add(1)
    appVer14.device_versions.add(8)
    appVer14.se_firmware_final_versions.add(4,6)
    # 15 , 
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
        app_id=15
    )
    appVer15.providers.add(1)
    appVer15.device_versions.add(8)
    appVer15.se_firmware_final_versions.add(4,6)
    # 16 , 
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
        app_id=16
    )
    appVer16.providers.add(1)
    appVer16.device_versions.add(8)
    appVer16.se_firmware_final_versions.add(4,6)
    # 17 , 
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
        app_id=17
    )
    appVer17.providers.add(1)
    appVer17.device_versions.add(8)
    appVer17.se_firmware_final_versions.add(4,6)
    # 18 , 
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
        app_id=18
    )
    appVer18.providers.add(1)
    appVer18.device_versions.add(8)
    appVer18.se_firmware_final_versions.add(4,6)
    # 19 , 
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
        app_id=19
    )
    appVer19.providers.add(1)
    appVer19.device_versions.add(8)
    appVer19.se_firmware_final_versions.add(4,6)
    # 20 , 
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
        app_id=20
    )
    appVer20.providers.add(1)
    appVer20.device_versions.add(8)
    appVer20.se_firmware_final_versions.add(4,6)
    # 21 , 
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
        app_id=21
    )
    appVer21.providers.add(1)
    appVer21.device_versions.add(8)
    appVer21.se_firmware_final_versions.add(4,6)
    # 22 , 
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
        app_id=22
    )
    appVer22.providers.add(1)
    appVer22.device_versions.add(8)
    appVer22.se_firmware_final_versions.add(4,6)
    # 23 , 
    appVer23 = ApplicationVersion.objects.create(
        name="Zcash",
        version=66052,
        display_name="Zcash",
        icon="zcash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/zcash/app_latest",
        firmware_key="blue/2.1.0-hw15/zcash/app_latest_key",
        delete="blue/2.1.0-hw15/zcash/app_del",
        delete_key="blue/2.1.0-hw15/zcash/app_del_key",
        app_id=23
    )
    appVer23.providers.add(1)
    appVer23.device_versions.add(8)
    appVer23.se_firmware_final_versions.add(4,6)
    # 24 , 
    appVer24 = ApplicationVersion.objects.create(
        name="ZenCash",
        version=66052,
        display_name="ZenCash",
        icon="zencash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/zencash/app_latest",
        firmware_key="blue/2.1.0-hw15/zencash/app_latest_key",
        delete="blue/2.1.0-hw15/zencash/app_del",
        delete_key="blue/2.1.0-hw15/zencash/app_del_key",
        app_id=24
    )
    appVer24.providers.add(1)
    appVer24.device_versions.add(8)
    appVer24.se_firmware_final_versions.add(4,6)
    # 25 , 
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
        app_id=25
    )
    appVer25.providers.add(1)
    appVer25.device_versions.add(8)
    appVer25.se_firmware_final_versions.add(4,6)
    # 26 , 
    appVer26 = ApplicationVersion.objects.create(
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
        app_id=26
    )
    appVer26.providers.add(1)
    appVer26.device_versions.add(8)
    appVer26.se_firmware_final_versions.add(4,6)
    # 27 , 
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
        app_id=27
    )
    appVer27.providers.add(1)
    appVer27.device_versions.add(8)
    appVer27.se_firmware_final_versions.add(4,6)
    # 28 , 
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
        app_id=1
    )
    appVer28.providers.add(1)
    appVer28.device_versions.add(7)
    appVer28.se_firmware_final_versions.add(3,5)
    # 29 , 
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
        app_id=2
    )
    appVer29.providers.add(1)
    appVer29.device_versions.add(7)
    appVer29.se_firmware_final_versions.add(3,5)
    # 30 , 
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
        app_id=3
    )
    appVer30.providers.add(1)
    appVer30.device_versions.add(7)
    appVer30.se_firmware_final_versions.add(3,5)
    # 31 , 
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
        app_id=4
    )
    appVer31.providers.add(1)
    appVer31.device_versions.add(7)
    appVer31.se_firmware_final_versions.add(3,5)
    # 32 , 
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
        app_id=5
    )
    appVer32.providers.add(1)
    appVer32.device_versions.add(7)
    appVer32.se_firmware_final_versions.add(3,5)
    # 33 , 
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
        app_id=6
    )
    appVer33.providers.add(1)
    appVer33.device_versions.add(7)
    appVer33.se_firmware_final_versions.add(3,5)
    # 34 , 
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
        app_id=7
    )
    appVer34.providers.add(1)
    appVer34.device_versions.add(7)
    appVer34.se_firmware_final_versions.add(3,5)
    # 35 , 
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
        app_id=8
    )
    appVer35.providers.add(1)
    appVer35.device_versions.add(7)
    appVer35.se_firmware_final_versions.add(3,5)
    # 36 , 
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
        app_id=9
    )
    appVer36.providers.add(1)
    appVer36.device_versions.add(7)
    appVer36.se_firmware_final_versions.add(3,5)
    # 37 , 
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
        app_id=10
    )
    appVer37.providers.add(1)
    appVer37.device_versions.add(7)
    appVer37.se_firmware_final_versions.add(3,5)
    # 38 , 
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
        app_id=11
    )
    appVer38.providers.add(1)
    appVer38.device_versions.add(7)
    appVer38.se_firmware_final_versions.add(3,5)
    # 39 , 
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
        app_id=12
    )
    appVer39.providers.add(1)
    appVer39.device_versions.add(7)
    appVer39.se_firmware_final_versions.add(3,5)
    # 40 , 
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
        app_id=13
    )
    appVer40.providers.add(1)
    appVer40.device_versions.add(7)
    appVer40.se_firmware_final_versions.add(3,5)
    # 41 , 
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
        app_id=14
    )
    appVer41.providers.add(1)
    appVer41.device_versions.add(7)
    appVer41.se_firmware_final_versions.add(3,5)
    # 42 , 
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
        app_id=15
    )
    appVer42.providers.add(1)
    appVer42.device_versions.add(7)
    appVer42.se_firmware_final_versions.add(3,5)
    # 43 , 
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
        app_id=16
    )
    appVer43.providers.add(1)
    appVer43.device_versions.add(7)
    appVer43.se_firmware_final_versions.add(3,5)
    # 44 , 
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
        app_id=17
    )
    appVer44.providers.add(1)
    appVer44.device_versions.add(7)
    appVer44.se_firmware_final_versions.add(3,5)
    # 45 , 
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
        app_id=18
    )
    appVer45.providers.add(1)
    appVer45.device_versions.add(7)
    appVer45.se_firmware_final_versions.add(3,5)
    # 46 , 
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
        app_id=19
    )
    appVer46.providers.add(1)
    appVer46.device_versions.add(7)
    appVer46.se_firmware_final_versions.add(3,5)
    # 47 , 
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
        app_id=20
    )
    appVer47.providers.add(1)
    appVer47.device_versions.add(7)
    appVer47.se_firmware_final_versions.add(3,5)
    # 48 , 
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
        app_id=21
    )
    appVer48.providers.add(1)
    appVer48.device_versions.add(7)
    appVer48.se_firmware_final_versions.add(3,5)
    # 49 , 
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
        app_id=22
    )
    appVer49.providers.add(1)
    appVer49.device_versions.add(7)
    appVer49.se_firmware_final_versions.add(3,5)
    # 50 , 
    appVer50 = ApplicationVersion.objects.create(
        name="Zcash",
        version=66052,
        display_name="Zcash",
        icon="zcash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/zcash/app_latest",
        firmware_key="blue/2.1.0-hw15/zcash/app_latest_key",
        delete="blue/2.1.0-hw15/zcash/app_del",
        delete_key="blue/2.1.0-hw15/zcash/app_del_key",
        app_id=23
    )
    appVer50.providers.add(1)
    appVer50.device_versions.add(7)
    appVer50.se_firmware_final_versions.add(3,5)
    # 51 , 
    appVer51 = ApplicationVersion.objects.create(
        name="ZenCash",
        version=66052,
        display_name="ZenCash",
        icon="zencash",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/zencash/app_latest",
        firmware_key="blue/2.1.0-hw15/zencash/app_latest_key",
        delete="blue/2.1.0-hw15/zencash/app_del",
        delete_key="blue/2.1.0-hw15/zencash/app_del_key",
        app_id=24
    )
    appVer51.providers.add(1)
    appVer51.device_versions.add(7)
    appVer51.se_firmware_final_versions.add(3,5)
    # 52 , 
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
        app_id=25
    )
    appVer52.providers.add(1)
    appVer52.device_versions.add(7)
    appVer52.se_firmware_final_versions.add(3,5)
    # 53 , 
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
        app_id=26
    )
    appVer53.providers.add(1)
    appVer53.device_versions.add(7)
    appVer53.se_firmware_final_versions.add(3,5)
    # 54 , 
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
        app_id=27
    )
    appVer54.providers.add(1)
    appVer54.device_versions.add(7)
    appVer54.se_firmware_final_versions.add(3,5)
    # 55 , 
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
        app_id=1
    )
    appVer55.providers.add(1)
    appVer55.device_versions.add(3)
    appVer55.se_firmware_final_versions.add(1,2)
    # 56 , 
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
        app_id=2
    )
    appVer56.providers.add(1)
    appVer56.device_versions.add(3)
    appVer56.se_firmware_final_versions.add(1,2)
    # 57 , 
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
        app_id=16
    )
    appVer57.providers.add(1)
    appVer57.device_versions.add(3)
    appVer57.se_firmware_final_versions.add(1,2)
    # 58 , 
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
        app_id=17
    )
    appVer58.providers.add(1)
    appVer58.device_versions.add(3)
    appVer58.se_firmware_final_versions.add(1,2)
    # 59 , 
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
        app_id=18
    )
    appVer59.providers.add(1)
    appVer59.device_versions.add(3)
    appVer59.se_firmware_final_versions.add(1,2)
    # 60 , 
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
        app_id=20
    )
    appVer60.providers.add(1)
    appVer60.device_versions.add(3)
    appVer60.se_firmware_final_versions.add(1,2)
    # 61 , 
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
        app_id=21
    )
    appVer61.providers.add(1)
    appVer61.device_versions.add(3)
    appVer61.se_firmware_final_versions.add(1,2)
    # 62 , 
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
        app_id=23
    )
    appVer62.providers.add(1)
    appVer62.device_versions.add(3)
    appVer62.se_firmware_final_versions.add(1,2)
    # 63 , 
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
        app_id=22
    )
    appVer63.providers.add(1)
    appVer63.device_versions.add(3)
    appVer63.se_firmware_final_versions.add(1,2)
    # 64 , 
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
        app_id=26
    )
    appVer64.providers.add(1)
    appVer64.device_versions.add(3)
    appVer64.se_firmware_final_versions.add(1,2)
    # 65 , 
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
        app_id=14
    )
    appVer65.providers.add(1)
    appVer65.device_versions.add(3)
    appVer65.se_firmware_final_versions.add(1,2)
    # 66 , 
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
        app_id=15
    )
    appVer66.providers.add(1)
    appVer66.device_versions.add(3)
    appVer66.se_firmware_final_versions.add(1,2)
    # 67 , 
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
        app_id=9
    )
    appVer67.providers.add(1)
    appVer67.device_versions.add(3)
    appVer67.se_firmware_final_versions.add(1,2)
    # 68 , 
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
        app_id=28
    )
    appVer68.providers.add(1)
    appVer68.device_versions.add(3)
    appVer68.se_firmware_final_versions.add(1,2)
    # 69 , 
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
        app_id=11
    )
    appVer69.providers.add(1)
    appVer69.device_versions.add(3)
    appVer69.se_firmware_final_versions.add(1,2)
    # 70 , 
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
        app_id=13
    )
    appVer70.providers.add(1)
    appVer70.device_versions.add(3)
    appVer70.se_firmware_final_versions.add(1,2)
    # 71 , 
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
        app_id=25
    )
    appVer71.providers.add(1)
    appVer71.device_versions.add(3)
    appVer71.se_firmware_final_versions.add(1,2)
    # 72 , 
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
        app_id=3
    )
    appVer72.providers.add(1)
    appVer72.device_versions.add(3)
    appVer72.se_firmware_final_versions.add(1,2)
    # 73 , 
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
        app_id=6
    )
    appVer73.providers.add(1)
    appVer73.device_versions.add(3)
    appVer73.se_firmware_final_versions.add(1,2)
    # 74 , 
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
        app_id=7
    )
    appVer74.providers.add(1)
    appVer74.device_versions.add(3)
    appVer74.se_firmware_final_versions.add(1,2)
    # 75 , 
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
        app_id=8
    )
    appVer75.providers.add(1)
    appVer75.device_versions.add(3)
    appVer75.se_firmware_final_versions.add(1,2)
    # 76 , 
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
        app_id=29
    )
    appVer76.providers.add(1)
    appVer76.device_versions.add(3)
    appVer76.se_firmware_final_versions.add(1,2)
    # 77 , 
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
        app_id=27
    )
    appVer77.providers.add(1)
    appVer77.device_versions.add(3)
    appVer77.se_firmware_final_versions.add(1,2)
    # 78 , 
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
        app_id=1
    )
    appVer78.providers.add(1)
    appVer78.device_versions.add(2)
    appVer78.se_firmware_final_versions.add(7)
    # 79 , 
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
        app_id=2
    )
    appVer79.providers.add(1)
    appVer79.device_versions.add(2)
    appVer79.se_firmware_final_versions.add(7)
    # 80 , 
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
        app_id=16
    )
    appVer80.providers.add(1)
    appVer80.device_versions.add(2)
    appVer80.se_firmware_final_versions.add(7)
    # 81 , 
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
        app_id=17
    )
    appVer81.providers.add(1)
    appVer81.device_versions.add(2)
    appVer81.se_firmware_final_versions.add(7)
    # 82 , 
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
        app_id=18
    )
    appVer82.providers.add(1)
    appVer82.device_versions.add(2)
    appVer82.se_firmware_final_versions.add(7)
    # 83 , 
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
        app_id=19
    )
    appVer83.providers.add(1)
    appVer83.device_versions.add(2)
    appVer83.se_firmware_final_versions.add(7)
    # 84 , 
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
        app_id=25
    )
    appVer84.providers.add(1)
    appVer84.device_versions.add(2)
    appVer84.se_firmware_final_versions.add(7)
    # 85 , 
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
        app_id=20
    )
    appVer85.providers.add(1)
    appVer85.device_versions.add(2)
    appVer85.se_firmware_final_versions.add(7)
    # 86 , 
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
        app_id=21
    )
    appVer86.providers.add(1)
    appVer86.device_versions.add(2)
    appVer86.se_firmware_final_versions.add(7)
    # 87 , 
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
        app_id=23
    )
    appVer87.providers.add(1)
    appVer87.device_versions.add(2)
    appVer87.se_firmware_final_versions.add(7)
    # 88 , 
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
        app_id=30
    )
    appVer88.providers.add(1)
    appVer88.device_versions.add(2)
    appVer88.se_firmware_final_versions.add(7)
    # 89 , 
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
        app_id=31
    )
    appVer89.providers.add(1)
    appVer89.device_versions.add(2)
    appVer89.se_firmware_final_versions.add(7)
    # 90 , 
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
        app_id=32
    )
    appVer90.providers.add(1)
    appVer90.device_versions.add(2)
    appVer90.se_firmware_final_versions.add(7)
    # 91 , 
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
        app_id=33
    )
    appVer91.providers.add(1)
    appVer91.device_versions.add(2)
    appVer91.se_firmware_final_versions.add(7)
    # 92 , 
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
        app_id=22
    )
    appVer92.providers.add(1)
    appVer92.device_versions.add(2)
    appVer92.se_firmware_final_versions.add(7)
    # 93 , 
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
        app_id=26
    )
    appVer93.providers.add(1)
    appVer93.device_versions.add(2)
    appVer93.se_firmware_final_versions.add(7)
    # 94 , 
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
        app_id=34
    )
    appVer94.providers.add(1)
    appVer94.device_versions.add(2)
    appVer94.se_firmware_final_versions.add(7)
    # 95 , 
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
        app_id=14
    )
    appVer95.providers.add(1)
    appVer95.device_versions.add(2)
    appVer95.se_firmware_final_versions.add(7)
    # 96 , 
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
        app_id=15
    )
    appVer96.providers.add(1)
    appVer96.device_versions.add(2)
    appVer96.se_firmware_final_versions.add(7)
    # 97 , 
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
        app_id=9
    )
    appVer97.providers.add(1)
    appVer97.device_versions.add(2)
    appVer97.se_firmware_final_versions.add(7)
    # 98 , 
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
        app_id=28
    )
    appVer98.providers.add(1)
    appVer98.device_versions.add(2)
    appVer98.se_firmware_final_versions.add(7)
    # 99 , 
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
        app_id=11
    )
    appVer99.providers.add(1)
    appVer99.device_versions.add(2)
    appVer99.se_firmware_final_versions.add(7)
    # 100 , 
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
        app_id=13
    )
    appVer100.providers.add(1)
    appVer100.device_versions.add(2)
    appVer100.se_firmware_final_versions.add(7)
    # 101 , 
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
        app_id=5
    )
    appVer101.providers.add(1)
    appVer101.device_versions.add(2)
    appVer101.se_firmware_final_versions.add(7)
    # 102 , 
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
        app_id=29
    )
    appVer102.providers.add(1)
    appVer102.device_versions.add(2)
    appVer102.se_firmware_final_versions.add(7)
    # 103 , 
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
        app_id=3
    )
    appVer103.providers.add(1)
    appVer103.device_versions.add(2)
    appVer103.se_firmware_final_versions.add(7)
    # 104 , 
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
        app_id=27
    )
    appVer104.providers.add(1)
    appVer104.device_versions.add(2)
    appVer104.se_firmware_final_versions.add(7)
    # 105 , 
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
        app_id=6
    )
    appVer105.providers.add(1)
    appVer105.device_versions.add(2)
    appVer105.se_firmware_final_versions.add(7)
    # 106 , 
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
        app_id=7
    )
    appVer106.providers.add(1)
    appVer106.device_versions.add(2)
    appVer106.se_firmware_final_versions.add(7)
    # 107 , 
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
        app_id=8
    )
    appVer107.providers.add(1)
    appVer107.device_versions.add(2)
    appVer107.se_firmware_final_versions.add(7)
    # 108 , 
    appVer108 = ApplicationVersion.objects.create(
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
        app_id=1
    )
    appVer108.providers.add(3)
    appVer108.device_versions.add(2)
    appVer108.se_firmware_final_versions.add(7)
    # 109 , 
    appVer109 = ApplicationVersion.objects.create(
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
        app_id=18
    )
    appVer109.providers.add(3)
    appVer109.device_versions.add(2)
    appVer109.se_firmware_final_versions.add(7)
    # 110 , 
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
        app_id=35
    )
    appVer110.providers.add(3)
    appVer110.device_versions.add(2)
    appVer110.se_firmware_final_versions.add(firmware_final_ver7)
    # 111 , 
    appVer111 = ApplicationVersion.objects.create(
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
        app_id=23
    )
    appVer111.providers.add(3)
    appVer111.device_versions.add(2)
    appVer111.se_firmware_final_versions.add(7)
    # 112 , 
    appVer112 = ApplicationVersion.objects.create(
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
        app_id=19
    )
    appVer112.providers.add(3)
    appVer112.device_versions.add(2)
    appVer112.se_firmware_final_versions.add(7)
    # 113 , 
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
        app_id=1
    )
    appVer113.providers.add(2)
    appVer113.device_versions.add(2)
    appVer113.se_firmware_final_versions.add(7)
    # 114 , 
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
        app_id=2
    )
    appVer114.providers.add(2)
    appVer114.device_versions.add(2)
    appVer114.se_firmware_final_versions.add(7)
    # 115 , 
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
        app_id=18
    )
    appVer115.providers.add(2)
    appVer115.device_versions.add(2)
    appVer115.se_firmware_final_versions.add(7)
    # 116 , 
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
        app_id=22
    )
    appVer116.providers.add(2)
    appVer116.device_versions.add(2)
    appVer116.se_firmware_final_versions.add(7)
    # 117 , 
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
        app_id=36
    )
    appVer117.providers.add(2)
    appVer117.device_versions.add(2)
    appVer117.se_firmware_final_versions.add(7)
    # 118 , 
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
        app_id=1
    )
    appVer118.providers.add(1)
    appVer118.device_versions.add(2)
    appVer118.se_firmware_final_versions.add(7)
    # 119 , 
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
        app_id=16
    )
    appVer119.providers.add(1)
    appVer119.device_versions.add(2)
    appVer119.se_firmware_final_versions.add(7)
    # 120 , 
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
        app_id=17
    )
    appVer120.providers.add(1)
    appVer120.device_versions.add(2)
    appVer120.se_firmware_final_versions.add(7)
    # 121 , 
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
        app_id=18
    )
    appVer121.providers.add(1)
    appVer121.device_versions.add(2)
    appVer121.se_firmware_final_versions.add(7)
    # 122 , 
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
        app_id=20
    )
    appVer122.providers.add(1)
    appVer122.device_versions.add(2)
    appVer122.se_firmware_final_versions.add(7)
    # 123 , 
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
        app_id=21
    )
    appVer123.providers.add(1)
    appVer123.device_versions.add(2)
    appVer123.se_firmware_final_versions.add(7)
    # 124 , 
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
        app_id=23
    )
    appVer124.providers.add(1)
    appVer124.device_versions.add(2)
    appVer124.se_firmware_final_versions.add(7)
    # 125 , 
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
        app_id=30
    )
    appVer125.providers.add(1)
    appVer125.device_versions.add(2)
    appVer125.se_firmware_final_versions.add(7)
    # 126 , 
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
        app_id=1
    )
    appVer126.providers.add(1)
    appVer126.device_versions.add(2)
    appVer126.se_firmware_final_versions.add(8)
    # 127 , 
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
        app_id=37
    )
    appVer127.providers.add(1)
    appVer127.device_versions.add(2)
    appVer127.se_firmware_final_versions.add(8)
    # 128 , 
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
        app_id=16
    )
    appVer128.providers.add(1)
    appVer128.device_versions.add(2)
    appVer128.se_firmware_final_versions.add(8)
    # 129 , 
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
        app_id=17
    )
    appVer129.providers.add(1)
    appVer129.device_versions.add(2)
    appVer129.se_firmware_final_versions.add(8)
    # 130 , 
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
        app_id=18
    )
    appVer130.providers.add(1)
    appVer130.device_versions.add(2)
    appVer130.se_firmware_final_versions.add(8)
    # 131 , 
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
        app_id=20
    )
    appVer131.providers.add(1)
    appVer131.device_versions.add(2)
    appVer131.se_firmware_final_versions.add(8)
    # 132 , 
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
        app_id=30
    )
    appVer132.providers.add(1)
    appVer132.device_versions.add(2)
    appVer132.se_firmware_final_versions.add(8)
    # 133 , 
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
        app_id=21
    )
    appVer133.providers.add(1)
    appVer133.device_versions.add(2)
    appVer133.se_firmware_final_versions.add(8)
    # 134 , 
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
        app_id=23
    )
    appVer134.providers.add(1)
    appVer134.device_versions.add(2)
    appVer134.se_firmware_final_versions.add(8)
    # 135 , 
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
        app_id=1
    )
    appVer135.providers.add(1)
    appVer135.device_versions.add(2)
    appVer135.se_firmware_final_versions.add(7)
    # 136 , 
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
        app_id=18
    )
    appVer136.providers.add(1)
    appVer136.device_versions.add(2)
    appVer136.se_firmware_final_versions.add(7)
    # 137 , 
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
        app_id=19
    )
    appVer137.providers.add(1)
    appVer137.device_versions.add(2)
    appVer137.se_firmware_final_versions.add(7)
    # 138 , 
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
        app_id=20
    )
    appVer138.providers.add(1)
    appVer138.device_versions.add(2)
    appVer138.se_firmware_final_versions.add(7)
    # 139 , 
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
        app_id=30
    )
    appVer139.providers.add(1)
    appVer139.device_versions.add(2)
    appVer139.se_firmware_final_versions.add(7)
    # 140 , 
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
        app_id=1
    )
    appVer140.providers.add(1)
    appVer140.device_versions.add(6)
    appVer140.se_firmware_final_versions.add(10)
    # 141 , 
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
        app_id=2
    )
    appVer141.providers.add(1)
    appVer141.device_versions.add(6)
    appVer141.se_firmware_final_versions.add(10)
    # 142 , 
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
        app_id=3
    )
    appVer142.providers.add(1)
    appVer142.device_versions.add(6)
    appVer142.se_firmware_final_versions.add(10)
    # 143 , 
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
        app_id=4
    )
    appVer143.providers.add(1)
    appVer143.device_versions.add(6)
    appVer143.se_firmware_final_versions.add(10)
    # 144 , 
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
        app_id=5
    )
    appVer144.providers.add(1)
    appVer144.device_versions.add(6)
    appVer144.se_firmware_final_versions.add(10)
    # 145 , 
    appVer145 = ApplicationVersion.objects.create(
        name="DigiByte",
        version=66056,
        display_name="DigiByte",
        icon="digibyte",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/digibyte/app_1.2.8",
        firmware_key="nanos/1.4.2/digibyte/app_1.2.8_key",
        delete="nanos/1.4.2/digibyte/app_del",
        delete_key="nanos/1.4.2/digibyte/app_del_key",
        app_id=6
    )
    appVer145.providers.add(1)
    appVer145.device_versions.add(6)
    appVer145.se_firmware_final_versions.add(10)
    # 146 , 
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
        app_id=7
    )
    appVer146.providers.add(1)
    appVer146.device_versions.add(6)
    appVer146.se_firmware_final_versions.add(10)
    # 147 , 
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
        app_id=8
    )
    appVer147.providers.add(1)
    appVer147.device_versions.add(6)
    appVer147.se_firmware_final_versions.add(10)
    # 148 , 
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
        app_id=9
    )
    appVer148.providers.add(1)
    appVer148.device_versions.add(6)
    appVer148.se_firmware_final_versions.add(10)
    # 149 , 
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
        app_id=10
    )
    appVer149.providers.add(1)
    appVer149.device_versions.add(6)
    appVer149.se_firmware_final_versions.add(10)
    # 150 , 
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
        app_id=11
    )
    appVer150.providers.add(1)
    appVer150.device_versions.add(6)
    appVer150.se_firmware_final_versions.add(10)
    # 151 , 
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
        app_id=13
    )
    appVer151.providers.add(1)
    appVer151.device_versions.add(6)
    appVer151.se_firmware_final_versions.add(10)
    # 152 , 
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
        app_id=14
    )
    appVer152.providers.add(1)
    appVer152.device_versions.add(6)
    appVer152.se_firmware_final_versions.add(10)
    # 153 , 
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
        app_id=15
    )
    appVer153.providers.add(1)
    appVer153.device_versions.add(6)
    appVer153.se_firmware_final_versions.add(10)
    # 154 , 
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
        app_id=16
    )
    appVer154.providers.add(1)
    appVer154.device_versions.add(6)
    appVer154.se_firmware_final_versions.add(10)
    # 155 , 
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
        app_id=17
    )
    appVer155.providers.add(1)
    appVer155.device_versions.add(6)
    appVer155.se_firmware_final_versions.add(10)
    # 156 , 
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
        app_id=18
    )
    appVer156.providers.add(1)
    appVer156.device_versions.add(6)
    appVer156.se_firmware_final_versions.add(10)
    # 157 , 
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
        app_id=19
    )
    appVer157.providers.add(1)
    appVer157.device_versions.add(6)
    appVer157.se_firmware_final_versions.add(10)
    # 158 , 
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
        app_id=20
    )
    appVer158.providers.add(1)
    appVer158.device_versions.add(6)
    appVer158.se_firmware_final_versions.add(10)
    # 159 , 
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
        app_id=21
    )
    appVer159.providers.add(1)
    appVer159.device_versions.add(6)
    appVer159.se_firmware_final_versions.add(10)
    # 160 , 
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
        app_id=22
    )
    appVer160.providers.add(1)
    appVer160.device_versions.add(6)
    appVer160.se_firmware_final_versions.add(10)
    # 161 , 
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
        app_id=23
    )
    appVer161.providers.add(1)
    appVer161.device_versions.add(6)
    appVer161.se_firmware_final_versions.add(10)
    # 162 , 
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
        app_id=24
    )
    appVer162.providers.add(1)
    appVer162.device_versions.add(6)
    appVer162.se_firmware_final_versions.add(10)
    # 163 , 
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
        app_id=25
    )
    appVer163.providers.add(1)
    appVer163.device_versions.add(6)
    appVer163.se_firmware_final_versions.add(10)
    # 164 , 
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
        app_id=12
    )
    appVer164.providers.add(1)
    appVer164.device_versions.add(6)
    appVer164.se_firmware_final_versions.add(10)
    # 165 , 
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
        app_id=26
    )
    appVer165.providers.add(1)
    appVer165.device_versions.add(6)
    appVer165.se_firmware_final_versions.add(10)
    # 166 , 
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
        app_id=34
    )
    appVer166.providers.add(1)
    appVer166.device_versions.add(6)
    appVer166.se_firmware_final_versions.add(10)
    # 167 , 
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
        app_id=29
    )
    appVer167.providers.add(1)
    appVer167.device_versions.add(6)
    appVer167.se_firmware_final_versions.add(10)
    # 168 , 
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
        app_id=38
    )
    appVer168.providers.add(1)
    appVer168.device_versions.add(6)
    appVer168.se_firmware_final_versions.add(10)
    # 169 , 
    appVer169 = ApplicationVersion.objects.create(
        name="Passwords Manager",
        version=4,
        display_name="Passwords Manager",
        icon="passwords",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/pwmgr/app_0.0.4",
        firmware_key="nanos/1.4.2/pwmgr/app_0.0.4_key",
        delete="nanos/1.4.2/pwmgr/app_del",
        delete_key="nanos/1.4.2/pwmgr/app_del_key",
        app_id=31
    )
    appVer169.providers.add(1)
    appVer169.device_versions.add(6)
    appVer169.se_firmware_final_versions.add(10)
    # 170 , 
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
        app_id=27
    )
    appVer170.providers.add(1)
    appVer170.device_versions.add(6)
    appVer170.se_firmware_final_versions.add(10)
    # 171 , 
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
        app_id=39
    )
    appVer171.providers.add(1)
    appVer171.device_versions.add(6)
    appVer171.se_firmware_final_versions.add(10)
    # 172 , 
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
        app_id=40
    )
    appVer172.providers.add(1)
    appVer172.device_versions.add(6)
    appVer172.se_firmware_final_versions.add(10)
    # 173 , 
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
        app_id=33
    )
    appVer173.providers.add(1)
    appVer173.device_versions.add(6)
    appVer173.se_firmware_final_versions.add(10)
    # 174 , 
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
        app_id=32
    )
    appVer174.providers.add(1)
    appVer174.device_versions.add(6)
    appVer174.se_firmware_final_versions.add(10)
    # 175 , 
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
        app_id=41
    )
    appVer175.providers.add(1)
    appVer175.device_versions.add(6)
    appVer175.se_firmware_final_versions.add(10)
    # 176 , 
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
        app_id=42
    )
    appVer176.providers.add(1)
    appVer176.device_versions.add(6)
    appVer176.se_firmware_final_versions.add(10)
    # 177 , 
    appVer177 = ApplicationVersion.objects.create(
        name="Tezos Baking",
        version=65536,
        display_name="Tezos Baking",
        icon="tezos_baking",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/tezos_baking/app_1.0.0",
        firmware_key="nanos/1.4.2/tezos_baking/app_1.0.0_key",
        delete="nanos/1.4.2/tezos_baking/app_1.0.0_del",
        delete_key="nanos/1.4.2/tezos_baking/app_1.0.0_del_key",
        app_id=43
    )
    appVer177.providers.add(1)
    appVer177.device_versions.add(6)
    appVer177.se_firmware_final_versions.add(10)
    # 178 , 
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
        app_id=44
    )
    appVer178.providers.add(1)
    appVer178.device_versions.add(6)
    appVer178.se_firmware_final_versions.add(10)
    # 179 , 
    appVer179 = ApplicationVersion.objects.create(
        name="Tron",
        version=2,
        display_name="Tron",
        icon="tron",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/tron/app_latest",
        firmware_key="nanos/1.4.2/tron/app_latest_key",
        delete="nanos/1.4.2/tron/app_del",
        delete_key="nanos/1.4.2/tron/app_del_key",
        app_id=45
    )
    appVer179.providers.add(1)
    appVer179.device_versions.add(6)
    appVer179.se_firmware_final_versions.add(10)
    # 180 , 
    appVer180 = ApplicationVersion.objects.create(
        name="Zcoin",
        version=66056,
        display_name="Zcoin",
        icon="zcoin",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.2/zcoin/app_1.2.8",
        firmware_key="nanos/1.4.2/zcoin/app_1.2.8_key",
        delete="nanos/1.4.2/zcoin/app_del",
        delete_key="nanos/1.4.2/zcoin/app_del_key",
        app_id=46
    )
    appVer180.providers.add(1)
    appVer180.device_versions.add(6)
    appVer180.se_firmware_final_versions.add(10)
    # 181 , 
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
        app_id=47
    )
    appVer181.providers.add(2)
    appVer181.device_versions.add(6)
    appVer181.se_firmware_final_versions.add(10)
    # 182 , 
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
        app_id=1
    )
    appVer182.providers.add(2)
    appVer182.device_versions.add(6)
    appVer182.se_firmware_final_versions.add(10)
    # 183 , 
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
        app_id=2
    )
    appVer183.providers.add(2)
    appVer183.device_versions.add(6)
    appVer183.se_firmware_final_versions.add(10)
    # 184 , 
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
        app_id=18
    )
    appVer184.providers.add(2)
    appVer184.device_versions.add(6)
    appVer184.se_firmware_final_versions.add(10)
    # 185 , 
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
        app_id=22
    )
    appVer185.providers.add(2)
    appVer185.device_versions.add(6)
    appVer185.se_firmware_final_versions.add(10)
    # 186 , 
    appVer186 = ApplicationVersion.objects.create(
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
        app_id=1
    )
    appVer186.providers.add(1)
    appVer186.device_versions.add(6)
    appVer186.se_firmware_final_versions.add(9)
    # 187 , 
    appVer187 = ApplicationVersion.objects.create(
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
        app_id=2
    )
    appVer187.providers.add(1)
    appVer187.device_versions.add(6)
    appVer187.se_firmware_final_versions.add(9)
    # 188 , 
    appVer188 = ApplicationVersion.objects.create(
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
        app_id=3
    )
    appVer188.providers.add(1)
    appVer188.device_versions.add(6)
    appVer188.se_firmware_final_versions.add(9)
    # 189 , 
    appVer189 = ApplicationVersion.objects.create(
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
        app_id=5
    )
    appVer189.providers.add(1)
    appVer189.device_versions.add(6)
    appVer189.se_firmware_final_versions.add(9)
    # 190 , 
    appVer190 = ApplicationVersion.objects.create(
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
        app_id=6
    )
    appVer190.providers.add(1)
    appVer190.device_versions.add(6)
    appVer190.se_firmware_final_versions.add(9)
    # 191 , 
    appVer191 = ApplicationVersion.objects.create(
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
        app_id=7
    )
    appVer191.providers.add(1)
    appVer191.device_versions.add(6)
    appVer191.se_firmware_final_versions.add(9)
    # 192 , 
    appVer192 = ApplicationVersion.objects.create(
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
        app_id=8
    )
    appVer192.providers.add(1)
    appVer192.device_versions.add(6)
    appVer192.se_firmware_final_versions.add(9)
    # 193 , 
    appVer193 = ApplicationVersion.objects.create(
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
        app_id=9
    )
    appVer193.providers.add(1)
    appVer193.device_versions.add(6)
    appVer193.se_firmware_final_versions.add(9)
    # 194 , 
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
        app_id=28
    )
    appVer194.providers.add(1)
    appVer194.device_versions.add(6)
    appVer194.se_firmware_final_versions.add(9)
    # 195 , 
    appVer195 = ApplicationVersion.objects.create(
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
        app_id=11
    )
    appVer195.providers.add(1)
    appVer195.device_versions.add(6)
    appVer195.se_firmware_final_versions.add(9)
    # 196 , 
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
        app_id=13
    )
    appVer196.providers.add(1)
    appVer196.device_versions.add(6)
    appVer196.se_firmware_final_versions.add(9)
    # 197 , 
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
        app_id=14
    )
    appVer197.providers.add(1)
    appVer197.device_versions.add(6)
    appVer197.se_firmware_final_versions.add(9)
    # 198 , 
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
        app_id=15
    )
    appVer198.providers.add(1)
    appVer198.device_versions.add(6)
    appVer198.se_firmware_final_versions.add(9)
    # 199 , 
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
        app_id=16
    )
    appVer199.providers.add(1)
    appVer199.device_versions.add(6)
    appVer199.se_firmware_final_versions.add(9)
    # 200 , 
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
        app_id=17
    )
    appVer200.providers.add(1)
    appVer200.device_versions.add(6)
    appVer200.se_firmware_final_versions.add(9)
    # 201 , 
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
        app_id=18
    )
    appVer201.providers.add(1)
    appVer201.device_versions.add(6)
    appVer201.se_firmware_final_versions.add(9)
    # 202 , 
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
        app_id=19
    )
    appVer202.providers.add(1)
    appVer202.device_versions.add(6)
    appVer202.se_firmware_final_versions.add(9)
    # 203 , 
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
        app_id=20
    )
    appVer203.providers.add(1)
    appVer203.device_versions.add(6)
    appVer203.se_firmware_final_versions.add(9)
    # 204 , 
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
        app_id=21
    )
    appVer204.providers.add(1)
    appVer204.device_versions.add(6)
    appVer204.se_firmware_final_versions.add(9)
    # 205 , 
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
        app_id=22
    )
    appVer205.providers.add(1)
    appVer205.device_versions.add(6)
    appVer205.se_firmware_final_versions.add(9)
    # 206 , 
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
        app_id=23
    )
    appVer206.providers.add(1)
    appVer206.device_versions.add(6)
    appVer206.se_firmware_final_versions.add(9)
    # 207 , 
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
        app_id=25
    )
    appVer207.providers.add(1)
    appVer207.device_versions.add(6)
    appVer207.se_firmware_final_versions.add(9)
    # 208 , 
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
        app_id=26
    )
    appVer208.providers.add(1)
    appVer208.device_versions.add(6)
    appVer208.se_firmware_final_versions.add(9)
    # 209 , 
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
        app_id=34
    )
    appVer209.providers.add(1)
    appVer209.device_versions.add(6)
    appVer209.se_firmware_final_versions.add(9)
    # 210 , 
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
        app_id=29
    )
    appVer210.providers.add(1)
    appVer210.device_versions.add(6)
    appVer210.se_firmware_final_versions.add(9)
    # 211 , 
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
        app_id=38
    )
    appVer211.providers.add(1)
    appVer211.device_versions.add(6)
    appVer211.se_firmware_final_versions.add(9)
    # 212 , 
    appVer212 = ApplicationVersion.objects.create(
        name="Passwords Manager",
        version=3,
        display_name="Passwords Manager",
        icon="passwords",
        hash="0000000000000000000000000000000000000000000000000000000000000000",
        perso="perso_11",
        firmware="nanos/1.4.1/pwmgr/app_0.0.3",
        firmware_key="nanos/1.4.1/pwmgr/app_0.0.3_key",
        delete="nanos/1.4.1/pwmgr/app_del",
        delete_key="nanos/1.4.1/pwmgr/app_del_key",
        app_id=31
    )
    appVer212.providers.add(1)
    appVer212.device_versions.add(6)
    appVer212.se_firmware_final_versions.add(9)
    # 213 , 
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
        app_id=27
    )
    appVer213.providers.add(1)
    appVer213.device_versions.add(6)
    appVer213.se_firmware_final_versions.add(9)
    # 214 , 
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
        app_id=40
    )
    appVer214.providers.add(1)
    appVer214.device_versions.add(6)
    appVer214.se_firmware_final_versions.add(9)
    # 215 , 
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
        app_id=32
    )
    appVer215.providers.add(1)
    appVer215.device_versions.add(6)
    appVer215.se_firmware_final_versions.add(9)
    # 216 , 
    appVer216 = ApplicationVersion.objects.create(
        name="Ubiq",
        version=65794,
        display_name="Ubiq",
        icon="ubiq",
        hash="none",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/ubiq/app_1.1.2",
        firmware_key="blue/2.1.0-hw15/ubiq/app_1.1.2_key",
        delete="blue/2.1.0-hw15/ubiq/app_del",
        delete_key="blue/2.1.0-hw15/ubiq/app_del_key",
        app_id=14
    )
    appVer216.providers.add(1)
    appVer216.device_versions.add(7,8)
    appVer216.se_firmware_final_versions.add(3,4,5,6)
    # 217 , 
    appVer217 = ApplicationVersion.objects.create(
        name="Expanse",
        version=65794,
        display_name="Expanse",
        icon="expanse",
        hash="none",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/expanse/app_1.1.2",
        firmware_key="blue/2.1.0-hw15/expanse/app_1.1.2_key",
        delete="blue/2.1.0-hw15/expanse/app_del",
        delete_key="blue/2.1.0-hw15/expanse/app_del_key",
        app_id=15
    )
    appVer217.providers.add(1)
    appVer217.device_versions.add(7,8)
    appVer217.se_firmware_final_versions.add(3,4,5,6)
    # 218 , 
    appVer218 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65794,
        display_name="Ethereum",
        icon="ethereum",
        hash="none",
        perso="perso_11",
        firmware="blue/2.1.0-hw15/ethereum/app_1.1.2",
        firmware_key="blue/2.1.0-hw15/ethereum/app_1.1.2_key",
        delete="blue/2.1.0-hw15/ethereum/app_del",
        delete_key="blue/2.1.0-hw15/ethereum/app_del_key",
        app_id=18
    )
    appVer218.providers.add(1)
    appVer218.device_versions.add(7,8)
    appVer218.se_firmware_final_versions.add(3,4,5,6)
    # 219 , 
    appVer219 = ApplicationVersion.objects.create(
        name="HODL",
        version=1,
        display_name="HODL",
        icon="hodl",
        hash="",
        perso="perso_11",
        firmware="nanos/1.4.2/hodl/app_0.0.1",
        firmware_key="nanos/1.4.2/hodl/app_0.0.1_key",
        delete="nanos/1.4.2/hodl/app_del",
        delete_key="nanos/1.4.2/hodl/app_del_key",
        app_id=48
    )
    appVer219.providers.add(1)
    appVer219.device_versions.add(6)
    appVer219.se_firmware_final_versions.add(10)
    # 220 , 
    appVer220 = ApplicationVersion.objects.create(
        name="Recovery Check",
        version=65536,
        display_name="Recovery Check",
        icon="checkseed",
        hash="none",
        perso="perso_11",
        firmware="nanos/1.4.2/checkseed/app_1.0.0",
        firmware_key="nanos/1.4.2/checkseed/app_1.0.0_key",
        delete="nanos/1.4.2/checkseed/app_del",
        delete_key="nanos/1.4.2/checkseed/app_del_key",
        app_id=49
    )
    appVer220.providers.add(1)
    appVer220.device_versions.add(6)
    appVer220.se_firmware_final_versions.add(10)
    # 221 , 
    appVer221 = ApplicationVersion.objects.create(
        name="Vault",
        version=65538,
        display_name="Vault",
        icon="vault",
        hash="1ba6e0aea725e281ba818b6d5eb30abf5aa2b3345eb7cc71fe392ced3707a095",
        perso="perso_11",
        firmware="blue/2.1.1-ee/vault3/vault-1.0.2_sdk-2.1.1-ee",
        firmware_key="blue/2.1.1-ee/vault3/vault-1.0.2_sdk-2.1.1-ee_key",
        delete="blue/2.1.1-ee/vault3/vault-1.0.1_sdk-2.1.1-ee_del",
        delete_key="blue/2.1.1-ee/vault3/vault-1.0.1_sdk-2.1.1-ee_del_key",
        app_id=50
    )
    appVer221.providers.add(5)
    appVer221.device_versions.add(7,8)
    appVer221.se_firmware_final_versions.add(firmware_final_ver8)
    # 222 , 
    appVer222 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65795,
        display_name="Ethereum",
        icon="ethereum",
        hash="a21e1537cad5b73e296fdf9248c0330c5803a77d7a66d8005fcc47ef4ac39237",
        perso="perso_11",
        firmware="nanos/1.4.2/ethereum/app_1.1.3",
        firmware_key="nanos/1.4.2/ethereum/app_1.1.3_key",
        delete="nanos/1.4.2/ethereum/app_1.1.3_del",
        delete_key="nanos/1.4.2/ethereum/app_1.1.3_del_key",
        app_id=18
    )
    appVer222.providers.add(1)
    appVer222.device_versions.add(6)
    appVer222.se_firmware_final_versions.add(10)
    # 223 , 
    appVer223 = ApplicationVersion.objects.create(
        name="ICON",
        version=256,
        display_name="ICON",
        icon="icon",
        hash="464f6318b4a499ce645e9eeeb1cab18e53d4ff1c6df5e1031b4a28428f82e86a",
        perso="perso_11",
        firmware="nanos/1.4.2/icon/app_0.1.0",
        firmware_key="nanos/1.4.2/icon/app_0.1.0_key",
        delete="nanos/1.4.2/icon/app_0.1.0_del",
        delete_key="nanos/1.4.2/icon/app_0.1.0_del_key",
        app_id=51
    )
    appVer223.providers.add(1)
    appVer223.device_versions.add(6)
    appVer223.se_firmware_final_versions.add(10)
    # 224 , 
    appVer224 = ApplicationVersion.objects.create(
        name="kUSD",
        version=65795,
        display_name="kUSD",
        icon="kusd",
        hash="01fde69e27ae8c2b1a18bb5c281965495f0aea02b7bc9973e9ae668eeba2c48d",
        perso="perso_11",
        firmware="nanos/1.4.2/kusd/app_1.1.3",
        firmware_key="nanos/1.4.2/kusd/app_1.1.3_key",
        delete="nanos/1.4.2/kusd/app_1.1.3_del",
        delete_key="nanos/1.4.2/kusd/app_1.1.3_del_key",
        app_id=52
    )
    appVer224.providers.add(1)
    appVer224.device_versions.add(6)
    appVer224.se_firmware_final_versions.add(10)
    # 225 , 
    appVer225 = ApplicationVersion.objects.create(
        name="Ontology",
        version=65536,
        display_name="Ontology",
        icon="ontology",
        hash="d7c500c1c585d695d2d04f2cd23b5e585577124befb94c4f82322188773b785e",
        perso="perso_11",
        firmware="nanos/1.4.2/ontology/app_1.0",
        firmware_key="nanos/1.4.2/ontology/app_1.0_key",
        delete="nanos/1.4.2/ontology/app_1.0_del",
        delete_key="nanos/1.4.2/ontology/app_1.0_del_key",
        app_id=53
    )
    appVer225.providers.add(1)
    appVer225.device_versions.add(6)
    appVer225.se_firmware_final_versions.add(10)
    # 226 , 
    appVer226 = ApplicationVersion.objects.create(
        name="Particl",
        version=66055,
        display_name="Particl",
        icon="particl",
        hash="e27b91dedb5f1ecbe923ced574f1bb58737366c2a22c1b09fca9ec57fd88e546",
        perso="perso_11",
        firmware="nanos/1.4.2/particl/app_1.2.7",
        firmware_key="nanos/1.4.2/particl/app_1.2.7_key",
        delete="nanos/1.4.2/particl/app_1.2.7_del",
        delete_key="nanos/1.4.2/particl/app_1.2.7_del_key",
        app_id=54
    )
    appVer226.providers.add(1)
    appVer226.device_versions.add(6)
    appVer226.se_firmware_final_versions.add(10)
    # 227 , 
    appVer227 = ApplicationVersion.objects.create(
        name="POA",
        version=65795,
        display_name="POA",
        icon="poa",
        hash="691bd80f5eb8fa0c42f402edebf70b4c263e68882280ec97f597f836d8f87a92",
        perso="perso_11",
        firmware="nanos/1.4.2/poa/app_1.1.3",
        firmware_key="nanos/1.4.2/poa/app_1.1.3_key",
        delete="nanos/1.4.2/poa/app_1.1.3_del",
        delete_key="nanos/1.4.2/poa/app_1.1.3_del_key",
        app_id=55
    )
    appVer227.providers.add(1)
    appVer227.device_versions.add(6)
    appVer227.se_firmware_final_versions.add(10)
    # 228 , 
    appVer228 = ApplicationVersion.objects.create(
        name="RSK",
        version=65795,
        display_name="RSK",
        icon="rsk",
        hash="c357069dea0a3ffb1b192d73e5402e5f515a23c8c8203ce0099c823ddb89b86d",
        perso="perso_11",
        firmware="nanos/1.4.2/rsk/app_1.1.3",
        firmware_key="nanos/1.4.2/rsk/app_1.1.3_key",
        delete="nanos/1.4.2/rsk/app_1.1.3_del",
        delete_key="nanos/1.4.2/rsk/app_1.1.3_del_key",
        app_id=56
    )
    appVer228.providers.add(1)
    appVer228.device_versions.add(6)
    appVer228.se_firmware_final_versions.add(10)
    # 229 , 
    appVer229 = ApplicationVersion.objects.create(
        name="VeChain",
        version=65536,
        display_name="VeChain",
        icon="vechain",
        hash="d4e68a1ed9defff56c5dd646c1883b046089c09fe84549605c3788fd2f8806cf",
        perso="perso_11",
        firmware="nanos/1.4.2/vechain/app_1.0.0",
        firmware_key="nanos/1.4.2/vechain/app_1.0.0_key",
        delete="nanos/1.4.2/vechain/app_1.0.0_del",
        delete_key="nanos/1.4.2/vechain/app_1.0.0_del_key",
        app_id=57
    )
    appVer229.providers.add(1)
    appVer229.device_versions.add(6)
    appVer229.se_firmware_final_versions.add(10)
    # 230 , 
    appVer230 = ApplicationVersion.objects.create(
        name="Wanchain",
        version=65795,
        display_name="Wanchain",
        icon="wanchain",
        hash="152a7bb1ce142ca4887dbdcdcfe7ddf6b6f19ba2f211828694a014dbd105c950",
        perso="perso_11",
        firmware="nanos/1.4.2/wanchain/app_1.1.3",
        firmware_key="nanos/1.4.2/wanchain/app_1.1.3_key",
        delete="nanos/1.4.2/wanchain/app_1.1.3_del",
        delete_key="nanos/1.4.2/wanchain/app_1.1.3_del_key",
        app_id=58
    )
    appVer230.providers.add(1)
    appVer230.device_versions.add(6)
    appVer230.se_firmware_final_versions.add(10)
    # 231 , 
    appVer231 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65795,
        display_name="Ethereum",
        icon="ethereum",
        hash="ff2892ab49bbe671f4a677e67d8f8f77866b8aa92a8559b60c4dd1060a7a12c6",
        perso="perso_11",
        firmware="blue/2.1.1/ethereum/app_1.1.3",
        firmware_key="blue/2.1.1/ethereum/app_1.1.3_key",
        delete="blue/2.1.1/ethereum/app_1.1.3_del",
        delete_key="blue/2.1.1/ethereum/app_1.1.3_del_key",
        app_id=18
    )
    appVer231.providers.add(1)
    appVer231.device_versions.add(7)
    appVer231.se_firmware_final_versions.add(3,4)
    # 232 , 
    appVer232 = ApplicationVersion.objects.create(
        name="kUSD",
        version=65795,
        display_name="kUSD",
        icon="kusd",
        hash="dfeeeb0697cc91b72765ebe720a878bda5ce58628c8bc8b4596b6684f689cd28",
        perso="perso_11",
        firmware="blue/2.1.1/kusd/app_1.1.3",
        firmware_key="blue/2.1.1/kusd/app_1.1.3_key",
        delete="blue/2.1.1/kusd/app_1.1.3_del",
        delete_key="blue/2.1.1/kusd/app_1.1.3_del_key",
        app_id=52
    )
    appVer232.providers.add(1)
    appVer232.device_versions.add(7)
    appVer232.se_firmware_final_versions.add(3,4)
    # 233 , 
    appVer233 = ApplicationVersion.objects.create(
        name="Ontology",
        version=65536,
        display_name="Ontology",
        icon="ontology",
        hash="c593f5a9396ebc9e4f917b1c2ae88efead4336eb3c3bc8a2bf53da83481921f3",
        perso="perso_11",
        firmware="blue/2.1.1/ontology/app_1.0",
        firmware_key="blue/2.1.1/ontology/app_1.0_key",
        delete="blue/2.1.1/ontology/app_1.0_del",
        delete_key="blue/2.1.1/ontology/app_1.0_del_key",
        app_id=53
    )
    appVer233.providers.add(1)
    appVer233.device_versions.add(7)
    appVer233.se_firmware_final_versions.add(3,4)
    # 234 , 
    appVer234 = ApplicationVersion.objects.create(
        name="POA",
        version=65795,
        display_name="POA",
        icon="poa",
        hash="dee2c578acf6da4a36281b4a4acbe515ba038cc28fa5e43e25c3223182e0f524",
        perso="perso_11",
        firmware="blue/2.1.1/poa/app_1.1.3",
        firmware_key="blue/2.1.1/poa/app_1.1.3_key",
        delete="blue/2.1.1/poa/app_1.1.3_del",
        delete_key="blue/2.1.1/poa/app_1.1.3_del_key",
        app_id=55
    )
    appVer234.providers.add(1)
    appVer234.device_versions.add(7)
    appVer234.se_firmware_final_versions.add(3,4)
    # 235 , 
    appVer235 = ApplicationVersion.objects.create(
        name="RSK",
        version=65795,
        display_name="RSK",
        icon="rsk",
        hash="d8f0dbcb192b08700c56d96d9d7b908765cbed51eab94e2d54e11659045485b1",
        perso="perso_11",
        firmware="blue/2.1.1/rsk/app_1.1.3",
        firmware_key="blue/2.1.1/rsk/app_1.1.3_key",
        delete="blue/2.1.1/rsk/app_1.1.3_del",
        delete_key="blue/2.1.1/rsk/app_1.1.3_del_key",
        app_id=56
    )
    appVer235.providers.add(1)
    appVer235.device_versions.add(7)
    appVer235.se_firmware_final_versions.add(3,4)
    # 236 , 
    appVer236 = ApplicationVersion.objects.create(
        name="Wanchain",
        version=65795,
        display_name="Wanchain",
        icon="wanchain",
        hash="2e482f5d42aa10f2b707d4e1861716d04228a8b2f1f77d778302edb7bf8e45ca",
        perso="perso_11",
        firmware="blue/2.1.1/wanchain/app_1.1.3",
        firmware_key="blue/2.1.1/wanchain/app_1.1.3_key",
        delete="blue/2.1.1/wanchain/app_1.1.3_del",
        delete_key="blue/2.1.1/wanchain/app_1.1.3_del_key",
        app_id=58
    )
    appVer236.providers.add(1)
    appVer236.device_versions.add(7)
    appVer236.se_firmware_final_versions.add(3,4)
    # 237 , 
    appVer237 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65795,
        display_name="Ethereum",
        icon="ethereum",
        hash="ff2892ab49bbe671f4a677e67d8f8f77866b8aa92a8559b60c4dd1060a7a12c6",
        perso="perso_11",
        firmware="blue/2.1.1/ethereum/app_1.1.3",
        firmware_key="blue/2.1.1/ethereum/app_1.1.3_key",
        delete="blue/2.1.1/ethereum/app_1.1.3_del",
        delete_key="blue/2.1.1/ethereum/app_1.1.3_del_key",
        app_id=18
    )
    appVer237.providers.add(1)
    appVer237.device_versions.add(8)
    appVer237.se_firmware_final_versions.add(3,4)
    # 238 , 
    appVer238 = ApplicationVersion.objects.create(
        name="kUSD",
        version=65795,
        display_name="kUSD",
        icon="kusd",
        hash="dfeeeb0697cc91b72765ebe720a878bda5ce58628c8bc8b4596b6684f689cd28",
        perso="perso_11",
        firmware="blue/2.1.1/kusd/app_1.1.3",
        firmware_key="blue/2.1.1/kusd/app_1.1.3_key",
        delete="blue/2.1.1/kusd/app_1.1.3_del",
        delete_key="blue/2.1.1/kusd/app_1.1.3_del_key",
        app_id=52
    )
    appVer238.providers.add(1)
    appVer238.device_versions.add(8)
    appVer238.se_firmware_final_versions.add(3,4)
    # 239 , 
    appVer239 = ApplicationVersion.objects.create(
        name="Ontology",
        version=65536,
        display_name="Ontology",
        icon="ontology",
        hash="c593f5a9396ebc9e4f917b1c2ae88efead4336eb3c3bc8a2bf53da83481921f3",
        perso="perso_11",
        firmware="blue/2.1.1/ontology/app_1.0",
        firmware_key="blue/2.1.1/ontology/app_1.0_key",
        delete="blue/2.1.1/ontology/app_1.0_del",
        delete_key="blue/2.1.1/ontology/app_1.0_del_key",
        app_id=53
    )
    appVer239.providers.add(1)
    appVer239.device_versions.add(8)
    appVer239.se_firmware_final_versions.add(3,4)
    # 240 , 
    appVer240 = ApplicationVersion.objects.create(
        name="POA",
        version=65795,
        display_name="POA",
        icon="poa",
        hash="dee2c578acf6da4a36281b4a4acbe515ba038cc28fa5e43e25c3223182e0f524",
        perso="perso_11",
        firmware="blue/2.1.1/poa/app_1.1.3",
        firmware_key="blue/2.1.1/poa/app_1.1.3_key",
        delete="blue/2.1.1/poa/app_1.1.3_del",
        delete_key="blue/2.1.1/poa/app_1.1.3_del_key",
        app_id=55
    )
    appVer240.providers.add(1)
    appVer240.device_versions.add(8)
    appVer240.se_firmware_final_versions.add(3,4)
    # 241 , 
    appVer241 = ApplicationVersion.objects.create(
        name="RSK",
        version=65795,
        display_name="RSK",
        icon="rsk",
        hash="d8f0dbcb192b08700c56d96d9d7b908765cbed51eab94e2d54e11659045485b1",
        perso="perso_11",
        firmware="blue/2.1.1/rsk/app_1.1.3",
        firmware_key="blue/2.1.1/rsk/app_1.1.3_key",
        delete="blue/2.1.1/rsk/app_1.1.3_del",
        delete_key="blue/2.1.1/rsk/app_1.1.3_del_key",
        app_id=56
    )
    appVer241.providers.add(1)
    appVer241.device_versions.add(8)
    appVer241.se_firmware_final_versions.add(3,4)
    # 242 , 
    appVer242 = ApplicationVersion.objects.create(
        name="Wanchain",
        version=65795,
        display_name="Wanchain",
        icon="wanchain",
        hash="2e482f5d42aa10f2b707d4e1861716d04228a8b2f1f77d778302edb7bf8e45ca",
        perso="perso_11",
        firmware="blue/2.1.1/wanchain/app_1.1.3",
        firmware_key="blue/2.1.1/wanchain/app_1.1.3_key",
        delete="blue/2.1.1/wanchain/app_1.1.3_del",
        delete_key="blue/2.1.1/wanchain/app_1.1.3_del_key",
        app_id=58
    )
    appVer242.providers.add(1)
    appVer242.device_versions.add(8)
    appVer242.se_firmware_final_versions.add(3,4)
    # 243 , 
    appVer243 = ApplicationVersion.objects.create(
        name="Ethereum Classic",
        version=65795,
        display_name="Ethereum Classic",
        icon="ethereum_classic",
        hash="2997bea46ca7eb35c9ef3eda0c7c71d3d90a3f75b542b0aa5ff84eda0c404bb7",
        perso="perso_11",
        firmware="nanos/1.4.2/ethereum_classic/app_1.1.3",
        firmware_key="nanos/1.4.2/ethereum_classic/app_1.1.3_key",
        delete="nanos/1.4.2/ethereum_classic/app_1.1.3_del",
        delete_key="nanos/1.4.2/ethereum_classic/app_1.1.3_del_key",
        app_id=59
    )
    appVer243.providers.add(1)
    appVer243.device_versions.add(6)
    appVer243.se_firmware_final_versions.add(10)
    # 244 , 
    appVer244 = ApplicationVersion.objects.create(
        name="Stellar",
        version=196609,
        display_name="Stellar",
        icon="stellar",
        hash="9f5dd4efde4ed06c24074c828214ffe195d4c81b05a66f5179f1d96ea697f44e",
        perso="perso_11",
        firmware="nanos/1.4.2/stellar/app_3.0.1",
        firmware_key="nanos/1.4.2/stellar/app_3.0.1_key",
        delete="nanos/1.4.2/stellar/app_3.0.1_del",
        delete_key="nanos/1.4.2/stellar/app_3.0.1_del_key",
        app_id=27
    )
    appVer244.providers.add(1)
    appVer244.device_versions.add(6)
    appVer244.se_firmware_final_versions.add(10)
    # 245 , 
    appVer245 = ApplicationVersion.objects.create(
        name="RSK Test",
        version=65795,
        display_name="RSK Test",
        icon="rsk_testnet",
        hash="493475106600d4ce1d8e364d9c41b987db16118e6d1d31a88d01a4f118c5f098",
        perso="perso_11",
        firmware="nanos/1.4.2/rsk_testnet/app_1.1.3",
        firmware_key="nanos/1.4.2/rsk_testnet/app_1.1.3_key",
        delete="nanos/1.4.2/rsk_testnet/app_1.1.3_del",
        delete_key="nanos/1.4.2/rsk_testnet/app_1.1.3_del_key",
        app_id=60
    )
    appVer245.providers.add(1)
    appVer245.device_versions.add(6)
    appVer245.se_firmware_final_versions.add(10)
    # 246 , 
    appVer246 = ApplicationVersion.objects.create(
        name="ICON Test",
        version=256,
        display_name="ICON Test",
        icon="icon_testnet",
        hash="464f6318b4a499ce645e9eeeb1cab18e53d4ff1c6df5e1031b4a28428f82e86a",
        perso="perso_11",
        firmware="nanos/1.4.2/icon_testnet/app_0.1.0",
        firmware_key="nanos/1.4.2/icon_testnet/app_0.1.0_key",
        delete="nanos/1.4.2/icon_testnet/app_0.1.0_del",
        delete_key="nanos/1.4.2/icon_testnet/app_0.1.0_del_key",
        app_id=61
    )
    appVer246.providers.add(1)
    appVer246.device_versions.add(6)
    appVer246.se_firmware_final_versions.add(10)
    # 247 , 
    appVer247 = ApplicationVersion.objects.create(
        name="Ethereum Classic",
        version=65795,
        display_name="Ethereum Classic",
        icon="ethereum_classic",
        hash="2d0e37fbfd1c7a0027445570b59966224c4102e62260bcf8b172dbeb5a8c1f93",
        perso="perso_11",
        firmware="blue/2.1.1/ethereum_classic/app_1.1.3",
        firmware_key="blue/2.1.1/ethereum_classic/app_1.1.3_key",
        delete="blue/2.1.1/ethereum_classic/app_1.1.3_del",
        delete_key="blue/2.1.1/ethereum_classic/app_1.1.3_del_key",
        app_id=59
    )
    appVer247.providers.add(1)
    appVer247.device_versions.add(7,8)
    appVer247.se_firmware_final_versions.add(3,4)
    # 248 , 
    appVer248 = ApplicationVersion.objects.create(
        name="Stellar",
        version=196609,
        display_name="Stellar",
        icon="stellar",
        hash="b5147f7c612fb2dc9c70bdbf354f8599c0406ed07df42b0e31cfeb3d8e158391",
        perso="perso_11",
        firmware="blue/2.1.1/stellar/app_3.0.1",
        firmware_key="blue/2.1.1/stellar/app_3.0.1_key",
        delete="blue/2.1.1/stellar/app_3.0.1_del",
        delete_key="blue/2.1.1/stellar/app_3.0.1_del_key",
        app_id=27
    )
    appVer248.providers.add(1)
    appVer248.device_versions.add(7,8)
    appVer248.se_firmware_final_versions.add(3,4)
    # 249 , 
    appVer249 = ApplicationVersion.objects.create(
        name="RSK Test",
        version=65795,
        display_name="RSK Test",
        icon="rsk_testnet",
        hash="3cef98f5a6cdbfc6ab0c0179c1b80aeba1b62f693d5d0e080cb720bd008d83b7",
        perso="perso_11",
        firmware="blue/2.1.1/rsk_testnet/app_1.1.3",
        firmware_key="blue/2.1.1/rsk_testnet/app_1.1.3_key",
        delete="blue/2.1.1/rsk_testnet/app_1.1.3_del",
        delete_key="blue/2.1.1/rsk_testnet/app_1.1.3_del_key",
        app_id=60
    )
    appVer249.providers.add(1)
    appVer249.device_versions.add(7,8)
    appVer249.se_firmware_final_versions.add(3,4)
    # 250 , 
    appVer250 = ApplicationVersion.objects.create(
        name="ICON Test",
        version=256,
        display_name="ICON Test",
        icon="icon_testnet",
        hash="d1c06c1dbbb2b3d1aadd0d3c245d98ba2f95fc11f950a62fe5bc992bd40a8aee",
        perso="perso_11",
        firmware="blue/2.1.1/icon_testnet/app_0.1.0",
        firmware_key="blue/2.1.1/icon_testnet/app_0.1.0_key",
        delete="blue/2.1.1/icon_testnet/app_0.1.0_del",
        delete_key="blue/2.1.1/icon_testnet/app_0.1.0_del_key",
        app_id=61
    )
    appVer250.providers.add(1)
    appVer250.device_versions.add(7,8)
    appVer250.se_firmware_final_versions.add(3,4)
    # 251 , 
    appVer251 = ApplicationVersion.objects.create(
        name="Tron",
        version=2,
        display_name="Tron",
        icon="tron",
        hash="15a866184d1eff6bc7782f843a5563570faf50c95ae1cec0ac3919d918bb53e6",
        perso="perso_11",
        firmware="blue/2.1.1/tron/app_0.0.2",
        firmware_key="blue/2.1.1/tron/app_0.0.2_key",
        delete="blue/2.1.1/tron/app_0.0.2_del",
        delete_key="blue/2.1.1/tron/app_0.0.2_del_key",
        app_id=45
    )
    appVer251.providers.add(1)
    appVer251.device_versions.add(7,8)
    appVer251.se_firmware_final_versions.add(3,4)
    # 252 , 
    appVer252 = ApplicationVersion.objects.create(
        name="NEO",
        version=66305,
        display_name="NEO",
        icon="neo",
        hash="68917c9ae0bd919ded6070e626226ed52b15b0b6a8aa346288ab629fc0f97e2c",
        perso="perso_11",
        firmware="blue/2.1.1/neo/app_1.3.1",
        firmware_key="blue/2.1.1/neo/app_1.3.1_key",
        delete="blue/2.1.1/neo/app_1.3.1_del",
        delete_key="blue/2.1.1/neo/app_1.3.1_del_key",
        app_id=29
    )
    appVer252.providers.add(1)
    appVer252.device_versions.add(7,8)
    appVer252.se_firmware_final_versions.add(3,4)
    # 253 , 
    appVer253 = ApplicationVersion.objects.create(
        name="Vault",
        version=65540,
        display_name="Vault",
        icon="vault",
        hash="none",
        perso="perso_11",
        firmware="blue/2.1.1-ee/vault3/vault-1.0.4_sdk-2.1.1-ee",
        firmware_key="blue/2.1.1-ee/vault3/vault-1.0.4_sdk-2.1.1-ee_key",
        delete="blue/2.1.1-ee/vault3/app_del",
        delete_key="blue/2.1.1-ee/vault3/app_del_key",
        app_id=50
    )
    appVer253.providers.add(5)
    appVer253.device_versions.add(7,8)
    appVer253.se_firmware_final_versions.add(firmware_final_ver8)
    # 254 , 
    appVer254 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65796,
        display_name="Ethereum",
        icon="ethereum",
        hash="d70067d3021a25d335cd4b037e5175ed28a81debc0c5fe654730449b556fbc29",
        perso="perso_11",
        firmware="nanos/1.4.2/ethereum/app_1.1.4",
        firmware_key="nanos/1.4.2/ethereum/app_1.1.4_key",
        delete="nanos/1.4.2/ethereum/app_1.1.4_del",
        delete_key="nanos/1.4.2/ethereum/app_1.1.4_del_key",
        app_id=18
    )
    appVer254.providers.add(1)
    appVer254.device_versions.add(6)
    appVer254.se_firmware_final_versions.add(10)
    # 255 , 
    appVer255 = ApplicationVersion.objects.create(
        name="POA",
        version=65796,
        display_name="POA",
        icon="poa",
        hash="4383af7691fffb30275664a6b5b4ede656c21547c26d95653464ffe6d45e62be",
        perso="perso_11",
        firmware="nanos/1.4.2/poa/app_1.1.4",
        firmware_key="nanos/1.4.2/poa/app_1.1.4_key",
        delete="nanos/1.4.2/poa/app_1.1.4_del",
        delete_key="nanos/1.4.2/poa/app_1.1.4_del_key",
        app_id=55
    )
    appVer255.providers.add(1)
    appVer255.device_versions.add(6)
    appVer255.se_firmware_final_versions.add(10)
    # 256 , 
    appVer256 = ApplicationVersion.objects.create(
        name="RSK",
        version=65796,
        display_name="RSK",
        icon="rsk",
        hash="a8ee5878ad7f92e641bd517cce4391d7c6b735bbd6ee60a74301f8906256dcf4",
        perso="perso_11",
        firmware="nanos/1.4.2/rsk/app_1.1.4",
        firmware_key="nanos/1.4.2/rsk/app_1.1.4_key",
        delete="nanos/1.4.2/rsk/app_1.1.4_del",
        delete_key="nanos/1.4.2/rsk/app_1.1.4_del_key",
        app_id=56
    )
    appVer256.providers.add(1)
    appVer256.device_versions.add(6)
    appVer256.se_firmware_final_versions.add(10)
    # 257 , 
    appVer257 = ApplicationVersion.objects.create(
        name="Expanse",
        version=65796,
        display_name="Expanse",
        icon="expanse",
        hash="f04adbb6f5785adb3553bf224731f0b44ff753e7b46a9099dfc2502ece030383",
        perso="perso_11",
        firmware="nanos/1.4.2/expanse/app_1.1.4",
        firmware_key="nanos/1.4.2/expanse/app_1.1.4_key",
        delete="nanos/1.4.2/expanse/app_1.1.4_del",
        delete_key="nanos/1.4.2/expanse/app_1.1.4_del_key",
        app_id=15
    )
    appVer257.providers.add(1)
    appVer257.device_versions.add(6)
    appVer257.se_firmware_final_versions.add(10)
    # 258 , 
    appVer258 = ApplicationVersion.objects.create(
        name="kUSD",
        version=65796,
        display_name="kUSD",
        icon="kusd",
        hash="93bd9339d6bff9cb7cb7514b2a0bbae4801dfb67d4f4b1de0da258174646ce66",
        perso="perso_11",
        firmware="nanos/1.4.2/kusd/app_1.1.4",
        firmware_key="nanos/1.4.2/kusd/app_1.1.4_key",
        delete="nanos/1.4.2/kusd/app_1.1.4_del",
        delete_key="nanos/1.4.2/kusd/app_1.1.4_del_key",
        app_id=52
    )
    appVer258.providers.add(1)
    appVer258.device_versions.add(6)
    appVer258.se_firmware_final_versions.add(10)
    # 259 , 
    appVer259 = ApplicationVersion.objects.create(
        name="Wanchain",
        version=65796,
        display_name="Wanchain",
        icon="wanchain",
        hash="feb8bd3408ed510bd7a97e02a00e472b79d39269d6d6561ec36c891af342e385",
        perso="perso_11",
        firmware="nanos/1.4.2/wanchain/app_1.1.4",
        firmware_key="nanos/1.4.2/wanchain/app_1.1.4_key",
        delete="nanos/1.4.2/wanchain/app_1.1.4_del",
        delete_key="nanos/1.4.2/wanchain/app_1.1.4_del_key",
        app_id=58
    )
    appVer259.providers.add(1)
    appVer259.device_versions.add(6)
    appVer259.se_firmware_final_versions.add(10)
    # 260 , 
    appVer260 = ApplicationVersion.objects.create(
        name="Ethereum Classic",
        version=65796,
        display_name="Ethereum Classic",
        icon="ethereum_classic",
        hash="0500d221130d189e4e9ec9935539838af3ffdabedf9d1113e4d65bff15066f61",
        perso="perso_11",
        firmware="nanos/1.4.2/ethereum_classic/app_1.1.4",
        firmware_key="nanos/1.4.2/ethereum_classic/app_1.1.4_key",
        delete="nanos/1.4.2/ethereum_classic/app_1.1.4_del",
        delete_key="nanos/1.4.2/ethereum_classic/app_1.1.4_del_key",
        app_id=59
    )
    appVer260.providers.add(1)
    appVer260.device_versions.add(6)
    appVer260.se_firmware_final_versions.add(10)
    # 261 , 
    appVer261 = ApplicationVersion.objects.create(
        name="Ubiq",
        version=65796,
        display_name="Ubiq",
        icon="ubiq",
        hash="c161a5f00b083cb3e78a3f809c2ce97fbfefbf6315faf50b275935d2107e82fe",
        perso="perso_11",
        firmware="nanos/1.4.2/ubiq/app_1.1.4",
        firmware_key="nanos/1.4.2/ubiq/app_1.1.4_key",
        delete="nanos/1.4.2/ubiq/app_1.1.4_del",
        delete_key="nanos/1.4.2/ubiq/app_1.1.4_del_key",
        app_id=14
    )
    appVer261.providers.add(1)
    appVer261.device_versions.add(6)
    appVer261.se_firmware_final_versions.add(10)
    # 262 , 
    appVer262 = ApplicationVersion.objects.create(
        name="RSK Test",
        version=65796,
        display_name="RSK Test",
        icon="rsk_testnet",
        hash="8e6703ac7fc6c31c74aa0ac72b7d0daf98d8e869454e7a4b9c48111570ce4320",
        perso="perso_11",
        firmware="nanos/1.4.2/rsk_testnet/app_1.1.4",
        firmware_key="nanos/1.4.2/rsk_testnet/app_1.1.4_key",
        delete="nanos/1.4.2/rsk_testnet/app_1.1.4_del",
        delete_key="nanos/1.4.2/rsk_testnet/app_1.1.4_del_key",
        app_id=60
    )
    appVer262.providers.add(1)
    appVer262.device_versions.add(6)
    appVer262.se_firmware_final_versions.add(10)
    # 263 , 
    appVer263 = ApplicationVersion.objects.create(
        name="POA",
        version=65796,
        display_name="POA",
        icon="poa",
        hash="b548898c51197b4717d08c25a01b82d9d519bb6326560e1313871ccff3b6ab7d",
        perso="perso_11",
        firmware="blue/2.1.1/poa/app_1.1.4",
        firmware_key="blue/2.1.1/poa/app_1.1.4_key",
        delete="blue/2.1.1/poa/app_1.1.4_del",
        delete_key="blue/2.1.1/poa/app_1.1.4_del_key",
        app_id=55
    )
    appVer263.providers.add(1)
    appVer263.device_versions.add(7,8)
    appVer263.se_firmware_final_versions.add(3,4)
    # 264 , 
    appVer264 = ApplicationVersion.objects.create(
        name="RSK",
        version=65796,
        display_name="RSK",
        icon="rsk",
        hash="96e2db9f752fca0d73e721e1832bf6cc47fb3fee5201d1f4ee5fa58dda16ab71",
        perso="perso_11",
        firmware="blue/2.1.1/rsk/app_1.1.4",
        firmware_key="blue/2.1.1/rsk/app_1.1.4_key",
        delete="blue/2.1.1/rsk/app_1.1.4_del",
        delete_key="blue/2.1.1/rsk/app_1.1.4_del_key",
        app_id=56
    )
    appVer264.providers.add(1)
    appVer264.device_versions.add(7,8)
    appVer264.se_firmware_final_versions.add(3,4)
    # 265 , 
    appVer265 = ApplicationVersion.objects.create(
        name="Ethereum",
        version=65796,
        display_name="Ethereum",
        icon="ethereum",
        hash="a656c9e3ea2da0fa7f053e2bf0e7a54ed5b0d7d1ae0618c932d8dcd76d31dfcc",
        perso="perso_11",
        firmware="blue/2.1.1/ethereum/app_1.1.4",
        firmware_key="blue/2.1.1/ethereum/app_1.1.4_key",
        delete="vblue/2.1.1/ethereum/app_1.1.4_del",
        delete_key="blue/2.1.1/ethereum/app_1.1.4_del_key",
        app_id=18
    )
    appVer265.providers.add(1)
    appVer265.device_versions.add(7,8)
    appVer265.se_firmware_final_versions.add(3,4)
    # 266 , 
    appVer266 = ApplicationVersion.objects.create(
        name="Expanse",
        version=65796,
        display_name="Expanse",
        icon="expanse",
        hash="e70cf64e6dc87d555ed3272d06de53531d6452c321971629d3b012470243e32d",
        perso="perso_11",
        firmware="blue/2.1.1/expanse/app_1.1.4",
        firmware_key="blue/2.1.1/expanse/app_1.1.4_key",
        delete="blue/2.1.1/expanse/app_1.1.4_del",
        delete_key="blue/2.1.1/expanse/app_1.1.4_del_key",
        app_id=15
    )
    appVer266.providers.add(1)
    appVer266.device_versions.add(7,8)
    appVer266.se_firmware_final_versions.add(3,4)
    # 267 , 
    appVer267 = ApplicationVersion.objects.create(
        name="kUSD",
        version=65796,
        display_name="kUSD",
        icon="kusd",
        hash="a2d94c95b9e7adc73e5539dcdfa32cdeac44fc842f89852ea9eb9b84a329172c",
        perso="perso_11",
        firmware="blue/2.1.1/kusd/app_1.1.4",
        firmware_key="blue/2.1.1/kusd/app_1.1.4_key",
        delete="blue/2.1.1/kusd/app_1.1.4_del",
        delete_key="blue/2.1.1/kusd/app_1.1.4_del_key",
        app_id=52
    )
    appVer267.providers.add(1)
    appVer267.device_versions.add(7,8)
    appVer267.se_firmware_final_versions.add(3,4)
    # 268 , 
    appVer268 = ApplicationVersion.objects.create(
        name="Wanchain",
        version=65796,
        display_name="Wanchain",
        icon="wanchain",
        hash="dec4bb44ddd64fb706b082afacaf2bd9c0a118d5f920b3c3f179a6191db59d1b",
        perso="perso_11",
        firmware="blue/2.1.1/wanchain/app_1.1.4",
        firmware_key="blue/2.1.1/wanchain/app_1.1.4_key",
        delete="blue/2.1.1/wanchain/app_1.1.4_del",
        delete_key="blue/2.1.1/wanchain/app_1.1.4_del_key",
        app_id=58
    )
    appVer268.providers.add(1)
    appVer268.device_versions.add(7,8)
    appVer268.se_firmware_final_versions.add(3,4)
    # 269 , 
    appVer269 = ApplicationVersion.objects.create(
        name="Ethereum Classic",
        version=65796,
        display_name="Ethereum Classic",
        icon="ethereum_classic",
        hash="9ae9d23e88e7b418ca7e7b32c98413c7b91616ea26edf8f7c42db341f4cf9831",
        perso="perso_11",
        firmware="blue/2.1.1/ethereum_classic/app_1.1.4",
        firmware_key="blue/2.1.1/ethereum_classic/app_1.1.4_key",
        delete="blue/2.1.1/ethereum_classic/app_1.1.4_del",
        delete_key="blue/2.1.1/ethereum_classic/app_1.1.4_del_key",
        app_id=59
    )
    appVer269.providers.add(1)
    appVer269.device_versions.add(7,8)
    appVer269.se_firmware_final_versions.add(3,4)
    # 270 , 
    appVer270 = ApplicationVersion.objects.create(
        name="Ubiq",
        version=65796,
        display_name="Ubiq",
        icon="ubiq",
        hash="141d78e722a0b162879c4fb6d8622e0bbf1215425ec2d94071e0cb8c912ba686",
        perso="perso_11",
        firmware="blue/2.1.1/ubiq/app_1.1.4",
        firmware_key="blue/2.1.1/ubiq/app_1.1.4_key",
        delete="blue/2.1.1/ubiq/app_1.1.4_del",
        delete_key="blue/2.1.1/ubiq/app_1.1.4_del_key",
        app_id=14
    )
    appVer270.providers.add(1)
    appVer270.device_versions.add(7,8)
    appVer270.se_firmware_final_versions.add(3,4)
    # 271 , 
    appVer271 = ApplicationVersion.objects.create(
        name="RSK Test",
        version=65796,
        display_name="RSK Test",
        icon="rsk_testnet",
        hash="075821f05ad9affe0272a2ba66d19c7e274af237f3822f723a95447eb8dbdb6d",
        perso="perso_11",
        firmware="blue/2.1.1/rsk_testnet/app_1.1.4",
        firmware_key="blue/2.1.1/rsk_testnet/app_1.1.4_key",
        delete="blue/2.1.1/rsk_testnet/app_1.1.4_del",
        delete_key="blue/2.1.1/rsk_testnet/app_1.1.4_del_key",
        app_id=60
    )
    appVer271.providers.add(1)
    appVer271.device_versions.add(7,8)
    appVer271.se_firmware_final_versions.add(3,4)
    # 272 , 
    appVer272 = ApplicationVersion.objects.create(
        name="VeChain",
        version=65537,
        display_name="VeChain",
        icon="vechain",
        hash="52028f60a2dcdde6f6b54927148ba910a8f07172cc93179c5bafa0fbfb3fe6d5",
        perso="perso_11",
        firmware="nanos/1.4.2/vechain/app_1.0.1",
        firmware_key="nanos/1.4.2/vechain/app_1.0.1_key",
        delete="nanos/1.4.2/vechain/app_1.0.1_del",
        delete_key="nanos/1.4.2/vechain/app_1.0.1_del_key",
        app_id=57
    )
    appVer272.providers.add(1)
    appVer272.device_versions.add(6)
    appVer272.se_firmware_final_versions.add(10)
    # 273 , 
    appVer273 = ApplicationVersion.objects.create(
        name="Tron",
        version=2,
        display_name="Tron",
        icon="tron",
        hash="e0ae2cddbdcd8bfa69eb819a6cd88ccbe520b43e5e1758af648e5b4e073a56d8",
        perso="perso_11",
        firmware="nanos/1.4.2/tron/app_0.0.2",
        firmware_key="nanos/1.4.2/tron/app_0.0.2_key",
        delete="nanos/1.4.2/tron/app_0.0.2_del",
        delete_key="nanos/1.4.2/tron/app_0.0.2_del_key",
        app_id=45
    )
    appVer273.providers.add(1)
    appVer273.device_versions.add(6)
    appVer273.se_firmware_final_versions.add(10)
    # 274 , 
    appVer274 = ApplicationVersion.objects.create(
        name="Ontology",
        version=66048,
        display_name="Ontology",
        icon="ontology",
        hash="23e6675be41b0bfa05a5f8534b62ec1821e53fbd09fe953deecdd5fd6ca46b25",
        perso="perso_11",
        firmware="nanos/1.4.2/ontology/app_1.2",
        firmware_key="nanos/1.4.2/ontology/app_1.2_key",
        delete="nanos/1.4.2/ontology/app_1.2_del",
        delete_key="nanos/1.4.2/ontology/app_1.2_del_key",
        app_id=53
    )
    appVer274.providers.add(1)
    appVer274.device_versions.add(6)
    appVer274.se_firmware_final_versions.add(10)
    # 275 , 
    appVer275 = ApplicationVersion.objects.create(
        name="Nimiq",
        version=66305,
        display_name="Nimiq",
        icon="nimiq",
        hash="cd67b137679df58ec798ad49aae86d6bc2cdff9eae866c142d7b324cd79886d2",
        perso="perso_11",
        firmware="nanos/1.4.2/nimiq/app_1.3.1",
        firmware_key="nanos/1.4.2/nimiq/app_1.3.1_key",
        delete="nanos/1.4.2/nimiq/app_1.3.1_del",
        delete_key="nanos/1.4.2/nimiq/app_1.3.1_del_key",
        app_id=42
    )
    appVer275.providers.add(1)
    appVer275.device_versions.add(6)
    appVer275.se_firmware_final_versions.add(10)
    # 276 , 
    appVer276 = ApplicationVersion.objects.create(
        name="Neo",
        version=66305,
        display_name="Neo",
        icon="neo",
        hash="989300a852951dfd1f52e2e187ebaa7e72a7e62d107aad15d8f768f22a3ea26f",
        perso="perso_11",
        firmware="nanos/1.4.2/neo/app_1.3.1",
        firmware_key="nanos/1.4.2/neo/app_1.3.1_key",
        delete="nanos/1.4.2/neo/app_1.3.1_del",
        delete_key="nanos/1.4.2/neo/app_1.3.1_del_key",
        app_id=29
    )
    appVer276.providers.add(1)
    appVer276.device_versions.add(6)
    appVer276.se_firmware_final_versions.add(10)
    # 277 , 
    appVer277 = ApplicationVersion.objects.create(
        name="Tron",
        version=2,
        display_name="Tron",
        icon="tron",
        hash="6287053d0a3d9aa02f6fa6a9aabe1c4218b333da6242a0afa6aa7394fd7cffe2",
        perso="perso_11",
        firmware="blue/2.1.1/tron/app_0.0.2",
        firmware_key="blue/2.1.1/tron/app_0.0.2_key",
        delete="blue/2.1.1/tron/app_0.0.2_del",
        delete_key="blue/2.1.1/tron/app_0.0.2_del_key",
        app_id=45
    )
    appVer277.providers.add(1)
    appVer277.device_versions.add(7,8)
    appVer277.se_firmware_final_versions.add(3,4)
    # 278 , 
    appVer278 = ApplicationVersion.objects.create(
        name="Ontology",
        version=66048,
        display_name="Ontology",
        icon="ontology",
        hash="018ece31a04ad78631e20920dd715f0007266db4b588749f2188863784ecfbb7",
        perso="perso_11",
        firmware="blue/2.1.1/ontology/app_1.2",
        firmware_key="blue/2.1.1/ontology/app_1.2_key",
        delete="blue/2.1.1/ontology/app_1.2_del",
        delete_key="blue/2.1.1/ontology/app_1.2_del_key",
        app_id=53
    )
    appVer278.providers.add(1)
    appVer278.device_versions.add(7,8)
    appVer278.se_firmware_final_versions.add(3,4)
    # 279 , 
    appVer279 = ApplicationVersion.objects.create(
        name="Neo",
        version=66305,
        display_name="Neo",
        icon="neo",
        hash="eec1fae39b5db7ab994cfbf7b6a4b060a69b47bbee51b0c371cf4de65648eb6a",
        perso="perso_11",
        firmware="blue/2.1.1/neo/app_1.3.1",
        firmware_key="blue/2.1.1/neo/app_1.3.1_key",
        delete="blue/2.1.1/neo/app_1.3.1_del",
        delete_key="blue/2.1.1/neo/app_1.3.1_del_key",
        app_id=29
    )
    appVer279.providers.add(1)
    appVer279.device_versions.add(7,8)
    appVer279.se_firmware_final_versions.add(3,4)
    # 280 , 
    appVer280 = ApplicationVersion.objects.create(
        name="XRP",
        version=65540,
        display_name="XRP",
        icon="xrp",
        hash="dfa8c19e7111ec4ca7a6ac82e4db3456a38ee12a5e1797d53fc8666471c50977",
        perso="perso_11",
        firmware="blue/2.1.1/XRP/app_1.0.4",
        firmware_key="blue/2.1.1/XRP/app_1.0.4_key",
        delete="blue/2.1.1/XRP/app_1.0.4_del",
        delete_key="blue/2.1.1/XRP/app_1.0.4_del_key",
        app_id=22
    )
    appVer280.providers.add(1,4)
    appVer280.device_versions.add(7,8)
    appVer280.se_firmware_final_versions.add(3,4)
    # 281 , 
    appVer281 = ApplicationVersion.objects.create(
        name="Horizen",
        version=66056,
        display_name="Horizen",
        icon="horizen",
        hash="2a3206b68c5b75d4d3c73eb6007fb751883db154c1b509ee97c4cba8ba1c69f7",
        perso="perso_11",
        firmware="blue/2.1.1/horizen/app_1.2.8",
        firmware_key="blue/2.1.1/horizen/app_1.2.8_key",
        delete="blue/2.1.1/horizen/app_1.2.8_del",
        delete_key="blue/2.1.1/horizen/app_1.2.8_del_key",
        app_id=24
    )
    appVer281.providers.add(1,4)
    appVer281.device_versions.add(7,8)
    appVer281.se_firmware_final_versions.add(3,4)
    # 282 , 
    appVer282 = ApplicationVersion.objects.create(
        name="XRP",
        version=65540,
        display_name="XRP",
        icon="xrp",
        hash="50f9e91c9a9b8847e6d749387d2a30e22b956d1cf937e6e73e82660c278fc058",
        perso="perso_11",
        firmware="nanos/1.4.2/XRP/app_1.0.4",
        firmware_key="nanos/1.4.2/XRP/app_1.0.4_key",
        delete="nanos/1.4.2/XRP/app_1.0.4_del",
        delete_key="nanos/1.4.2/XRP/app_1.0.4_del_key",
        app_id=22
    )
    appVer282.providers.add(1,4)
    appVer282.device_versions.add(6)
    appVer282.se_firmware_final_versions.add(10)
    # 283 , 
    appVer283 = ApplicationVersion.objects.create(
        name="Horizen",
        version=66056,
        display_name="Horizen",
        icon="horizen",
        hash="26590c992024f3d3dd96c68642d97535168d21e1535acff5523753581240db09",
        perso="perso_11",
        firmware="nanos/1.4.2/horizen/app_1.2.8",
        firmware_key="nanos/1.4.2/horizen/app_1.2.8_key",
        delete="nanos/1.4.2/horizen/app_1.2.8_del",
        delete_key="nanos/1.4.2/horizen/app_1.2.8_del_key",
        app_id=24
    )
    appVer283.providers.add(1,4)
    appVer283.device_versions.add(6)
    appVer283.se_firmware_final_versions.add(10)
    # 284 , 
    appVer284 = ApplicationVersion.objects.create(
        name="EOS",
        version=65536,
        display_name="EOS",
        icon="eos",
        hash="a4d034f0aaacb8da49cb5815fe7310dbd0d2bdc6932cc9a44c0eb7e090ba9e2e",
        perso="perso_11",
        firmware="nanos/1.4.2/eos/app_1.0.0",
        firmware_key="nanos/1.4.2/eos/app_1.0.0_key",
        delete="nanos/1.4.2/eos/app_1.0.0_del",
        delete_key="nanos/1.4.2/eos/app_1.0.0_del_key",
        app_id=62
    )
    appVer284.providers.add(1)
    appVer284.device_versions.add(6)
    appVer284.se_firmware_final_versions.add(10)
    # 285 , 
    appVer285 = ApplicationVersion.objects.create(
        name="Lisk",
        version=65536,
        display_name="Lisk",
        icon="lisk",
        hash="b134a97753770384134ddf6aa0d90049da07dc8118ec78fe82c99bc6bdfaa653",
        perso="perso_11",
        firmware="nanos/1.4.2/lisk/app_1.0.0",
        firmware_key="nanos/1.4.2/lisk/app_1.0.0_key",
        delete="nanos/1.4.2/lisk/app_1.0.0_del",
        delete_key="nanos/1.4.2/lisk/app_1.0.0_del_key",
        app_id=63
    )
    appVer285.providers.add(1,4)
    appVer285.device_versions.add(6)
    appVer285.se_firmware_final_versions.add(10)
    # 286 , 
    appVer286 = ApplicationVersion.objects.create(
        name="Tezos Wallet",
        version=66304,
        display_name="Tezos Wallet",
        icon="tezos_wallet",
        hash="5524b44890b944fc277bf694c97d79e06578d27dabd17f4c2fdd9c40b1326bb6",
        perso="perso_11",
        firmware="nanos/1.4.2/tezos_wallet/app_0.0.0",
        firmware_key="nanos/1.4.2/tezos_wallet/app_0.0.0_key",
        delete="nanos/1.4.2/tezos_wallet/app_0.0.0_del",
        delete_key="nanos/1.4.2/tezos_wallet/app_0.0.0_del_key",
        app_id=44
    )
    appVer286.providers.add(1,4)
    appVer286.device_versions.add(6)
    appVer286.se_firmware_final_versions.add(10)
    # 287 , 
    appVer287 = ApplicationVersion.objects.create(
        name="FIC",
        version=196608,
        display_name="FIC",
        icon="fic",
        hash="c7a32e4709d18ef2c1e60d06af9fde4bb244636a568b1474d76bc2894cccf32a",
        perso="perso_11",
        firmware="nanos/1.4.2/fic/app_3.0.0",
        firmware_key="nanos/1.4.2/fic/app_3.0.0_key",
        delete="nanos/1.4.2/fic/app_3.0.0_del",
        delete_key="nanos/1.4.2/fic/app_3.0.0_del_key",
        app_id=64
    )
    appVer287.providers.add(1,4)
    appVer287.device_versions.add(6)
    appVer287.se_firmware_final_versions.add(10)
    # 288 , 
    appVer288 = ApplicationVersion.objects.create(
        name="Rise",
        version=65536,
        display_name="Rise",
        icon="rise",
        hash="f0a6d345d5ccc66b9373d963c22999466482cb8f5c5fd476ac6004038e6dd075",
        perso="perso_11",
        firmware="nanos/1.4.2/rise/app_1.0.0",
        firmware_key="nanos/1.4.2/rise/app_1.0.0_key",
        delete="nanos/1.4.2/rise/app_1.0.0_del",
        delete_key="nanos/1.4.2/rise/app_1.0.0_del_key",
        app_id=65
    )
    appVer288.providers.add(1,4)
    appVer288.device_versions.add(6)
    appVer288.se_firmware_final_versions.add(10)
    # 289 , 
    appVer289 = ApplicationVersion.objects.create(
        name="Aion",
        version=65536,
        display_name="Aion",
        icon="aion",
        hash="e93375bf87174366eccb8c187a52060c0af0fbd2a77bfc8c574937913ac1a88a",
        perso="perso_11",
        firmware="nanos/1.4.2/aion/app_1.0.0",
        firmware_key="nanos/1.4.2/aion/app_1.0.0_key",
        delete="nanos/1.4.2/aion/app_1.0.0_del",
        delete_key="nanos/1.4.2/aion/app_1.0.0_del_key",
        app_id=66
    )
    appVer289.providers.add(1,4)
    appVer289.device_versions.add(6)
    appVer289.se_firmware_final_versions.add(10)
    # 290 , 
    appVer290 = ApplicationVersion.objects.create(
        name="Pirl",
        version=65796,
        display_name="Pirl",
        icon="pirl",
        hash="baa7dccb2a7f0ade1e15337676a0b50bd51fda7b7a8f2ded10c74a48433a7fd9",
        perso="perso_11",
        firmware="nanos/1.4.2/pirl/app_1.1.4",
        firmware_key="nanos/1.4.2/pirl/app_1.1.4_key",
        delete="nanos/1.4.2/pirl/app_1.1.4_del",
        delete_key="nanos/1.4.2/pirl/app_1.1.4_del_key",
        app_id=67
    )
    appVer290.providers.add(1,4)
    appVer290.device_versions.add(6)
    appVer290.se_firmware_final_versions.add(10)
    # 291 , 
    appVer291 = ApplicationVersion.objects.create(
        name="Waves",
        version=2310,
        display_name="Waves",
        icon="waves",
        hash="22affb00fa00dcc2558e88e610634844b044a3335e102f9c03aed9e40d2719a0",
        perso="perso_11",
        firmware="nanos/1.4.2/waves/app_0.9.6",
        firmware_key="nanos/1.4.2/waves/app_0.9.6_key",
        delete="nanos/1.4.2/waves/app_0.9.6_del",
        delete_key="nanos/1.4.2/waves/app_0.9.6_del_key",
        app_id=68
    )
    appVer291.providers.add(1,4)
    appVer291.device_versions.add(6)
    appVer291.se_firmware_final_versions.add(10)
    # 292 , 
    appVer292 = ApplicationVersion.objects.create(
        name="Hycon",
        version=512,
        display_name="Hycon",
        icon="hycon",
        hash="8475f73be70f27c230aa3d14a8d835dd23e0f7887a0a04e9e7abef038897331d",
        perso="perso_11",
        firmware="nanos/1.4.2/hycon/app_0.2.0",
        firmware_key="nanos/1.4.2/hycon/app_0.2.0_key",
        delete="nanos/1.4.2/hycon/app_0.2.0_del",
        delete_key="nanos/1.4.2/hycon/app_0.2.0_del_key",
        app_id=69
    )
    appVer292.providers.add(1,4)
    appVer292.device_versions.add(6)
    appVer292.se_firmware_final_versions.add(10)
    # 293 , 
    appVer293 = ApplicationVersion.objects.create(
        name="Tezos Baking",
        version=66304,
        display_name="Tezos Baking",
        icon="tezos_baking",
        hash="a4c4a5e482be7e8a7382bf18314b395ffb68e4e8c577ee30a64aefe9741fc54f",
        perso="perso_11",
        firmware="nanos/1.4.2/tezos_baking/app_0.0.0",
        firmware_key="nanos/1.4.2/tezos_baking/app_0.0.0_key",
        delete="nanos/1.4.2/tezos_baking/app_0.0.0_del",
        delete_key="nanos/1.4.2/tezos_baking/app_0.0.0_del_key",
        app_id=43
    )
    appVer293.providers.add(1,4)
    appVer293.device_versions.add(6)
    appVer293.se_firmware_final_versions.add(10)
    # 294 , 
    appVer294 = ApplicationVersion.objects.create(
        name="Akroma",
        version=65796,
        display_name="Akroma",
        icon="akroma",
        hash="3ad7055f50f2d1bf0e02c46e2f3bffacb61d346f21cc697880e415d7d7859574",
        perso="perso_11",
        firmware="nanos/1.4.2/akroma/app_1.1.4",
        firmware_key="nanos/1.4.2/akroma/app_1.1.4_key",
        delete="nanos/1.4.2/akroma/app_1.1.4_del",
        delete_key="nanos/1.4.2/akroma/app_1.1.4_del_key",
        app_id=70
    )
    appVer294.providers.add(1,4)
    appVer294.device_versions.add(6)
    appVer294.se_firmware_final_versions.add(10)
    # 295 , 
    appVer295 = ApplicationVersion.objects.create(
        name="FIC",
        version=196608,
        display_name="FIC",
        icon="fic",
        hash="0f9a41e6d80c3993d75c471d4db5b8e8b528ceec751f6ea053cc1a4e7ff3c260",
        perso="perso_11",
        firmware="blue/2.1.1/fic/app_3.0.0",
        firmware_key="blue/2.1.1/fic/app_3.0.0_key",
        delete="blue/2.1.1/fic/app_3.0.0_del",
        delete_key="blue/2.1.1/fic/app_3.0.0_del_key",
        app_id=64
    )
    appVer295.providers.add(1,4)
    appVer295.device_versions.add(7,8)
    appVer295.se_firmware_final_versions.add(3,4)
    # 296 , 
    appVer296 = ApplicationVersion.objects.create(
        name="Pirl",
        version=65796,
        display_name="Pirl",
        icon="pirl",
        hash="9cb60fef91812e3774aea0fc45680dde139bc0a04512e4ce014a31cdded75cb6",
        perso="perso_11",
        firmware="blue/2.1.1/pirl/app_1.1.4",
        firmware_key="blue/2.1.1/pirl/app_1.1.4_key",
        delete="blue/2.1.1/pirl/app_1.1.4_del",
        delete_key="blue/2.1.1/pirl/app_1.1.4_del_key",
        app_id=67
    )
    appVer296.providers.add(1,4)
    appVer296.device_versions.add(7,8)
    appVer296.se_firmware_final_versions.add(3,4)
    # 297 , 
    appVer297 = ApplicationVersion.objects.create(
        name="Hycon",
        version=512,
        display_name="Hycon",
        icon="hycon",
        hash="7c327582755020f72849620bdaa17d968002f2fe220b94145c31f106ad8355d6",
        perso="perso_11",
        firmware="blue/2.1.1/hycon/app_0.2.0",
        firmware_key="blue/2.1.1/hycon/app_0.2.0_key",
        delete="blue/2.1.1/hycon/app_0.2.0_del",
        delete_key="blue/2.1.1/hycon/app_0.2.0_del_key",
        app_id=69
    )
    appVer297.providers.add(1,4)
    appVer297.device_versions.add(7,8)
    appVer297.se_firmware_final_versions.add(3,4)
    # 298 , 
    appVer298 = ApplicationVersion.objects.create(
        name="Akroma",
        version=65796,
        display_name="Akroma",
        icon="akroma",
        hash="f948f23613d4ccc0d06c65a510d6db57ed80b18366d569dca71b7b79b4165311",
        perso="perso_11",
        firmware="blue/2.1.1/akroma/app_1.1.4",
        firmware_key="blue/2.1.1/akroma/app_1.1.4_key",
        delete="blue/2.1.1/akroma/app_1.1.4_del",
        delete_key="blue/2.1.1/akroma/app_1.1.4_del_key",
        app_id=70
    )
    appVer298.providers.add(1,4)
    appVer298.device_versions.add(7,8)
    appVer298.se_firmware_final_versions.add(3,4)
    # 299 , 
    appVer299 = ApplicationVersion.objects.create(
        name="Horizen",
        version=66056,
        display_name="Horizen",
        icon="horizen",
        hash="2a3206b68c5b75d4d3c73eb6007fb751883db154c1b509ee97c4cba8ba1c69f7",
        perso="perso_11",
        firmware="blue/2.1.1/horizen/app_1.2.8",
        firmware_key="blue/2.1.1/horizen/app_1.2.8_key",
        delete="blue/2.1.1/horizen/app_1.2.8_del",
        delete_key="blue/2.1.1/horizen/app_1.2.8_del_key",
        app_id=71
    )
    appVer299.providers.add(1,4)
    appVer299.device_versions.add(7,8)
    appVer299.se_firmware_final_versions.add(3,4)
    # 300 , 
    appVer300 = ApplicationVersion.objects.create(
        name="Horizen",
        version=66056,
        display_name="Horizen",
        icon="horizen",
        hash="26590c992024f3d3dd96c68642d97535168d21e1535acff5523753581240db09",
        perso="perso_11",
        firmware="nanos/1.4.2/horizen/app_1.2.8",
        firmware_key="nanos/1.4.2/horizen/app_1.2.8_key",
        delete="nanos/1.4.2/horizen/app_1.2.8_del",
        delete_key="nanos/1.4.2/horizen/app_1.2.8_del_key",
        app_id=71
    )
    appVer300.providers.add(1,4)
    appVer300.device_versions.add(6)
    appVer300.se_firmware_final_versions.add(10)
    # 301 , 
    appVer301 = ApplicationVersion.objects.create(
        name="XRP",
        version=65540,
        display_name="XRP",
        icon="xrp",
        hash="50f9e91c9a9b8847e6d749387d2a30e22b956d1cf937e6e73e82660c278fc058",
        perso="perso_11",
        firmware="nanos/1.4.2/XRP/app_1.0.4",
        firmware_key="nanos/1.4.2/XRP/app_1.0.4_key",
        delete="nanos/1.4.2/XRP/app_1.0.4_del",
        delete_key="nanos/1.4.2/XRP/app_1.0.4_del_key",
        app_id=72
    )
    appVer301.providers.add(1,4)
    appVer301.device_versions.add(6)
    appVer301.se_firmware_final_versions.add(10)
    # 302 , 
    appVer302 = ApplicationVersion.objects.create(
        name="XRP",
        version=65540,
        display_name="XRP",
        icon="xrp",
        hash="dfa8c19e7111ec4ca7a6ac82e4db3456a38ee12a5e1797d53fc8666471c50977",
        perso="perso_11",
        firmware="blue/2.1.1/XRP/app_1.0.4",
        firmware_key="blue/2.1.1/XRP/app_1.0.4_key",
        delete="blue/2.1.1/XRP/app_1.0.4_del",
        delete_key="blue/2.1.1/XRP/app_1.0.4_del_key",
        app_id=72
    )
    appVer302.providers.add(1,4)
    appVer302.device_versions.add(7,8)
    appVer302.se_firmware_final_versions.add(3,4)
    # 303 , 
    appVer303 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=66057,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="577426819737db66bf84915c68ee03e85511c130a66ab4334de3e4f4e5e49377",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin/app_1.2.9",
        firmware_key="nanos/1.4.2/bitcoin/app_1.2.9_key",
        delete="nanos/1.4.2/bitcoin/app_1.2.9_del",
        delete_key="nanos/1.4.2/bitcoin/app_1.2.9_del_key",
        app_id=1
    )
    appVer303.providers.add(1,4)
    appVer303.device_versions.add(6)
    appVer303.se_firmware_final_versions.add(10)
    # 304 , 
    appVer304 = ApplicationVersion.objects.create(
        name="Bitcoin Cash",
        version=66057,
        display_name="Bitcoin Cash",
        icon="bitcoin_cash",
        hash="da11e6fa12188a1569a43f0ff50b540f905b61207e783852df365fde331e0d2b",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_cash/app_1.2.9",
        firmware_key="nanos/1.4.2/bitcoin_cash/app_1.2.9_key",
        delete="nanos/1.4.2/bitcoin_cash/app_1.2.9_del",
        delete_key="nanos/1.4.2/bitcoin_cash/app_1.2.9_del_key",
        app_id=2
    )
    appVer304.providers.add(1,4)
    appVer304.device_versions.add(6)
    appVer304.se_firmware_final_versions.add(10)
    # 305 , 
    appVer305 = ApplicationVersion.objects.create(
        name="Bitcoin Gold",
        version=66057,
        display_name="Bitcoin Gold",
        icon="bitcoin_gold",
        hash="25e8ef4e0ee2839eb001f490d54be144fc05b55c883b6f8e7ef487a7bd491982",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_gold/app_1.2.9",
        firmware_key="nanos/1.4.2/bitcoin_gold/app_1.2.9_key",
        delete="nanos/1.4.2/bitcoin_gold/app_1.2.9_del",
        delete_key="nanos/1.4.2/bitcoin_gold/app_1.2.9_del_key",
        app_id=3
    )
    appVer305.providers.add(1,4)
    appVer305.device_versions.add(6)
    appVer305.se_firmware_final_versions.add(10)
    # 306 , 
    appVer306 = ApplicationVersion.objects.create(
        name="Bitcoin Gold",
        version=66057,
        display_name="Bitcoin Gold",
        icon="bitcoin gold",
        hash="25e8ef4e0ee2839eb001f490d54be144fc05b55c883b6f8e7ef487a7bd491982",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_gold/app_1.2.9",
        firmware_key="nanos/1.4.2/bitcoin_gold/app_1.2.9_key",
        delete="nanos/1.4.2/bitcoin_gold/app_1.2.9_del",
        delete_key="nanos/1.4.2/bitcoin_gold/app_1.2.9_del_key",
        app_id=3
    )
    appVer306.providers.add(1,4)
    appVer306.device_versions.add(6)
    appVer306.se_firmware_final_versions.add(10)
    # 307 , 
    appVer307 = ApplicationVersion.objects.create(
        name="Bitcoin Private",
        version=66057,
        display_name="Bitcoin Private",
        icon="bitcoin_private",
        hash="c9208b7326943138115a7eb13d29d582f124881be06da00e54a406435ab24648",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_private/app_1.2.9",
        firmware_key="nanos/1.4.2/bitcoin_private/app_1.2.9_key",
        delete="nanos/1.4.2/bitcoin_private/app_1.2.9_del",
        delete_key="nanos/1.4.2/bitcoin_private/app_1.2.9_del_key",
        app_id=4
    )
    appVer307.providers.add(1,4)
    appVer307.device_versions.add(6)
    appVer307.se_firmware_final_versions.add(10)
    # 308 , 
    appVer308 = ApplicationVersion.objects.create(
        name="Bitcoin testnet",
        version=66057,
        display_name="Bitcoin testnet",
        icon="bitcoin_testnet",
        hash="7ba8ba6b503343ce46b735e957a59b88ea0ae28dcace9797baaa5ca4954127b8",
        perso="perso_11",
        firmware="nanos/1.4.2/bitcoin_testnet/app_1.2.9",
        firmware_key="nanos/1.4.2/bitcoin_testnet/app_1.2.9_key",
        delete="nanos/1.4.2/bitcoin_testnet/app_1.2.9_del",
        delete_key="nanos/1.4.2/bitcoin_testnet/app_1.2.9_del_key",
        app_id=5
    )
    appVer308.providers.add(1,4)
    appVer308.device_versions.add(6)
    appVer308.se_firmware_final_versions.add(10)
    # 309 , 
    appVer309 = ApplicationVersion.objects.create(
        name="Dash",
        version=66057,
        display_name="Dash",
        icon="dash",
        hash="42ccf84cb685ea91b5c8d5d00a5b6486ed99e223f5a6acc6baf68772de99f1b9",
        perso="perso_11",
        firmware="nanos/1.4.2/dash/app_1.2.9",
        firmware_key="nanos/1.4.2/dash/app_1.2.9_key",
        delete="nanos/1.4.2/dash/app_1.2.9_del",
        delete_key="nanos/1.4.2/dash/app_1.2.9_del_key",
        app_id=16
    )
    appVer309.providers.add(1,4)
    appVer309.device_versions.add(6)
    appVer309.se_firmware_final_versions.add(10)
    # 310 , 
    appVer310 = ApplicationVersion.objects.create(
        name="Digibyte",
        version=66057,
        display_name="Digibyte",
        icon="digibyte",
        hash="2304bd64ef447bcf4fcd98efb78c942f47b05b243f787ce3d43652a292dff73b",
        perso="perso_11",
        firmware="nanos/1.4.2/digibyte/app_1.2.9",
        firmware_key="nanos/1.4.2/digibyte/app_1.2.9_key",
        delete="nanos/1.4.2/digibyte/app_1.2.9_del",
        delete_key="nanos/1.4.2/digibyte/app_1.2.9_del_key",
        app_id=6
    )
    appVer310.providers.add(1,4)
    appVer310.device_versions.add(6)
    appVer310.se_firmware_final_versions.add(10)
    # 311 , 
    appVer311 = ApplicationVersion.objects.create(
        name="Dogecoin",
        version=66057,
        display_name="Dogecoin",
        icon="dogecoin",
        hash="e17e1c0906d383b1a8fecfb7447601b3850608b781a53931245ce52b3df58de9",
        perso="perso_11",
        firmware="nanos/1.4.2/dogecoin/app_1.2.9",
        firmware_key="nanos/1.4.2/dogecoin/app_1.2.9_key",
        delete="nanos/1.4.2/dogecoin/app_1.2.9_del",
        delete_key="nanos/1.4.2/dogecoin/app_1.2.9_del_key",
        app_id=17
    )
    appVer311.providers.add(1,4)
    appVer311.device_versions.add(6)
    appVer311.se_firmware_final_versions.add(10)
    # 312 , 
    appVer312 = ApplicationVersion.objects.create(
        name="HCash",
        version=66057,
        display_name="HCash",
        icon="hcash",
        hash="ee2ee52f333ac42231bcb4b9c295ca91b688e516a24053cee5bc57ab6ee75963",
        perso="perso_11",
        firmware="nanos/1.4.2/hcash/app_1.2.9",
        firmware_key="nanos/1.4.2/hcash/app_1.2.9_key",
        delete="nanos/1.4.2/hcash/app_1.2.9_del",
        delete_key="nanos/1.4.2/hcash/app_1.2.9_del_key",
        app_id=7
    )
    appVer312.providers.add(1,4)
    appVer312.device_versions.add(6)
    appVer312.se_firmware_final_versions.add(10)
    # 313 , 
    appVer313 = ApplicationVersion.objects.create(
        name="Horizen",
        version=66057,
        display_name="Horizen",
        icon="horizen",
        hash="c3ce096300c6c52351675913fc000c2a9bd80208a68644cacde9dddc19d6cace",
        perso="perso_11",
        firmware="nanos/1.4.2/horizen/app_1.2.9",
        firmware_key="nanos/1.4.2/horizen/app_1.2.9_key",
        delete="nanos/1.4.2/horizen/app_1.2.9_del",
        delete_key="nanos/1.4.2/horizen/app_1.2.9_del_key",
        app_id=71
    )
    appVer313.providers.add(1,4)
    appVer313.device_versions.add(6)
    appVer313.se_firmware_final_versions.add(10)
    # 314 , 
    appVer314 = ApplicationVersion.objects.create(
        name="ICON",
        version=65538,
        display_name="ICON",
        icon="icon",
        hash="42fe55f627eaa2cae747f5ae868608bc779f710f3a5ce8ecd63258e80b5436dc",
        perso="perso_11",
        firmware="nanos/1.4.2/icon/app_1.0.2",
        firmware_key="nanos/1.4.2/icon/app_1.0.2_key",
        delete="nanos/1.4.2/icon/app_1.0.2_del",
        delete_key="nanos/1.4.2/icon/app_1.0.2_del_key",
        app_id=51
    )
    appVer314.providers.add(1,4)
    appVer314.device_versions.add(6)
    appVer314.se_firmware_final_versions.add(10)
    # 315 , 
    appVer315 = ApplicationVersion.objects.create(
        name="ICON testnet",
        version=65538,
        display_name="ICON testnet",
        icon="icon_testnet",
        hash="821a0a58232e38e211b8473b8acf0bdb928759e91b2c9eff20065329b7cba688",
        perso="perso_11",
        firmware="nanos/1.4.2/icon_testnet/app_1.0.2",
        firmware_key="nanos/1.4.2/icon_testnet/app_1.0.2_key",
        delete="nanos/1.4.2/icon_testnet/app_1.0.2_del",
        delete_key="nanos/1.4.2/icon_testnet/app_1.0.2_del_key",
        app_id=61
    )
    appVer315.providers.add(1,4)
    appVer315.device_versions.add(6)
    appVer315.se_firmware_final_versions.add(10)
    # 316 , 
    appVer316 = ApplicationVersion.objects.create(
        name="Komodo",
        version=66057,
        display_name="Komodo",
        icon="komodo",
        hash="22a97583d5a7fb74dbf4befe63297c3d23f0381d4f35282dea4a361267d965cf",
        perso="perso_11",
        firmware="nanos/1.4.2/komodo/app_1.2.9",
        firmware_key="nanos/1.4.2/komodo/app_1.2.9_key",
        delete="nanos/1.4.2/komodo/app_1.2.9_del",
        delete_key="nanos/1.4.2/komodo/app_1.2.9_del_key",
        app_id=25
    )
    appVer316.providers.add(1,4)
    appVer316.device_versions.add(6)
    appVer316.se_firmware_final_versions.add(10)
    # 317 , 
    appVer317 = ApplicationVersion.objects.create(
        name="Litecoin",
        version=66057,
        display_name="Litecoin",
        icon="litecoin",
        hash="fb7d250c0408cf2e3c563689f4dd9d76b0a49985217003b2d2806611e56d857f",
        perso="perso_11",
        firmware="nanos/1.4.2/litecoin/app_1.2.9",
        firmware_key="nanos/1.4.2/litecoin/app_1.2.9_key",
        delete="nanos/1.4.2/litecoin/app_1.2.9_del",
        delete_key="nanos/1.4.2/litecoin/app_1.2.9_del_key",
        app_id=20
    )
    appVer317.providers.add(1,4)
    appVer317.device_versions.add(6)
    appVer317.se_firmware_final_versions.add(10)
    # 318 , 
    appVer318 = ApplicationVersion.objects.create(
        name="Peercoin",
        version=66057,
        display_name="Peercoin",
        icon="peercoin",
        hash="603fcc59891ec8049603d67c900c9ae5e78a11d913333b391d972d78b3f8b7e1",
        perso="perso_11",
        firmware="nanos/1.4.2/peercoin/app_1.2.9",
        firmware_key="nanos/1.4.2/peercoin/app_1.2.9_key",
        delete="nanos/1.4.2/peercoin/app_1.2.9_del",
        delete_key="nanos/1.4.2/peercoin/app_1.2.9_del_key",
        app_id=12
    )
    appVer318.providers.add(1,4)
    appVer318.device_versions.add(6)
    appVer318.se_firmware_final_versions.add(10)
    # 319 , 
    appVer319 = ApplicationVersion.objects.create(
        name="PivX",
        version=66057,
        display_name="PivX",
        icon="pivx",
        hash="27eed53441f55a67c37db575585be8c58cd0531c22a518d94952be14b3215f1b",
        perso="perso_11",
        firmware="nanos/1.4.2/pivx/app_1.2.9",
        firmware_key="nanos/1.4.2/pivx/app_1.2.9_key",
        delete="nanos/1.4.2/pivx/app_1.2.9_del",
        delete_key="nanos/1.4.2/pivx/app_1.2.9_del_key",
        app_id=9
    )
    appVer319.providers.add(1,4)
    appVer319.device_versions.add(6)
    appVer319.se_firmware_final_versions.add(10)
    # 320 , 
    appVer320 = ApplicationVersion.objects.create(
        name="PoSW",
        version=66057,
        display_name="PoSW",
        icon="posw",
        hash="1eddb096138547c9d2f12d82bcc0d54768f31216a223ebbcf3d45d3a3db8b587",
        perso="perso_11",
        firmware="nanos/1.4.2/posw/app_1.2.9",
        firmware_key="nanos/1.4.2/posw/app_1.2.9_key",
        delete="nanos/1.4.2/posw/app_1.2.9_del",
        delete_key="nanos/1.4.2/posw/app_1.2.9_del_key",
        app_id=26
    )
    appVer320.providers.add(1,4)
    appVer320.device_versions.add(6)
    appVer320.se_firmware_final_versions.add(10)
    # 321 , 
    appVer321 = ApplicationVersion.objects.create(
        name="Qtum",
        version=66057,
        display_name="Qtum",
        icon="qtum",
        hash="8fce816325f1ec8bbf45c7f5916299580a4a05e1f57dda3d10e0217fdf892bd2",
        perso="perso_11",
        firmware="nanos/1.4.2/qtum/app_1.2.9",
        firmware_key="nanos/1.4.2/qtum/app_1.2.9_key",
        delete="nanos/1.4.2/qtum/app_1.2.9_del",
        delete_key="nanos/1.4.2/qtum/app_1.2.9_del_key",
        app_id=8
    )
    appVer321.providers.add(1,4)
    appVer321.device_versions.add(6)
    appVer321.se_firmware_final_versions.add(10)
    # 322 , 
    appVer322 = ApplicationVersion.objects.create(
        name="Stealth",
        version=66057,
        display_name="Stealth",
        icon="stealthcoin",
        hash="598cddeb78aaed0e530dd71046733b4211732587e65c46b7f64b89a99c38cddb",
        perso="perso_11",
        firmware="nanos/1.4.2/stealth/app_1.2.9",
        firmware_key="nanos/1.4.2/stealth/app_1.2.9_key",
        delete="nanos/1.4.2/stealth/app_1.2.9_del",
        delete_key="nanos/1.4.2/stealth/app_1.2.9_del_key",
        app_id=10
    )
    appVer322.providers.add(1,4)
    appVer322.device_versions.add(6)
    appVer322.se_firmware_final_versions.add(10)
    # 323 , 
    appVer323 = ApplicationVersion.objects.create(
        name="Stratis",
        version=66057,
        display_name="Stratis",
        icon="stratis",
        hash="a4f537ff09e9f44325cd69237d366811f1aea69eb844f09eba56b6c6864053d2",
        perso="perso_11",
        firmware="nanos/1.4.2/stratis/app_1.2.9",
        firmware_key="nanos/1.4.2/stratis/app_1.2.9_key",
        delete="nanos/1.4.2/stratis/app_1.2.9_del",
        delete_key="nanos/1.4.2/stratis/app_1.2.9_del_key",
        app_id=21
    )
    appVer323.providers.add(1,4)
    appVer323.device_versions.add(6)
    appVer323.se_firmware_final_versions.add(10)
    # 324 , 
    appVer324 = ApplicationVersion.objects.create(
        name="Vertcoin",
        version=66057,
        display_name="Vertcoin",
        icon="vertcoin",
        hash="48db63b63570920574c86697373ee19b16916dba393bd5699af37f6c6f4aa95c",
        perso="perso_11",
        firmware="nanos/1.4.2/vertcoin/app_1.2.9",
        firmware_key="nanos/1.4.2/vertcoin/app_1.2.9_key",
        delete="nanos/1.4.2/vertcoin/app_1.2.9_del",
        delete_key="nanos/1.4.2/vertcoin/app_1.2.9_del_key",
        app_id=11
    )
    appVer324.providers.add(1,4)
    appVer324.device_versions.add(6)
    appVer324.se_firmware_final_versions.add(10)
    # 325 , 
    appVer325 = ApplicationVersion.objects.create(
        name="Viacoin",
        version=66057,
        display_name="Viacoin",
        icon="viacoin",
        hash="55ebd0d7534d66f959400eada88fd7b3c49a8a13454afb33e4945b82d1cb5742",
        perso="perso_11",
        firmware="nanos/1.4.2/viacoin/app_1.2.9",
        firmware_key="nanos/1.4.2/viacoin/app_1.2.9_key",
        delete="nanos/1.4.2/viacoin/app_1.2.9_del",
        delete_key="nanos/1.4.2/viacoin/app_1.2.9_del_key",
        app_id=13
    )
    appVer325.providers.add(1,4)
    appVer325.device_versions.add(6)
    appVer325.se_firmware_final_versions.add(10)
    # 326 , 
    appVer326 = ApplicationVersion.objects.create(
        name="XRP",
        version=65542,
        display_name="XRP",
        icon="xrp",
        hash="cf66ef5243b55c9e021ee5b334125fb30033c7c6223aac3b799ab1468b963c69",
        perso="perso_11",
        firmware="nanos/1.4.2/xrp/app_1.0.6",
        firmware_key="nanos/1.4.2/xrp/app_1.0.6_key",
        delete="nanos/1.4.2/xrp/app_1.0.6_del",
        delete_key="nanos/1.4.2/xrp/app_1.0.6_del_key",
        app_id=72
    )
    appVer326.providers.add(1,4)
    appVer326.device_versions.add(6)
    appVer326.se_firmware_final_versions.add(10)
    # 327 , 
    appVer327 = ApplicationVersion.objects.create(
        name="Zcash",
        version=66057,
        display_name="Zcash",
        icon="zcash",
        hash="b0534569abd692a104c75936e2e247fc3d3509c631cf6d1bc39c061df05e4d01",
        perso="perso_11",
        firmware="nanos/1.4.2/zcash/app_1.2.9",
        firmware_key="nanos/1.4.2/zcash/app_1.2.9_key",
        delete="nanos/1.4.2/zcash/app_1.2.9_del",
        delete_key="nanos/1.4.2/zcash/app_1.2.9_del_key",
        app_id=23
    )
    appVer327.providers.add()
    appVer327.device_versions.add(6)
    appVer327.se_firmware_final_versions.add(10)
    # 328 , 
    appVer328 = ApplicationVersion.objects.create(
        name="Zcoin",
        version=66057,
        display_name="Zcoin",
        icon="zcoin",
        hash="190ebc3d979446666327db3314ea27b0acf1ad000096ef087319df8a7e317c71",
        perso="perso_11",
        firmware="nanos/1.4.2/zcoin/app_1.2.9",
        firmware_key="nanos/1.4.2/zcoin/app_1.2.9_key",
        delete="nanos/1.4.2/zcoin/app_1.2.9_del",
        delete_key="nanos/1.4.2/zcoin/app_1.2.9_del_key",
        app_id=46
    )
    appVer328.providers.add(1,4)
    appVer328.device_versions.add(6)
    appVer328.se_firmware_final_versions.add(10)
    # 329 , 
    appVer329 = ApplicationVersion.objects.create(
        name="Bitcoin",
        version=66057,
        display_name="Bitcoin",
        icon="bitcoin",
        hash="23c118683e0dc8d2cb7e5ef4843e22a96d82651707e738bea941fbb0aa95a8a5",
        perso="perso_11",
        firmware="blue/2.1.1/bitcoin/app_1.2.9",
        firmware_key="blue/2.1.1/bitcoin/app_1.2.9_key",
        delete="blue/2.1.1/bitcoin/app_1.2.9_del",
        delete_key="blue/2.1.1/bitcoin/app_1.2.9_del_key",
        app_id=1
    )
    appVer329.providers.add(1,4)
    appVer329.device_versions.add(7,8)
    appVer329.se_firmware_final_versions.add(3,4)
    # 330 , 
    appVer330 = ApplicationVersion.objects.create(
        name="Bitcoin Cash",
        version=66057,
        display_name="Bitcoin Cash",
        icon="bitcoin_cash",
        hash="070d5b7f57c94fb74dcf50bba6870e574a0226b972611e22ab84984dff72f5a6",
        perso="perso_11",
        firmware="blue/2.1.1/bitcoin_cash/app_1.2.9",
        firmware_key="blue/2.1.1/bitcoin_cash/app_1.2.9_key",
        delete="blue/2.1.1/bitcoin_cash/app_1.2.9_del",
        delete_key="blue/2.1.1/bitcoin_cash/app_1.2.9_del_key",
        app_id=2
    )
    appVer330.providers.add(1,4)
    appVer330.device_versions.add(7,8)
    appVer330.se_firmware_final_versions.add(3,4)
    # 331 , 
    appVer331 = ApplicationVersion.objects.create(
        name="Bitcoin Gold",
        version=66057,
        display_name="Bitcoin Gold",
        icon="bitcoin_gold",
        hash="e893f8d4cb27eee3e477a37c4af6fb913bb9b8c65cd5e363f3b4758b145c8fd9",
        perso="perso_11",
        firmware="blue/2.1.1/bitcoin_gold/app_1.2.9",
        firmware_key="blue/2.1.1/bitcoin_gold/app_1.2.9_key",
        delete="blue/2.1.1/bitcoin_gold/app_1.2.9_del",
        delete_key="blue/2.1.1/bitcoin_gold/app_1.2.9_del_key",
        app_id=3
    )
    appVer331.providers.add(1,4)
    appVer331.device_versions.add(7,8)
    appVer331.se_firmware_final_versions.add(3,4)
    # 332 , 
    appVer332 = ApplicationVersion.objects.create(
        name="Bitcoin Private",
        version=66057,
        display_name="Bitcoin Private",
        icon="bitcoin_private",
        hash="629e18607b184eaac5dda3f0e9479d35bfce1ba1995c942faa8af20d01441e76",
        perso="perso_11",
        firmware="blue/2.1.1/bitcoin_private/app_1.2.9",
        firmware_key="blue/2.1.1/bitcoin_private/app_1.2.9_key",
        delete="blue/2.1.1/bitcoin_private/app_1.2.9_del",
        delete_key="blue/2.1.1/bitcoin_private/app_1.2.9_del_key",
        app_id=4
    )
    appVer332.providers.add(1,4)
    appVer332.device_versions.add(7,8)
    appVer332.se_firmware_final_versions.add(3,4)
    # 333 , 
    appVer333 = ApplicationVersion.objects.create(
        name="Bitcoin Test",
        version=66057,
        display_name="Bitcoin Test",
        icon="bitcoin_testnet",
        hash="a4045054c48f16e452894d659db4b2a2861356f28c88e0ffbe27a8771b58f494",
        perso="perso_11",
        firmware="blue/2.1.1/bitcoin_testnet/app_1.2.9",
        firmware_key="blue/2.1.1/bitcoin_testnet/app_1.2.9_key",
        delete="blue/2.1.1/bitcoin_testnet/app_1.2.9_del",
        delete_key="blue/2.1.1/bitcoin_testnet/app_1.2.9_del_key",
        app_id=5
    )
    appVer333.providers.add(1,4)
    appVer333.device_versions.add(7,8)
    appVer333.se_firmware_final_versions.add(3,4)
    # 334 , 
    appVer334 = ApplicationVersion.objects.create(
        name="Dash",
        version=66057,
        display_name="Dash",
        icon="dash",
        hash="20e8a1721d441da35262ff5c2451e3ca1acb70b7acb7215723df877763b3e50e",
        perso="perso_11",
        firmware="blue/2.1.1/dash/app_1.2.9",
        firmware_key="blue/2.1.1/dash/app_1.2.9_key",
        delete="blue/2.1.1/dash/app_1.2.9_del",
        delete_key="blue/2.1.1/dash/app_1.2.9_del_key",
        app_id=16
    )
    appVer334.providers.add(1,4)
    appVer334.device_versions.add(7,8)
    appVer334.se_firmware_final_versions.add(3,4)
    # 335 , 
    appVer335 = ApplicationVersion.objects.create(
        name="Digibyte",
        version=66057,
        display_name="Digibyte",
        icon="digibyte",
        hash="cf31af541dc1baf5ba6db9e5a06ca8613b868f07f76bc2e3b9ac0d0383b2cae5",
        perso="perso_11",
        firmware="blue/2.1.1/digibyte/app_1.2.9",
        firmware_key="blue/2.1.1/digibyte/app_1.2.9_key",
        delete="blue/2.1.1/digibyte/app_1.2.9_del",
        delete_key="blue/2.1.1/digibyte/app_1.2.9_del_key",
        app_id=6
    )
    appVer335.providers.add(1,4)
    appVer335.device_versions.add(7,8)
    appVer335.se_firmware_final_versions.add(3,4)
    # 336 , 
    appVer336 = ApplicationVersion.objects.create(
        name="Dogecoin",
        version=66057,
        display_name="Dogecoin",
        icon="dogecoin",
        hash="20b383ae3480bc1fd0d6136516468d0e695484bbda6fce41eaed375325f2912f",
        perso="perso_11",
        firmware="blue/2.1.1/dogecoin/app_1.2.9",
        firmware_key="blue/2.1.1/dogecoin/app_1.2.9_key",
        delete="blue/2.1.1/dogecoin/app_1.2.9_del",
        delete_key="blue/2.1.1/dogecoin/app_1.2.9_del_key",
        app_id=17
    )
    appVer336.providers.add(1,4)
    appVer336.device_versions.add(7,8)
    appVer336.se_firmware_final_versions.add(3,4)
    # 337 , 
    appVer337 = ApplicationVersion.objects.create(
        name="HCash",
        version=66057,
        display_name="HCash",
        icon="hcash",
        hash="c435cb7ac7b1374b15a9ba958f923576c79b67a6e22eb66865d83198da532daa",
        perso="perso_11",
        firmware="blue/2.1.1/hcash/app_1.2.9",
        firmware_key="blue/2.1.1/hcash/app_1.2.9_key",
        delete="blue/2.1.1/hcash/app_1.2.9_del",
        delete_key="blue/2.1.1/hcash/app_1.2.9_del_key",
        app_id=7
    )
    appVer337.providers.add(1,4)
    appVer337.device_versions.add(7,8)
    appVer337.se_firmware_final_versions.add(3,4)
    # 338 , 
    appVer338 = ApplicationVersion.objects.create(
        name="Horizen",
        version=66057,
        display_name="Horizen",
        icon="horizen",
        hash="adeab9aff2a83c6cf1ffbf2e3254f8b69aa44b3603f869ff1cf02729af9c0fd1",
        perso="perso_11",
        firmware="blue/2.1.1/horizen/app_1.2.9",
        firmware_key="blue/2.1.1/horizen/app_1.2.9_key",
        delete="blue/2.1.1/horizen/app_1.2.9_del",
        delete_key="blue/2.1.1/horizen/app_1.2.9_del_key",
        app_id=71
    )
    appVer338.providers.add(1,4)
    appVer338.device_versions.add(7,8)
    appVer338.se_firmware_final_versions.add(3,4)
    # 339 , 
    appVer339 = ApplicationVersion.objects.create(
        name="Komodo",
        version=66057,
        display_name="Komodo",
        icon="komodo",
        hash="6e0dbc9b74199e25c9c7b822f2964edf2fa9f92ebe93aba7a375fe87868b6fe0",
        perso="perso_11",
        firmware="blue/2.1.1/komodo/app_1.2.9",
        firmware_key="blue/2.1.1/komodo/app_1.2.9_key",
        delete="blue/2.1.1/komodo/app_1.2.9_del",
        delete_key="blue/2.1.1/komodo/app_1.2.9_del_key",
        app_id=25
    )
    appVer339.providers.add(1,4)
    appVer339.device_versions.add(7,8)
    appVer339.se_firmware_final_versions.add(3,4)
    # 340 , 
    appVer340 = ApplicationVersion.objects.create(
        name="Litecoin",
        version=66057,
        display_name="Litecoin",
        icon="litecoin",
        hash="37dd5889ab15e19431af2843c77b7771205491e8d95fda4402cc888ab8c48a78",
        perso="perso_11",
        firmware="blue/2.1.1/litecoin/app_1.2.9",
        firmware_key="blue/2.1.1/litecoin/app_1.2.9_key",
        delete="blue/2.1.1/litecoin/app_1.2.9_del",
        delete_key="blue/2.1.1/litecoin/app_1.2.9_del_key",
        app_id=20
    )
    appVer340.providers.add(1,4)
    appVer340.device_versions.add(7,8)
    appVer340.se_firmware_final_versions.add(3,4)
    # 341 , 
    appVer341 = ApplicationVersion.objects.create(
        name="Peercoin",
        version=66057,
        display_name="Peercoin",
        icon="peercoin",
        hash="fdddf8ae6130f0c2511066ba452863c1f8c536f8cda8051ec7da7809d24e0a7a",
        perso="perso_11",
        firmware="blue/2.1.1/peercoin/app_1.2.9",
        firmware_key="blue/2.1.1/peercoin/app_1.2.9_key",
        delete="blue/2.1.1/peercoin/app_1.2.9_del",
        delete_key="blue/2.1.1/peercoin/app_1.2.9_del_key",
        app_id=12
    )
    appVer341.providers.add(1,4)
    appVer341.device_versions.add(7,8)
    appVer341.se_firmware_final_versions.add(3,4)
    # 342 , 
    appVer342 = ApplicationVersion.objects.create(
        name="PivX",
        version=66057,
        display_name="PivX",
        icon="pivx",
        hash="fd88bf94f8f601d699656b1ef366212b7c76332521149c40df210c705b40de92",
        perso="perso_11",
        firmware="blue/2.1.1/pivx/app_1.2.9",
        firmware_key="blue/2.1.1/pivx/app_1.2.9_key",
        delete="blue/2.1.1/pivx/app_1.2.9_del",
        delete_key="blue/2.1.1/pivx/app_1.2.9_del_key",
        app_id=9
    )
    appVer342.providers.add(1,4)
    appVer342.device_versions.add(7,8)
    appVer342.se_firmware_final_versions.add(3,4)
    # 343 , 
    appVer343 = ApplicationVersion.objects.create(
        name="PoSW",
        version=66057,
        display_name="PoSW",
        icon="posw",
        hash="e20759f01f85f332cdd8e8e2c3174b725ec638902c9129c627bdbf74000654c1",
        perso="perso_11",
        firmware="blue/2.1.1/posw/app_1.2.9",
        firmware_key="blue/2.1.1/posw/app_1.2.9_key",
        delete="blue/2.1.1/posw/app_1.2.9_del",
        delete_key="blue/2.1.1/posw/app_1.2.9_del_key",
        app_id=26
    )
    appVer343.providers.add(1,4)
    appVer343.device_versions.add(7,8)
    appVer343.se_firmware_final_versions.add(3,4)
    # 344 , 
    appVer344 = ApplicationVersion.objects.create(
        name="Qtum",
        version=66057,
        display_name="Qtum",
        icon="qtum",
        hash="b48527ca4860d9fcd2aacefe7b427a1ed7efe1fe377abe3a85ad0f902e6fa089",
        perso="perso_11",
        firmware="blue/2.1.1/qtum/app_1.2.9",
        firmware_key="blue/2.1.1/qtum/app_1.2.9_key",
        delete="blue/2.1.1/qtum/app_1.2.9_del",
        delete_key="blue/2.1.1/qtum/app_1.2.9_del_key",
        app_id=8
    )
    appVer344.providers.add(1,4)
    appVer344.device_versions.add(7,8)
    appVer344.se_firmware_final_versions.add(3,4)
    # 345 , 
    appVer345 = ApplicationVersion.objects.create(
        name="Stealth",
        version=66057,
        display_name="Stealth",
        icon="stealthcoin",
        hash="ea08e98ae7b441bf3c1504aa23dec082cc662d7bb73bae2010064904ebab5682",
        perso="perso_11",
        firmware="blue/2.1.1/stealth/app_1.2.9",
        firmware_key="blue/2.1.1/stealth/app_1.2.9_key",
        delete="blue/2.1.1/stealth/app_1.2.9_del",
        delete_key="blue/2.1.1/stealth/app_1.2.9_del_key",
        app_id=10
    )
    appVer345.providers.add(1,4)
    appVer345.device_versions.add(7,8)
    appVer345.se_firmware_final_versions.add(3,4)
    # 346 , 
    appVer346 = ApplicationVersion.objects.create(
        name="Stratis",
        version=66057,
        display_name="Stratis",
        icon="stratis",
        hash="b61ace5e7ce446843ed1ac827e3e31ccdcb906a38f5572e2925a80a361ec9948",
        perso="perso_11",
        firmware="blue/2.1.1/stratis/app_1.2.9",
        firmware_key="blue/2.1.1/stratis/app_1.2.9_key",
        delete="blue/2.1.1/stratis/app_1.2.9_del",
        delete_key="blue/2.1.1/stratis/app_1.2.9_del_key",
        app_id=21
    )
    appVer346.providers.add(1,4)
    appVer346.device_versions.add(7,8)
    appVer346.se_firmware_final_versions.add(3,4)
    # 347 , 
    appVer347 = ApplicationVersion.objects.create(
        name="Vertcoin",
        version=66057,
        display_name="Vertcoin",
        icon="vertcoin",
        hash="986fcc139e4ca729c2f2805b95949491b803637b9a8d812fdeaa220d52a6c754",
        perso="perso_11",
        firmware="blue/2.1.1/vertcoin/app_1.2.9",
        firmware_key="blue/2.1.1/vertcoin/app_1.2.9_key",
        delete="blue/2.1.1/vertcoin/app_1.2.9_del",
        delete_key="blue/2.1.1/vertcoin/app_1.2.9_del_key",
        app_id=11
    )
    appVer347.providers.add(1,4)
    appVer347.device_versions.add(7,8)
    appVer347.se_firmware_final_versions.add(3,4)
    # 348 , 
    appVer348 = ApplicationVersion.objects.create(
        name="Viacoin",
        version=66057,
        display_name="Viacoin",
        icon="viacoin",
        hash="f229f87f6ece39b5e43733eb0829ffd550a3d0ae0b4f207556c03cf12ad50d02",
        perso="perso_11",
        firmware="blue/2.1.1/viacoin/app_1.2.9",
        firmware_key="blue/2.1.1/viacoin/app_1.2.9_key",
        delete="blue/2.1.1/viacoin/app_1.2.9_del",
        delete_key="blue/2.1.1/viacoin/app_1.2.9_del_key",
        app_id=13
    )
    appVer348.providers.add(1,4)
    appVer348.device_versions.add(7,8)
    appVer348.se_firmware_final_versions.add(3,4)
    # 349 , 
    appVer349 = ApplicationVersion.objects.create(
        name="XRP",
        version=65542,
        display_name="XRP",
        icon="xrp",
        hash="782650f08482ddac5f7e3e1c7917f0ef1cb932be171f129365dff9f0a1da28d4",
        perso="perso_11",
        firmware="blue/2.1.1/xrp/app_1.0.6",
        firmware_key="blue/2.1.1/xrp/app_1.0.6_key",
        delete="blue/2.1.1/xrp/app_1.0.6_del",
        delete_key="blue/2.1.1/xrp/app_1.0.6_del_key",
        app_id=72
    )
    appVer349.providers.add(1,4)
    appVer349.device_versions.add(7,8)
    appVer349.se_firmware_final_versions.add(3,4)
    # 350 , 
    appVer350 = ApplicationVersion.objects.create(
        name="Zcash",
        version=66057,
        display_name="Zcash",
        icon="zcash",
        hash="c15208ebf14dcec8d31e9bccf1835cc5de5f86f577bdfebffc057f61e578b6ef",
        perso="perso_11",
        firmware="blue/2.1.1/zcash/app_1.2.9",
        firmware_key="blue/2.1.1/zcash/app_1.2.9_key",
        delete="blue/2.1.1/zcash/app_1.2.9_del",
        delete_key="blue/2.1.1/zcash/app_1.2.9_del_key",
        app_id=23
    )
    appVer350.providers.add()
    appVer350.device_versions.add()
    appVer350.se_firmware_final_versions.add()
    # 351 , 
    appVer351 = ApplicationVersion.objects.create(
        name="Zcoin",
        version=66057,
        display_name="Zcoin",
        icon="zcoin",
        hash="69b19e78584be8e317fca43796dceef3c98ddc6f97362c8ae94e1ba256a19fc1",
        perso="perso_11",
        firmware="blue/2.1.1/zcoin/app_1.2.9",
        firmware_key="blue/2.1.1/zcoin/app_1.2.9_key",
        delete="blue/2.1.1/zcoin/app_1.2.9_del",
        delete_key="blue/2.1.1/zcoin/app_1.2.9_del_key",
        app_id=46
    )
    appVer351.providers.add(1,4)
    appVer351.device_versions.add(7,8)
    appVer351.se_firmware_final_versions.add(3,4)
    # 352 , 
    appVer352 = ApplicationVersion.objects.create(
        name="Vault",
        version=65549,
        display_name="Vault",
        icon="vault",
        hash="5b264b14861cfd0086b045cb30c8d72002babbe5ab761a784c6cc27194e1cf9e",
        perso="perso_11",
        firmware="blue/2.1.1-ee/vault3/vault-1.0.13_sdk-2.1.1-ee",
        firmware_key="blue/2.1.1-ee/vault3/vault-1.0.13_sdk-2.1.1-ee_key",
        delete="blue/2.1.1-ee/vault3/app_del",
        delete_key="blue/2.1.1-ee/vault3/app_del_key",
        app_id=50
    )
    appVer352.providers.add(4,5)
    appVer352.device_versions.add(7,8)
    appVer352.se_firmware_final_versions.add(firmware_final_ver8)
