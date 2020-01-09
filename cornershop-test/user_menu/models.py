import datetime

from django.db import models

from menu.models import MenuOptions
from user.models import User
from commons.helpers import get_now_cl


class UserMenu(models.Model):
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, null=False, blank=False)
    menu_option = models.ForeignKey(
        "menu.MenuOptions", on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(default=1)
    customizations = models.CharField(max_length=300, blank=False, null=False)
    order_date = models.DateField(default=get_now_cl().strftime("%Y-%m-%d"))
