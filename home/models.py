# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Herramientas(models.Model):

    #__Herramientas_FIELDS__
    nombre = models.TextField(max_length=255, null=True, blank=True)
    codigo = models.TextField(max_length=255, null=True, blank=True)
    linea = models.TextField(max_length=255, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)

    #__Herramientas_FIELDS__END

    class Meta:
        verbose_name        = _("Herramientas")
        verbose_name_plural = _("Herramientas")



#__MODELS__END
