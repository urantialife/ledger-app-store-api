from django.contrib import admin
from api.models import U2FKey, Application, ApplicationVersion, DeviceVersion
from api.models import Device, SeFirmwareOSUVersion, SeFirmwareFinalVersion, U2FRegistrationRequest
from api.models import Provider, Publisher, Mcu, McuVersion, SeFirmware, Icon
from api.models import Category
from api.models import U2FAuthenticationRequest

admin.site.register(U2FKey)
admin.site.register(U2FAuthenticationRequest)
admin.site.register(U2FRegistrationRequest)
admin.site.register(Provider)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Application)
admin.site.register(ApplicationVersion)
admin.site.register(Device)
admin.site.register(DeviceVersion)
admin.site.register(SeFirmware)
admin.site.register(SeFirmwareFinalVersion)
admin.site.register(SeFirmwareOSUVersion)
admin.site.register(Mcu)
admin.site.register(McuVersion)
admin.site.register(Icon)
