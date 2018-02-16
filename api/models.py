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


# class Device(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     date_creation = models.DateTimeField()
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class DeviceVersion(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     version = models.CharField()
#     date_creation = models.DateTimeField()
#     device = models.ForeignKey(Device, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class Mcu(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     date_creation = models.DateTimeField()
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class McuVersion(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     version = models.CharField()
#     date_creation = models.DateTimeField()
#     mcu = models.ForeignKey(Mcu, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class SecureElement(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     date_creation = models.DateTimeField()
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class SecureElementVersion(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     version = models.CharField()
#     date_creation = models.DateTimeField()
#     se = models.ForeignKey(SecureElement, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class BootLoader(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     date_creation = models.DateTimeField()
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class BootLoaderVersion(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     version = models.CharField()
#     date_creation = models.DateTimeField()
#     se = models.ForeignKey(BootLoader, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class Lib(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     date_creation = models.DateTimeField()
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class LibVersion(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     version = models.CharField()
#     date_creation = models.DateTimeField()
#     se = models.ForeignKey(Lib, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class Application(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     date_creation = models.DateTimeField()
#
#     def __str__(self):
#         return "%s" % (self.name)
#
#
# class ApplicationVersion(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     version = models.CharField()
#     date_creation = models.DateTimeField()
#     se = models.ForeignKey(Application, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "%s" % (self.name)