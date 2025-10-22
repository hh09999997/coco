from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# 👤 نموذج المستخدم المخصص
class User(AbstractUser):
    phone = models.CharField(
        _("رقم الجوال"),
        max_length=20,
        blank=True,
        null=True
    )
    address = models.CharField(
        _("العنوان"),
        max_length=255,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("مستخدم")
        verbose_name_plural = _("المستخدمون")

    def __str__(self):
        return self.username
