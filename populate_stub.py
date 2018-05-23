import django
import os
import semver

os.environ['DJANGO_SETTINGS_MODULE'] = 'ledger_app_store.settings'
django.setup()
from api.models import *

devices = {
    "nanos": {
        "name": "Ledger Nano S",
        "targetId": 823132162
    },
    "blue_2": {
        "name": "Ledger Blue",
        "targetId": 822083586
    },
    "blue_1": {
        "name": "Ledger Blue",
        "targetId": 822083585
    },
    "aramis": {
        "name": "Ledger Aramis",
        "targetId": 824180738
    },
    "nanos-1.4": {
        "name": "Ledger Nano S",
        "targetId": 823132163
    }
}

firmwares = {
    "nanos-1.4": [
        {
            "bolos_version": {
                "min": "1.4.1-osu",
                "max": "1.4.1-osu"
            },
            "name": "1.4.1",
            "identifier": "afb2033260e6a397430df3f3a5cda276292fb28fba3831a4e4b192bbe0c5b2d1",
            "osu": {
                "perso": "perso_11",
                "targetId": "",
                "firmware": "nanos/1.4.1/upgrade_osu_1.4.1",
                "firmwareKey": "nanos/1.4.1/upgrade_osu_1.4.1_key",
                "hash": "2e88ef1ce8e01b181a9083950196dd0b99c6240198728b54b18bfe179856f573"
            },
            "final": {
                "perso": "perso_11",
                "targetId": 823132163,
                "firmware": "nanos/1.4.1/upgrade_1.4.1",
                "firmwareKey": "nanos/1.4.1/upgrade_1.4.1_key",
                "hash": "74d10f134677adb030bafce8adb70c6510e7181a9aae509159f904be01edeed2"
            }
        },
        {
            "bolos_version": {
                "min": "1.4.2-osu",
                "max": "1.4.2-osu"
            },
            "name": "1.4.2",
            "identifier": "02480d50b1d197d70b5134efd6a020bc990071d7cda5bac27344ba0f3bf5d05d",
            "osu": {
                "perso": "perso_11",
                "targetId": 823132163,
                "firmware": "nanos/1.4.2/fw_1.4.1/upgrade_osu_1.4.2",
                "firmwareKey": "nanos/1.4.2/fw_1.4.1/upgrade_osu_1.4.2_key",
                "hash": "fbc17a950ff7576fdb22442cba6b9f32011025b4c331f44b2d6e85811e96d522"
            },
            "final": {
                "perso": "perso_11",
                "targetId": 823132163,
                "firmware": "nanos/1.4.2/fw_1.4.1/upgrade_1.4.2",
                "firmwareKey": "nanos/1.4.2/fw_1.4.1/upgrade_1.4.2_key",
                "hash": "8309d76fee0e809f22d4a00960b795ffdc631970cdd4b9c2a547f6c7cad3ea48"
            }
        }
    ],
    "nanos": [
        {
            "bolos_version": {
                "min": "1.3.1",
                "max": "1.3.1"
            },
            "notes": "The firmware 1.4.2 update brings several user experience and minor security improvements:\n- User Pin code's start number is now always randomized\n- Each recovery word's first letter is now always randomized\n- Improvement of the interaction between microcontroller (MCU) and secure element to remove confusing error message\n- Verification & checks of installed applications\n- Improved dashboard responsiveness\n\nTo update your device, please [refer to our step by step guide](https://support.ledgerwallet.com/hc/en-us/articles/360002731113).\n\nMore information about the firmware available on [our firmware 1.4.2 FAQ](https://www.ledger.fr/2018/04/17/announcing-ledger-firmware-1-4-2/)\n",
            "name": "1.4.2",
            "identifier": "1c1cd36a98aeab8b235149dfa5f3df9f9165f4d0051c9d323d0ad30a24eb7f29",
            "osu": {
                "perso": "perso_11",
                "targetId": 823132162,
                "firmware": "nanos/1.4.2/fw_1.3.1/upgrade_osu_1.4.2",
                "firmwareKey": "nanos/1.4.2/fw_1.3.1/upgrade_osu_1.4.2_key",
                "hash": "4a1a484f7b57ad41909b2c5115e4cfb69dafb173d0eedf85ea82152deb7d7637"
            },
            "final": {
                "perso": "perso_11",
                "targetId": 823132163,
                "firmware": "nanos/1.4.2/fw_1.3.1/upgrade_1.4.2",
                "firmwareKey": "nanos/1.4.2/fw_1.3.1/upgrade_1.4.2_key",
                "hash": "3bf9b3b6cbec65f0b1a9764a2cd26102c51e0aa0b490c01ebe46e0b42307bee0"
            }
        },
        {
            "bolos_version": {
                "max": "1.3.0"
            },
            "identifier": "28bc46cbab68691336c5bc921e13a8a4b3bbb69d9802b7b0088ab0c58b3cbe7a",
            "name": "1.3.1",
            "osu": {
                "perso": "perso_11",
                "targetId": 823132162,
                "firmware": "nanos/1.3.1/upgrade_osu_1.3.1",
                "firmwareKey": "nanos/1.3.1/upgrade_osu_1.3.1_key",
                "hash": "78ef4503452b5810b42e6e715d4fe8ff3765f06758c78eefe3977e1949a12503"
            },
            "final": {
                "perso": "perso_11",
                "targetId": 823132162,
                "firmware": "nanos/1.3.1/upgrade_1.3.1",
                "firmwareKey": "nanos/1.3.1/upgrade_1.3.1_key",
                "hash": "74d10f134677adb030bafce8adb70c6510e7181a9aae509159f904be01edeed2"
            }
        }
    ]
}

