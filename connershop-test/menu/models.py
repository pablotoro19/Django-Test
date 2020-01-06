from django.db import models
from commons.helpers import generate_uuid


class Menu(models.Model):
    menu_date = models.DateField(null=False, blank=False)
    uuid = models.UUIDField(default=generate_uuid())


class MenuOptions(models.Model):
    option = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    menu = models.ForeignKey(
        "Menu", on_delete=models.CASCADE, null=False, blank=False)
