from datetime import date, datetime

from pytz import timezone

from menu.models import Menu, MenuOptions
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer


class MenuOptionsSerializer(ModelSerializer):

    class Meta:
        model = MenuOptions
        fields = ('menu', 'option', 'description')

    def validate(self, data):
        if 'menu' not in data:
            raise ValidationError({'Menu': 'Menu cannot be empty'})
        if 'option' not in data:
            raise ValidationError({'option': 'Option cannot be empty'})
        if 'description' not in data:
            raise ValidationError({'description': 'Description cannot be empty'})

        return data

    def create(self, validated_data):
        option = MenuOptions.objects.create(**validated_data)
        return option

    def update(self, instance, validated_data):
        instance.option = validated_data.get('option', instance.option)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance

class MenuSerializer(ModelSerializer):

    class Meta:
        model = Menu
        fields = ('menu_date',)

    def validate(self, data):
        if 'menu_date' not in data:
            raise ValidationError({'menu_date': 'Menu date cannot be empty'})
        if Menu.objects.filter(menu_date=data['menu_date']).count() > 0:
            raise ValidationError(
                {'menu_date': 'Menu for the date has already been created'})

        return data

    def create(self, validated_data):
        dt = datetime.combine(validated_data['menu_date'], datetime.min.time())
        menu_date = (timezone('America/Santiago').localize(dt)).strftime("%Y-%m-%d")

        menu = Menu.objects.create(
            menu_date=menu_date)

        return menu