applications = {
    "blue_2": [
        {
            "icon": "bitcoin",
            "name": "Bitcoin",
            "version": "1.1.18",
            "bolos_version": {
                "min": "2.0"
            },
            "app": {
                "delete": "blue/2.0/bitcoin/st31_bitcoin_del",
                "perso": "perso_11",
                "hash": "26a8fb14fabce93792d43674fe7bbb4c41c7aa75ff4aacb4c9be87a1f3bf0866",
                "targetId": 822083586,
                "firmware": "blue/2.0/bitcoin/app_latest",
                "firmwareKey": "blue/2.0/bitcoin/app_latest_key",
                "deleteKey": "blue/2.0/bitcoin/st31_bitcoin_del_key"
            },
            "identifier": "cbc6411d2356338faff7387a06e03bf88d7918b318860b6a6c293656f6790347"
        },
        {
            "icon": "bitcoin_cash",
            "name": "Bitcoin Cash",
            "version": "1.1.8",
            "bolos_version": {
                "min": "2.0"
            },
            "app": {
                "delete": "blue/2.0/bitcoin_cash/app_del",
                "perso": "perso_11",
                "hash": "6954e8a37e6d22c703ed5bfd090b4726dbdacaf034a53d51bb80611f11e2218e",
                "targetId": 822083586,
                "firmware": "blue/2.0/bitcoin_cash/app_1.1.8",
                "firmwareKey": "blue/2.0/bitcoin_cash/app_1.1.8_key",
                "deleteKey": "blue/2.0/bitcoin_cash/app_del_key"
            },
            "identifier": "442f6309034df008b40e5d315a554edcce7d68882715377b5eaac14837f6e84c"
        },
        {
            "icon": "dash",
            "name": "Dash",
            "version": "1.1.3",
            "bolos_version": {
                "min": "2.0"
            },
            "app": {
                "delete": "blue/2.0/dash/st31_dash_del",
                "perso": "perso_11",
                "hash": "db5daa27dc0e1c1c1a12804bc76c7ddf6cf629b197b903fd33a30912c48b6b63",
                "targetId": 822083586,
                "firmware": "blue/2.0/dash/st31_dash_1.1.3",
                "firmwareKey": "blue/2.0/dash/st31_dash_1.1.3_key",
                "deleteKey": "blue/2.0/dash/st31_dash_del_key"
            },
            "identifier": "80bc760633b6aeb77831fabffaf80e47b38e4cc03ea18b3a4f598879eb3d6086"
        },
        {
            "icon": "zcash",
            "name": "Zcash",
            "version": "1.1.3",
            "bolos_version": {
                "min": "2.0"
            },
            "app": {
                "delete": "blue/2.0/zcash/st31_zcash_del",
                "perso": "perso_11",
                "hash": "b01de65cc1f8db466c9d872d866aa7672c30fc6cc90b5fc4cd0ff26f29ceefdb",
                "targetId": 822083586,
                "firmware": "blue/2.0/zcash/st31_zcash_1.1.3",
                "firmwareKey": "blue/2.0/zcash/st31_zcash_1.1.3_key",
                "deleteKey": "blue/2.0/zcash/st31_zcash_del_key"
            },
            "identifier": "03994b846940f9e22fb33fd5c86c9324159a11f391d9084a06a5b0148c4f6263"
        },
        {
            "icon": "ripple",
            "name": "Ripple",
            "version": "1.0.3",
            "bolos_version": {
                "min": "2.0"
            },
            "app": {
                "delete": "blue/2.0/ripple/app_del",
                "perso": "perso_11",
                "hash": "609db324fd55e570aa4e342d748694518ff6497e3e1fa9acaed1413077b0e6dd",
                "targetId": 822083586,
                "firmware": "blue/2.0/ripple/app_1.0.3",
                "firmwareKey": "blue/2.0/ripple/app_1.0.3_key",
                "deleteKey": "blue/2.0/ripple/app_del_key"
            },
            "identifier": "b3288a28885ec8f11149dc66e38cceb7d7e0255cf07ebd2f7f1cddecf6265073"
        }
    ],
    "nanos": [
        {
            "icon": "bitcoin",
            "name": "Bitcoin",
            "version": "1.1.18",
            "bolos_version": {
                "max": "1.3.1",
                "min": "1.3.1"
            },
            "app": {
                "delete": "nanos/1.3.1/bitcoin/st31_bitcoin_del",
                "perso": "perso_11",
                "hash": "00a56bce3651ad87092721ef3626866ca3413b334e9a392e2561ee9d4150f956",
                "targetId": 823132162,
                "firmware": "nanos/1.3.1/bitcoin/app_latest",
                "firmwareKey": "nanos/1.3.1/bitcoin/app_latest_key",
                "deleteKey": "nanos/1.3.1/bitcoin/st31_bitcoin_del_key"
            },
            "identifier": "856ef5ad6e38e9742f21851bbf6d6f5f2b76afbb1861f06bd12742a210244b5f"
        },
        {
            "icon": "bitcoin_cash",
            "name": "Bitcoin Cash",
            "version": "1.1.8",
            "bolos_version": {
                "max": "1.3.1",
                "min": "1.3.1"
            },
            "app": {
                "delete": "nanos/1.3.1/bitcoin_cash/app_del",
                "perso": "perso_11",
                "hash": "a7b1d4f91ff90697c2a532bfed60b85e5f4ff55bbfc92fe9d3d13994fe0a8cbf",
                "targetId": 823132162,
                "firmware": "nanos/1.3.1/bitcoin_cash/app_1.1.8",
                "firmwareKey": "nanos/1.3.1/bitcoin_cash/app_1.1.8_key",
                "deleteKey": "nanos/1.3.1/bitcoin_cash/app_del_key"
            },
            "identifier": "4b0dc2cefb3d0b72e578f03b640a3d7c46fb6369a4087dc58ba219d2bb517cb1"
        },
        {
            "icon": "dash",
            "name": "Dash",
            "version": "1.1.5",
            "bolos_version": {
                "max": "1.3.1",
                "min": "1.3.1"
            },
            "app": {
                "delete": "nanos/1.3.1/dash/st31_dash_del",
                "perso": "perso_11",
                "hash": "3d15fb18db1f258c8b20b549b7fb4bf3e6d79c84e4c973081674b039440b34cf",
                "targetId": 823132162,
                "firmware": "nanos/1.3.1/dash/st31_dash_1.1.5",
                "firmwareKey": "nanos/1.3.1/dash/st31_dash_1.1.5_key",
                "deleteKey": "nanos/1.3.1/dash/st31_dash_del_key"
            },
            "identifier": "57f9530a5464cfe8528778280aba46379eb42e1a8b6bd78f205fd19cc2b03d78"
        },
        {
            "icon": "expanse",
            "name": "Expanse",
            "version": "1.0.20",
            "bolos_version": {
                "max": "1.3.1",
                "min": "1.3.1"
            },
            "app": {
                "delete": "nanos/1.3.1/expanse/app_del",
                "perso": "perso_11",
                "hash": "5b89eedd5135a55a69396c4f9f94d280262d171fade6f368b09c6a6011741944",
                "targetId": 823132162,
                "firmware": "nanos/1.3.1/expanse/app_1.0.20",
                "firmwareKey": "nanos/1.3.1/expanse/app_1.0.20_key",
                "deleteKey": "nanos/1.3.1/expanse/app_del_key"
            },
            "identifier": "3a73a33e1346b7e903f7dba8c3fd7d2e34a8b9b2fb59f19dc6d40c3a43ea86c6"
        },
        {
            "icon": "pivx",
            "name": "PIVX",
            "version": "1.1.12",
            "bolos_version": {
                "max": "1.3.1",
                "min": "1.3.1"
            },
            "app": {
                "delete": "nanos/1.3.1/pivx/app_del",
                "perso": "perso_11",
                "hash": "b4e1e81987cab9933994f440eaff6035a62f622aa36d3c2b97f0e1a4990e7bfb",
                "targetId": 823132162,
                "firmware": "nanos/1.3.1/pivx/app_1.1.12",
                "firmwareKey": "nanos/1.3.1/pivx/app_1.1.12_key",
                "deleteKey": "nanos/1.3.1/pivx/app_del_key"
            },
            "identifier": "19dac53cafeecf075f0c8457aeb00081ba570c18f19bd02f61e7d8f4541c38f7"
        },
        {
            "icon": "stealthcoin",
            "name": "Stealthcoin",
            "version": "1.1.10",
            "bolos_version": {
                "max": "1.3.1",
                "min": "1.3.1"
            },
            "app": {
                "delete": "nanos/1.3.1/stealthcoin/app_del",
                "perso": "perso_11",
                "hash": "9fa6e9971aa884d117f5e16db80e8f897b39b0e30728389cc74acd680439ebb1",
                "targetId": 823132162,
                "firmware": "nanos/1.3.1/stealthcoin/app_latest",
                "firmwareKey": "nanos/1.3.1/stealthcoin/app_latest_key",
                "deleteKey": "nanos/1.3.1/stealthcoin/app_del_key"
            },
            "identifier": "085851e690d9a731c103b9995e71a949bcef10f7f17bd15397ee620bae542176"
        }
    ],
    "nanos-1.4": [
        {
            "icon": "bitcoin",
            "name": "Bitcoin",
            "version": "1.2.5",
            "bolos_version": {
                "max": "1.4.2",
                "min": "1.4.2"
            },
            "app": {
                "delete": "nanos/1.4.2/bitcoin/app_del",
                "perso": "perso_11",
                "hash": "0000000000000000000000000000000000000000000000000000000000000000",
                "targetId": 823132163,
                "firmware": "nanos/1.4.2/bitcoin/app_latest",
                "firmwareKey": "nanos/1.4.2/bitcoin/app_latest_key",
                "deleteKey": "nanos/1.4.2/bitcoin/app_del_key"
            },
            "identifier": "17bab300b56912b343bc6660b74c16534ca49cae07fc4b6ff2df1f3366a51bf6"
        },
        {
            "icon": "bitcoin_cash",
            "name": "Bitcoin Cash",
            "version": "1.2.5",
            "bolos_version": {
                "max": "1.4.2",
                "min": "1.4.2"
            },
            "app": {
                "delete": "nanos/1.4.2/bitcoin_cash/app_del",
                "perso": "perso_11",
                "hash": "0000000000000000000000000000000000000000000000000000000000000000",
                "targetId": 823132163,
                "firmware": "nanos/1.4.2/bitcoin_cash/app_latest",
                "firmwareKey": "nanos/1.4.2/bitcoin_cash/app_latest_key",
                "deleteKey": "nanos/1.4.2/bitcoin_cash/app_del_key"
            },
            "identifier": "bac0b0834440a5c0067bebd428600828f26f4e35023738a28dd8264303ca8f32"
        },
        {
            "icon": "stellar",
            "name": "Stellar",
            "version": "2.1.0",
            "bolos_version": {
                "max": "1.4.2",
                "min": "1.4.2"
            },
            "app": {
                "delete": "nanos/1.4.2/stellar/app_del",
                "perso": "perso_11",
                "hash": "0000000000000000000000000000000000000000000000000000000000000000",
                "targetId": 823132163,
                "firmware": "nanos/1.4.2/stellar/app_latest",
                "firmwareKey": "nanos/1.4.2/stellar/app_latest_key",
                "deleteKey": "nanos/1.4.2/stellar/app_del_key"
            },
            "identifier": "9877884548005711fcf692f5703cf18b5506effc74abfd36628413dc026e2fea"
        },
        {
            "icon": "dascoin",
            "name": "Dascoin",
            "version": "1.1.1",
            "bolos_version": {
                "max": "1.4.2-das",
                "min": "1.4.2-das"
            },
            "app": {
                "delete": "nanos/1.4.2-das/dascoin/app_del",
                "perso": "perso_11",
                "hash": "0000000000000000000000000000000000000000000000000000000000000000",
                "targetId": 823132163,
                "firmware": "nanos/1.4.2-das/dascoin/app_latest",
                "firmwareKey": "nanos/1.4.2-das/dascoin/app_latest_key",
                "deleteKey": "nanos/1.4.2-das/dascoin/app_del_key"
            },
            "identifier": "1ffbf689fb640b5d865c58899f09bb8b71a211a441be1fc0b8c22ee187ae7af1"
        },
        {
            "icon": "bitcoin",
            "name": "Bitcoin",
            "version": "1.2.4",
            "bolos_version": {
                "max": "1.4.1",
                "min": "1.4.1"
            },
            "app": {
                "delete": "nanos/1.4.1/bitcoin/app_del",
                "perso": "perso_11",
                "hash": "0000000000000000000000000000000000000000000000000000000000000000",
                "targetId": 823132163,
                "firmware": "nanos/1.4.1/bitcoin/app_latest",
                "firmwareKey": "nanos/1.4.1/bitcoin/app_latest_key",
                "deleteKey": "nanos/1.4.1/bitcoin/app_del_key"
            },
            "identifier": "9629ba48927b0597b23abfdef7ee277f8527e02f49a70ebc89213ad6cd1e5c0e"
        },
        {
            "icon": "bitcoin_cash",
            "name": "Bitcoin Cash",
            "version": "1.2.4",
            "bolos_version": {
                "max": "1.4.1",
                "min": "1.4.1"
            },
            "app": {
                "delete": "nanos/1.4.1/bitcoin_cash/app_del",
                "perso": "perso_11",
                "hash": "0000000000000000000000000000000000000000000000000000000000000000",
                "targetId": 823132163,
                "firmware": "nanos/1.4.1/bitcoin_cash/app_latest",
                "firmwareKey": "nanos/1.4.1/bitcoin_cash/app_latest_key",
                "deleteKey": "nanos/1.4.1/bitcoin_cash/app_del_key"
            },
            "identifier": "43e9f6952233605263060b31a25418fe6b417c052c82864a361140b69d16fe9c"
        },
    ]
}

