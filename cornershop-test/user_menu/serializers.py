from menu.models import MenuOptions
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from user.models import User
from user_menu.models import UserMenu


class UserMenuSerializer(ModelSerializer):

    option = serializers.SerializerMethodField(read_only=True)
    user_id = serializers.SerializerMethodField(read_only=True)
    user_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserMenu
        fields = (
            'customizations',
            'option',
            'menu_option',
            'quantity',
            'order_date',
            'user_name',
            'user_id',
            )

    def get_option(self, user_menu):
        mo = MenuOptions.objects.filter(id=user_menu.menu_option.id).first()
        return mo.description

    def get_user_id(self, user_menu):
        return user_menu.user.id

    def get_user_name(self, user_menu):
        return user_menu.user.name

    def validate(self, data):
        if 'menu_option' not in data:
            raise ValidationError(
                {'menu_option': 'Menu option cannot be empty'})
        if 'quantity' not in data:
            raise ValidationError({'quantity': 'Quantity cannot be empty'})

        return data
