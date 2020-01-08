import datetime

from django.conf import settings

from menu.models import Menu, MenuOptions
from commons.helpers import get_now_cl
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import render
from .serializers import MenuOptionsSerializer, MenuSerializer


class MenuViewSet(ViewSet):

    def index(request):
        return render(request, 'menu/index.html')

    #MENU

    def create_menu(self, request, user_id):
        #Nora is system admin
        if user_id != settings.ADMIN_ID:
            raise ValidationError(
                {'invalid user': 'the user not permitted to create a menu'})

        menu_data = request.data
        menu_serializer = MenuSerializer(data=menu_data)

        if menu_serializer.is_valid():
            menu = menu_serializer.save()
            return Response(
                {'id': menu.id,
                 'uuid': menu.uuid,
                 'menu_date': menu.menu_date},
                 status=status.HTTP_201_CREATED)
        return Response(
            menu_serializer.errors,
            status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get_menu(self, request, uuid):
        try:
            menu = Menu.objects.get(uuid=uuid)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        menu_options = MenuOptions.objects.filter(
            menu=menu.id).all().order_by('option')
        menu_opt_serializer = MenuOptionsSerializer(menu_options, many=True)

        return Response(
            {'id': menu.id,
             'uuid': menu.uuid,
             'menu_date': menu.menu_date,
             'options': menu_opt_serializer.data
             })



    #OPTIONS

    def create_option(self, request, user_id):
        #Nora is system admin
        if user_id != settings.ADMIN_ID:
            raise ValidationError(
                {'invalid user': 'the user not permitted to create a menu'})

        option_data = request.data

        try:
            Menu.objects.get(id=option_data['menu'])
        except Menu.DoesNotExist:
            return Response({'Menu does not exist'},
                             status=status.HTTP_404_NOT_FOUND)

        if MenuOptions.objects.filter(option=option_data['option']).count() > 0:
            return Response(
                {'Option already been created'},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        option_serializer = MenuOptionsSerializer(data=option_data)

        if option_serializer.is_valid():
            option = option_serializer.save()
            return Response(option_serializer.data,
                 status=status.HTTP_201_CREATED)
        return Response(
            option_serializer.errors,
            status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def update_option(self, request, user_id):
        #Nora is system admin
        if user_id != settings.ADMIN_ID:
            raise ValidationError(
                {'invalid user': 'the user not permitted to edit a menu'})

        option_data = request.data

        try:
            Menu.objects.get(id=option_data['menu'])
        except Menu.DoesNotExist:
            return Response(
                {'Menu does not exist'}, status=status.HTTP_404_NOT_FOUND)

        try:
            menu_options = MenuOptions.objects.get(
                menu=option_data['menu'], option=option_data['option'])
        except MenuOptions.DoesNotExist:
            return Response(
                {'Option does not exist'}, status=status.HTTP_404_NOT_FOUND)

        menu_serializer = MenuOptionsSerializer(
            menu_options, data=option_data, partial=True)

        if menu_serializer.is_valid():
            menu_serializer.save()
            return Response(menu_serializer.data)
        return Response(
            menu_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
