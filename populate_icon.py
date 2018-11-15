import django
import os
import re

os.environ['DJANGO_SETTINGS_MODULE'] = 'ledger_app_store.settings'
django.setup()

from api.models import *

if __name__ == '__main__':
    mypath = './icons'
    only_files = [f for f in os.listdir(
        mypath) if os.path.isfile(os.path.join(mypath, f))]

    for file in only_files:
        if re.match(r'.*\.png', file):
            print(file)
            with open('./icons/{file_name}'.format(file_name=file), 'rb') as f:
                name, _ = os.path.splitext(file)

                django_file = django.core.files.File(f)

                try:
                    icon_file = Icon.objects.get(name=name)
                except Icon.DoesNotExist:
                    icon = Icon()
                    icon.name = name
                    icon.file.save(file, django_file, save=True)

    app_versions = ApplicationVersion.objects.all()

    for version in app_versions:
        icon_name = version.icon

        try:
            icon_file = Icon.objects.get(name=icon_name)
            version.picture = icon_file
            version.save()
        except Icon.DoesNotExist:
            None
