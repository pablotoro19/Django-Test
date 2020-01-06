from menu.models import Menu, MenuOptions
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from datetime import date
from datetime import datetime
from pytz import timezone


class MenuOptionsSerializer(ModelSerializer):
    
    class Meta:
        model = MenuOptions
        fields = ('option', 'description')

    def validate(self, data):
        if 'option' not in data:
            raise ValidationError({'option': 'Option cannot be empty'})
        if 'description' not in data:
            raise ValidationError({'description': 'Description cannot be empty'})

        return data

    def update(self, instance, validated_data):
        instance.option = validated_data.get('option', instance.option)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance

class MenuSerializer(ModelSerializer):
    options = MenuOptionsSerializer(many=True)

    class Meta:
        model = Menu
        fields = ('menu_date', 'options')

    def validate(self, data):
        if 'menu_date' not in data:
            raise ValidationError({'menu_date': 'Menu date cannot be empty'})
        if Menu.objects.filter(menu_date=data['menu_date']).count() > 0:
            raise ValidationError(
                {'menu_date': 'Menu for the date has already been created'})

        return data

    def create(self, validated_data):
        dt = datetime.combine(validated_data['menu_date'], datetime.min.time())
        menu_date = timezone('America/Santiago').localize(dt)

        menu = Menu.objects.create(
            menu_date=menu_date.strftime("%Y-%m-%d"))

        for option in validated_data['options']:
            MenuOptions.objects.create(
                option=option['option'],
                description=option['description'],
                menu=menu)

        return menu
