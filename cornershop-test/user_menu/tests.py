from datetime import date, timedelta

import pytz
from commons.helpers import get_now_cl

import factory
from menu.factories import MenuFactory, MenuOptionsFactory
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from user.factories import UserFactory
import random

from .factories import OrderFactory


class FakeHttpResponse():
    def __init__(self, status_code=200):
        self.status_code = status_code

    def json(self):
        return {}


class UserMenuTestCase(APITestCase):

    # def test_create_order(self):
    #     menu_date=date.today()
    #     menu = MenuFactory(menu_date=menu_date)
    #     menu_opt = MenuOptionsFactory(menu=menu)
    #     user = UserFactory()
    #     order_dict = self.create_order_data(menu_id=menu.id, menu_option=menu_opt.option)
    #
    #     with self.settings(LIMIT_TIME=23):
    #         response = self.client.post(reverse('create_order', kwargs={
    #                     'user_id': user.id}), order_dict, format='json')
    #         print(response.data)
    #         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_ordes_today(self):
        menu_date = get_now_cl().strftime("%Y-%m-%d")
        menu = MenuFactory(menu_date=menu_date)
        menu_opt = MenuOptionsFactory(menu=menu)
        user = UserFactory()
        order = OrderFactory(menu_option=menu_opt, user=user, order_date=menu_date)
        url = reverse('get_orders', kwargs={'user_id': order.user_id})
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['menu_option'], order.menu_option_id)

    def test_get_ordes_empty_today(self):
        menu_date=date.today()
        menu = MenuFactory(menu_date=menu_date)
        menu_opt = MenuOptionsFactory(menu=menu)
        user = UserFactory()
        url = reverse('get_orders', kwargs={'user_id': user.id})
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


        #self.assertEqual(response.data['menu_date'], menu_dict['menu_date'])
    #
    # def test_create_menu_exist(self):
    #     menu_date=date.today().strftime("%Y-%m-%d")
    #     menu = MenuFactory(menu_date=menu_date)
    #     MenuOptionsFactory(menu=menu)
    #
    #     menu_dict = self.create_menu_data(menu_date)
    #     response = self.client.post(reverse('create_menu', kwargs={
    #                 'user_id': 1}), menu_dict, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
    #     self.assertEqual(
    #         response.data['menu_date'][0], 'Menu for the date has already been created')
    #
    #     def test_update_menu_option(self):
    #         menu_date=date.today().strftime("%Y-%m-%d")
    #         menu = MenuFactory(menu_date=menu_date)
    #         menu_opt = MenuOptionsFactory(menu=menu)
    #         description = 'chicken'
    #         menu_dict = {'option': menu_opt.option, 'description': description}
    #         response = self.client.put(reverse('update_menu', kwargs={
    #                     'id': menu.id, 'user_id': 1}), menu_dict, format='json')
    #         self.assertEqual(response.status_code, status.HTTP_200_OK)
    #         self.assertEqual(response.data['description'], description)
    #
    def create_order_data(self, menu_id, menu_option):
        data = {
            "menu": menu_id,
            "menu_option": menu_option,
            "quantity": random.randint(1, 4),
            "customizations": "tomates sin sal"
}

        return data
