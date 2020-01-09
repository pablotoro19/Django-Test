from datetime import datetime

from django.conf import settings
from pytz import timezone

from commons.helpers import get_now_cl
from menu.models import Menu, MenuOptions
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from user.models import User
from user_menu.models import UserMenu

from .serializers import UserMenuSerializer


class UserMenuViewSet(ViewSet):

    def create(self, request, user_id):
        if self.validate_time():
            raise ValidationError({
                    'menu_time': 'You must place orders until 11 AM.'})

        order_data = request.data
        order_serializer = UserMenuSerializer(data=order_data)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError({'user': 'This user is not valid.'})

        try:
            if 'menu' not in order_data:
                raise ValidationError({'menu': 'Menu cannot be empty'})
            Menu.objects.get(id=order_data['menu'])
        except Menu.DoesNotExist:
            raise ValidationError({'menu': 'This menu is not valid.'})

        try:
            menu_option = MenuOptions.objects.get(
                menu_id=order_data['menu'],
                option=order_data['menu_option'])
        except MenuOptions.DoesNotExist:
            raise ValidationError({
                    'menu_option': 'This menu_option is not valid.'})

        if order_serializer.is_valid():
            order = UserMenu.objects.create(
                user=user,
                menu_option=menu_option,
                quantity=order_data['quantity'],
                customizations=order_data['customizations'])

            if 'order_date' in order_data:
                order.order_date.add(order_data['order_date'])
            return Response(
                {'message': 'Order created successfully',
                 'order': order.menu_option.description,
                 'customizations': order.customizations,
                 'order_date': order.order_date},
                 status=status.HTTP_201_CREATED)
        return Response(
            order_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, request, user_id):
        try:
            User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError({
                    'user': 'This user is not valid.'
                })

        today = get_now_cl()
        today = today.strftime("%Y-%m-%d")

        query = UserMenu.objects
        #Nora(admin) is user_id=1
        if user_id == settings.ADMIN_ID:
            orders = query.filter(order_date=today).all()
        else:
            orders = query.filter(user=user_id, order_date=today).all()

        orders_serializer = UserMenuSerializer(orders, many=True)
        return Response(orders_serializer.data)

    def validate_time(self):
        now = get_now_cl()
        if now.hour > settings.LIMIT_TIME:
            return True

        return False
