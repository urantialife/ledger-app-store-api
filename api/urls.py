from django.urls import path
from api import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Manager API')

urlpatterns = [
    path('doc', schema_view),
    path('users', views.UserList.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),
    path('auth', views.login),
    path('finish_auth', views.finish_login),
    path('key_registration', views.RegisterKey.as_view()),
    ### APPLICATIONS ###
    path('applications', views.ApplicationView.as_view()),
    path('applications/<int:pk>', views.ApplicationDetail.as_view()),
    path('application_versions', views.ApplicationVersionView.as_view()),
    path('application_versions/<int:pk>',
         views.ApplicationVersionDetail.as_view()),
    ### FIRMWARES ###
    path('firmwares', views.SeFirmwareView.as_view()),
    path('firmwares/<int:pk>', views.SeFirmwareDetail.as_view()),
    path('firmware_final_versions', views.SeFirmwareFinalVersionView.as_view()),
    path('firmware_osu_versions', views.SeFirmwareOSUVersionView.as_view()),
    path('firmware_final_versions/<int:pk>',
         views.SeFirmwareFinalVersionDetail.as_view()),
    path('firmware_osu_versions/<int:pk>',
         views.SeFirmwareOSUVersionDetail.as_view()),
    ### ICONS ###
    path('icons', views.IconView.as_view()),
    path('icons/<int:pk>', views.IconDetail.as_view()),
    ### DEVICES ###
    path('devices', views.DeviceView.as_view()),
    path('devices/<int:pk>', views.DeviceDetail.as_view()),
    path('device_versions', views.DeviceVersionView.as_view()),
    path('device_versions/<int:pk>', views.DeviceVersionDetail.as_view()),
    ### PUBLISHERS ###
    path('publishers', views.PublisherView.as_view()),
    path('publishers/<int:pk>', views.PublisherDetail.as_view()),
    ### PROVIDERS ###
    path('providers', views.ProviderView.as_view()),
    path('providers/<int:pk>', views.ProviderDetail.as_view()),
    ### CATEGORIES ###
    path('categories', views.CategoryView.as_view()),
    path('categories/<int:pk>', views.CategoryDetail.as_view()),
    ### MCU ###
    path('mcu', views.McuView.as_view()),
    path('mcu/<int:pk>', views.McuDetail.as_view()),
    path('mcu_versions', views.McuVersionView.as_view()),
    path('mcu_versions/<int:pk>', views.McuVersionDetail.as_view()),
    path('mcu_versions_bootloader', views.mcu_version_by_bootloader_version),
    ### LIVE CALLS ###
    path('get_latest_firmware', views.get_latest),
    path('get_apps', views.get_app_to_display),
    path('get_device_version',
         views.device_by_target_id),
    path('get_firmware_version',
         views.get_firmware_version),
    path('get_osu_version',
         views.get_osu_version),
    # PUBLIC CALLS
    # path('get_supported_currencies', views.get_supported_currencies),
]
