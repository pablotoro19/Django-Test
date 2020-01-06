from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    username = models.CharField(
        max_length=128, unique=True, null=False, blank=False)
    email = models.CharField(max_length=128)
    country_code = models.CharField(max_length=3, null=False, blank=False)
