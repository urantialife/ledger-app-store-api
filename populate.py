import requests
import sys
import django
import os
import semver

os.environ['DJANGO_SETTINGS_MODULE'] = 'ledger_app_store.settings'
django.setup()
from api.models import *


API_URL = 'https://api.ledgerwallet.com/update'


def _req(method, url, verify=False, **kwargs):
    resp = requests.request(method, url, verify=verify, **kwargs)
    if resp.status_code < 400:
        return resp.json()
    else:
        print('ERROR: ', resp.text)
        sys.exit()


def main():
    d = _req('GET', API_URL + '/devices')
    for key, value in d.items():
        try:
            device = Device.objects.get(name=value['name'])
        except Device.DoesNotExist:
            device = Device.objects.create(name=value['name'])
        DeviceVersion.objects.create(
            name=key,
            target_id=value['targetId'],
            device=device
        )

    f = _req('GET', API_URL + '/firmwares')
    for key, value in f.items():
        device_version = DeviceVersion.objects.get(name=key)
        for fi in value:
            try:
                firmware = SeFirmware.objects.get(name=fi['name'])
            except SeFirmware.DoesNotExist:
                firmware = SeFirmware.objects.create(name=fi['name'])
            SeFirmwareVersion.objects.create(
                name=fi['name'],
                notes=fi.get('notes', None),
                final_perso=fi['final']['perso'],
                final_target_id=fi['final']['targetId'],
                final_firmware=fi['final']['firmware'],
                final_firmware_key=fi['final']['firmwareKey'],
                final_hash=fi['final']['hash'],
                osu_perso=fi['osu']['perso'],
                osu_target_id=fi['osu']['targetId'],
                osu_firmware=fi['osu']['firmware'],
                osu_firmware_key=fi['osu']['firmwareKey'],
                osu_hash=fi['osu']['hash'],
                bolos_version_min=fi['bolos_version'].get(
                    'min', None),
                bolos_version_max=fi['bolos_version'].get(
                    'max', None),
                device_version=device_version,
                se_firmware=firmware
            )

    a = _req('GET', API_URL + '/applications')
    for key, value in a.items():
        device_version = DeviceVersion.objects.get(name=key)
        for app_version in value:
            try:
                app = Application.objects.get(name=app_version['name'])
            except Application.DoesNotExist:
                app = Application.objects.create(name=app_version['name'])
            ApplicationVersion.objects.create(name=app_version['version'],
                                              notes=app_version.get(
                                                  'notes', None),
                                              icon=app_version.get(
                                                  'icon', None),
                                              delete=app_version['app'].get(
                                                  'delete', None),
                                              delete_key=app_version['app'].get(
                                                  'deleteKey', None),
                                              perso=app_version['app'].get(
                                                  'perso', None),
                                              hash=app_version['app'].get(
                                                  'hash', None),
                                              firmware=app_version['app'].get(
                                                  'firmware', None),
                                              firmware_key=app_version['app'].get(
                                                  'firmwareKey', None),
                                              target_id=app_version['app'].get(
                                                  'targetId', None),
                                              bolos_version_min=app_version['bolos_version'].get(
                                                  'min', None),
                                              bolos_version_max=app_version['bolos_version'].get(
                                                  'max', None),
                                              app=app,
                                              device_version=device_version)


if __name__ == '__main__':
    main()