if __name__ == '__main__':
    provider1 = Provider.objects.create(name="WutWut")

    #### DEVICE CREATION

    device1 = Device.objects.create(name="Ledger Nano S")
    device2 = Device.objects.create(name="Ledger Blue")
    device3 = Device.objects.create(name="Ledger Aramis")

    device_ver1 = DeviceVersion.objects.create(
        name="nanos",
        target_id=823132162,
        device=device1
    )
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

    #### FIRMWARE CREATION

    firmware = SeFirmware.objects.create(name="1.3.1")
    firmware2 = SeFirmware.objects.create(name="1.4.1")
    firmware3 = SeFirmware.objects.create(name="1.4.2")

    firmware_ver1 = SeFirmwareVersion(
        name="1.3.1",
        notes=None,
        final_perso="perso_11",
        final_target_id=823132162,
        final_firmware="nanos/1.3.1/upgrade_1.3.1",
        final_firmware_key="nanos/1.3.1/upgrade_1.3.1_key",
        final_hash="74d10f134677adb030bafce8adb70c6510e7181a9aae509159f904be01edeed2",
        osu_perso="perso_11",
        osu_target_id=823132162,
        osu_firmware="nanos/1.3.1/upgrade_osu_1.3.1",
        osu_firmware_key="nanos/1.3.1/upgrade_osu_1.3.1_key",
        osu_hash="78ef4503452b5810b42e6e715d4fe8ff3765f06758c78eefe3977e1949a12503",
        se_firmware=firmware
    )
    firmware_ver1.save()
    firmware_ver1.device_versions.add(device_ver1)

    firmware_ver2 = SeFirmwareVersion(
        name="1.4.1",
        notes=None,
        final_perso="perso_11",
        final_target_id=823132163,
        final_firmware="nanos/1.4.1/upgrade_1.4.1",
        final_firmware_key="nanos/1.4.1/upgrade_1.4.1_key",
        final_hash="74d10f134677adb030bafce8adb70c6510e7181a9aae509159f904be01edeed2",
        osu_perso="perso_11",
        osu_target_id=None,
        osu_firmware="nanos/1.4.1/upgrade_osu_1.4.1",
        osu_firmware_key="nanos/1.4.1/upgrade_osu_1.4.1_key",
        osu_hash="2e88ef1ce8e01b181a9083950196dd0b99c6240198728b54b18bfe179856f573",
        se_firmware=firmware2
    )
    firmware_ver2.save()
    firmware_ver2.device_versions.add(device_ver5)

    firmware_ver3 = SeFirmwareVersion(
        name="1.4.2",
        notes=None,
        final_perso="perso_11",
        final_target_id=823132163,
        final_firmware="nanos/1.4.2/fw_1.4.1/upgrade_1.4.2",
        final_firmware_key="nanos/1.4.2/fw_1.4.1/upgrade_1.4.2_key",
        final_hash="8309d76fee0e809f22d4a00960b795ffdc631970cdd4b9c2a547f6c7cad3ea48",
        osu_perso="perso_11",
        osu_target_id=823132163,
        osu_firmware="nanos/1.4.2/fw_1.4.1/upgrade_osu_1.4.2",
        osu_firmware_key="nanos/1.4.2/fw_1.4.1/upgrade_osu_1.4.2_key",
        osu_hash="fbc17a950ff7576fdb22442cba6b9f32011025b4c331f44b2d6e85811e96d522",
        se_firmware=firmware3
    )
    firmware_ver3.save()
    firmware_ver3.device_versions.add(device_ver5)
    firmware_ver3.previous_se_firmware_versions.add(firmware_ver2)
    firmware_ver3.providers.add(provider1)

    firmware_ver4 = SeFirmwareVersion(
        name="1.4.2",
        notes=None,
        final_perso="perso_11",
        final_target_id=823132163,
        final_firmware="nanos/1.4.2/fw_1.3.1/upgrade_1.4.2",
        final_firmware_key="nanos/1.4.2/fw_1.3.1/upgrade_1.4.2_key",
        final_hash="3bf9b3b6cbec65f0b1a9764a2cd26102c51e0aa0b490c01ebe46e0b42307bee0",
        osu_perso="perso_11",
        osu_target_id=823132162,
        osu_firmware="nanos/1.4.2/fw_1.3.1/upgrade_osu_1.4.2",
        osu_firmware_key="nanos/1.4.2/fw_1.3.1/upgrade_osu_1.4.2_ke",
        osu_hash="4a1a484f7b57ad41909b2c5115e4cfb69dafb173d0eedf85ea82152deb7d7637",
        se_firmware=firmware3
    )
    firmware_ver4.save()
    firmware_ver4.device_versions.add(device_ver1)
    firmware_ver4.previous_se_firmware_versions.add(firmware_ver1)
    firmware_ver4.providers.add(provider1)