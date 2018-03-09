from django.db import models


class U2FKey(models.Model):
    user = models.ForeignKey('auth.User', related_name='u2f_key', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used_at = models.DateTimeField(null=True)

    public_key = models.TextField(unique=True)
    key_handle = models.TextField()
    app_id = models.TextField()
    version = models.CharField(max_length=255, default='U2F_V2')


class U2FRegistrationRequest(models.Model):
    user = models.ForeignKey('auth.User', related_name='u2f_registration_request', on_delete=models.CASCADE)
    body = models.TextField(null=True)


class U2FAuthenticationRequest(models.Model):
    user = models.ForeignKey('auth.User', related_name='u2f_authentication_request', on_delete=models.CASCADE)
    body = models.TextField(null=True)


class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "%s" % (self.name)


class DeviceVersion(models.Model):
    name = models.CharField(max_length=255)
    target_id = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, related_name='device_version', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)


class McuVersion(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    version = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    device_version = models.ForeignKey(DeviceVersion, related_name='mcu_version', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)


class SeFirmwareVersion(models.Model):
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, null=True)
    bolos_version_min = models.CharField(max_length=255, null=True)
    bolos_version_max = models.CharField(max_length=255, null=True)
    final_perso = models.CharField(max_length=255, null=True)
    final_target_id = models.CharField(max_length=255, null=True)
    final_firmware = models.CharField(max_length=255, null=True)
    final_firmware_key = models.CharField(max_length=255, null=True)
    final_hash = models.CharField(max_length=255, null=True)
    osu_perso = models.CharField(max_length=255, null=True)
    osu_target_id = models.CharField(max_length=255, null=True)
    osu_firmware = models.CharField(max_length=255, null=True)
    osu_firmware_key = models.CharField(max_length=255, null=True)
    osu_hash = models.CharField(max_length=255, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    device_version = models.ForeignKey(DeviceVersion, related_name='se_firmware_version', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)


class Application(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "%s" % (self.name)


class ApplicationVersion(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, null=True)
    notes = models.CharField(max_length=255, null=True)
    hash = models.CharField(max_length=255, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    bolos_version_min = models.CharField(max_length=255, null=True)
    bolos_version_max = models.CharField(max_length=255, null=True)
    perso = models.CharField(max_length=255, null=True)
    target_id = models.CharField(max_length=255, null=True)
    firmware = models.CharField(max_length=255, null=True)
    firmware_key = models.CharField(max_length=255, null=True)
    delete_key = models.CharField(max_length=255, null=True)
    delete = models.CharField(max_length=255, null=True)
    app = models.ForeignKey(Application, related_name='app_version', on_delete=models.CASCADE)
    device_version = models.ForeignKey(DeviceVersion, related_name='app_version', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)


# class BootLoader(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255, null=True)
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class BootLoaderVersion(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255, null=True)
#     version = models.CharField(max_length=255)
#     date_creation = models.DateTimeField(auto_now_add=True)
#     se = models.ForeignKey(BootLoader, related_name='bl_version', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class Lib(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255, null=True)
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class LibVersion(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255, null=True)
#     version = models.CharField(max_length=255)
#     date_creation = models.DateTimeField(auto_now_add=True)
#     se = models.ForeignKey(Lib, related_name='lib_version', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "%s" % (self.name)