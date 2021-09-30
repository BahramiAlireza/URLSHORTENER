from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

import datetime

from random import randint


class UrlObject(models.Model):
    original_url = models.URLField()
    shorten_url = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        date = datetime.datetime.today()
        letters = [chr(randint(65,90)) for x in range(4)]
        self.shorten_url = f'{date.day}{"".join(letters[0:2])}{date.year}{letters[3]}{date.month}{date.second}{letters[2]}'
        super().save(*args, **kwargs)

    def get_url(self):
        return f'{settings.HOST_NAME}/u/{self.shorten_url}/'