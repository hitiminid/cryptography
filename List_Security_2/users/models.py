from django.db import models
from django.contrib.auth.models import User


class YubiKeyDevice(models.Model):

    public_key = models.TextField(unique=True)
    key_handle = models.TextField()
    app_id = models.TextField()

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

