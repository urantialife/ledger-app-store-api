from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.name)


class Resource(models.Model):
    """
    Abstract class with default value inherited by all types
    of Resources
    """
    # Resources might have a Hash and Signature Field
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    providers = models.ManyToManyField(Provider)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % (self.name)


class Icon(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='icons/', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.name)


class U2FKey(models.Model):
    user = models.ForeignKey(
        'auth.User',
        related_name='u2f_key',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_used_at = models.DateTimeField(null=True)
    publicKey = models.TextField(unique=True)
    keyHandle = models.TextField()
    appId = models.TextField()
    version = models.CharField(max_length=255, default='U2F_V2')


class U2FRegistrationRequest(models.Model):
    user = models.ForeignKey(
        'auth.User',
        related_name='u2f_registration_request',
        on_delete=models.CASCADE
    )
    body = models.TextField(null=True)


class U2FAuthenticationRequest(models.Model):
    user = models.ForeignKey(
        'auth.User',
        related_name='u2f_authentication_request',
        on_delete=models.CASCADE
    )
    body = models.TextField(null=True)


class Publisher(Resource):
    pass


class Device(Resource):
    pass


class DeviceVersion(Resource):
    display_name = models.CharField(max_length=255, null=True, blank=True)
    target_id = models.CharField(max_length=255, null=True, blank=True)
    device = models.ForeignKey(
        Device,
        related_name='device_versions',
        on_delete=models.CASCADE,
    )


class SeFirmware(Resource):
    pass


class SeFirmwareFinalVersion(Resource):
    version = models.IntegerField()
    display_name = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    perso = models.CharField(max_length=255, null=True, blank=True)

    firmware = models.CharField(max_length=255, null=True, blank=True)
    firmware_key = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    hash = models.CharField(max_length=255, null=True, blank=True)
    se_firmware = models.ForeignKey(
        SeFirmware,
        related_name='se_firmware_final_versions',
        on_delete=models.CASCADE,
        null=True
    )
    device_versions = models.ManyToManyField(
        DeviceVersion,
        related_name='se_firmware_final_versions',
        blank=True,
    )


class SeFirmwareOSUVersion(Resource):
    display_name = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    perso = models.CharField(max_length=255, null=True, blank=True)
    firmware = models.CharField(max_length=255, null=True, blank=True)
    firmware_key = models.CharField(max_length=255, null=True, blank=True)
    hash = models.CharField(max_length=255, null=True, blank=True)
    next_se_firmware_final_version = models.ForeignKey(
        SeFirmwareFinalVersion,
        related_name='osu_versions',
        on_delete=models.CASCADE,
        null=True
    )
    device_versions = models.ManyToManyField(
        DeviceVersion,
        related_name='osu_versions',
        blank=True,
    )
    previous_se_firmware_final_versions = models.ManyToManyField(
        SeFirmwareFinalVersion,
        related_name='next_se_firmware_osu_versions',
        blank=True
    )


class Mcu(Resource):
    pass


class McuVersion(Resource):
    from_bootloader_version = models.CharField(max_length=255)
    mcu = models.ForeignKey(
        Mcu,
        related_name='mcu_versions',
        on_delete=models.CASCADE,
    )

    device_versions = models.ManyToManyField(
        DeviceVersion,
        related_name='mcu_versions',
        blank=True,
    )

    se_firmware_final_versions = models.ManyToManyField(
        SeFirmwareFinalVersion,
        related_name='mcu_versions',
        blank=True,
    )


class Category(Resource):
    pass


class Application(Resource):
    category = models.ForeignKey(
        Category,
        related_name='applications',
        on_delete=models.SET_NULL,
        null=True,
    )

    publisher = models.ForeignKey(
        Publisher,
        related_name='applications',
        on_delete=models.CASCADE,
        null=True,
    )


class ApplicationVersion(Resource):
    version = models.IntegerField()
    display_name = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ForeignKey(
        Icon,
        related_name="application_versions",
        on_delete=models.SET_NULL,
        null=True,
    )
    notes = models.TextField(blank=True, null=True)
    hash = models.CharField(max_length=255, null=True, blank=True)
    perso = models.CharField(max_length=255, null=True, blank=True)
    firmware = models.CharField(max_length=255, null=True, blank=True)
    firmware_key = models.CharField(max_length=255, null=True, blank=True)
    delete = models.CharField(max_length=255, null=True, blank=True)
    delete_key = models.CharField(max_length=255, null=True, blank=True)
    app = models.ForeignKey(
        Application,
        related_name='application_versions',
        on_delete=models.CASCADE,
    )
    device_versions = models.ManyToManyField(
        DeviceVersion,
        related_name='application_versions',
        blank=True,
    )
    se_firmware_final_versions = models.ManyToManyField(
        SeFirmwareFinalVersion,
        related_name="application_versions",
        blank=True,
    )

