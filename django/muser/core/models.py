# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from random import randint

from django.db import models
from django.conf import settings
from django.urls import reverse


def get_random_int():
    return randint(1, 100)

class CustomUser(models.Model):
    """ Extends Auth Model """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile',
                                on_delete=models.CASCADE)
    birthday = models.DateField(default=date.today)
    bizzfuzz_number = models.PositiveSmallIntegerField(default=get_random_int)

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})
