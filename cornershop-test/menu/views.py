import datetime

from django.conf import settings

from menu.models import Menu, MenuOptions
from commons.helpers import get_now_cl
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import MenuOptionsSerializer, MenuSerializer


class MenuViewSet(ViewSet):

    def create(self, request, user_id):
        #Nora is system admin
        if user_id != settings.ADMIN_ID:
            raise ValidationError(
                {'invalid user': 'the user not permitted to create a menu'})

        menu_data = request.data
        menu_serializer = MenuSerializer(data=menu_data)

        if menu_serializer.is_valid():
            menu = menu_serializer.save()
            return Response(
                {'menu_uuid': menu.uuid,
                 'menu_date': menu.menu_date},
                 status=status.HTTP_201_CREATED)
        return Response(
            menu_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, request):
        today = get_now_cl().strftime("%Y-%m-%d")
        menu_date = request.query_params.get('menu_date', today)

        try:
            menu = Menu.objects.get(menu_date=menu_date)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        menu_options = MenuOptions.objects.filter(
            menu=menu.id).all().order_by('option')
        menu_opt_serializer = MenuOptionsSerializer(menu_options, many=True)
        return Response(
            {'id': menu.id,
             'uuid': menu.uuid,
             'menu_date': menu.menu_date,
             'menu': menu_opt_serializer.data
             })

    def update(self, request, id, user_id):
        #Nora is system admin
        if user_id != settings.ADMIN_ID:
            raise ValidationError(
                {'invalid user': 'the user not permitted to edit a menu'})

        try:
            Menu.objects.get(id=id)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        menu_data = JSONParser().parse(request)

        try:
            menu_options = MenuOptions.objects.filter(
                menu=id,option=menu_data['option']).first()
        except MenuOptions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        menu_serializer = MenuOptionsSerializer(
            menu_options, data=menu_data, partial=True)

        if menu_serializer.is_valid():
            menu_serializer.save()
            return Response(menu_serializer.data)
        return Response(menu_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
