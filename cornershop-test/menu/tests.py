from datetime import date, timedelta

import factory
from commons.helpers import generate_uuid, get_now_cl
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .factories import MenuFactory, MenuOptionsFactory


class FakeHttpResponse():
    def __init__(self, status_code=200):
        self.status_code = status_code

    def json(self):
        return {}


class MenuTestCase(APITestCase):

    def test_list_menu(self):
        menu_date = get_now_cl().strftime("%Y-%m-%d")
        menu_date_2 = (get_now_cl() + timedelta(days=1)).strftime("%Y-%m-%d")
        MenuFactory(menu_date=menu_date)
        MenuFactory(menu_date=menu_date_2)

        url = reverse('list_menu')
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_menu_empty(self):
        url = reverse('list_menu')
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_get_menu_today(self):
        menu_date = get_now_cl().strftime("%Y-%m-%d")
        menu = MenuFactory(menu_date=menu_date)
        MenuOptionsFactory(menu=menu)
        url = reverse('get_menu', kwargs={'uuid': menu.uuid})
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['menu_date'].strftime("%Y-%m-%d"), menu_date)

    def test_get_menu_empty_today(self):
        uuid = generate_uuid()
        menu_date = get_now_cl().strftime("%Y-%m-%d")
        MenuFactory(menu_date=menu_date)
        url = reverse('get_menu', kwargs={'uuid': uuid})
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_menu(self):
        menu_date=date.today()
        menu_dict = self.create_menu_data(menu_date.strftime("%Y-%m-%d"))
        response = self.client.post(reverse('create_menu', kwargs={
                    'user_id': 1}), menu_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['menu_date'], menu_dict['menu_date'])

    def test_create_menu_exist(self):
        menu_date=date.today().strftime("%Y-%m-%d")
        menu = MenuFactory(menu_date=menu_date)
        MenuOptionsFactory(menu=menu)
        menu_dict = self.create_menu_data(menu_date)
        response = self.client.post(reverse('create_menu', kwargs={
                    'user_id': 1}), menu_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(
            response.data['menu_date'][0], 'Menu for the date has already been created')

    def create_menu_data(self, menu_date):
        data = {
            "menu_date": menu_date
            }

        return data


class MenuOptionTestCase(APITestCase):

    def test_create_option(self):
        menu_date=date.today().strftime("%Y-%m-%d")
        menu = MenuFactory(menu_date=menu_date)
        opt_dict = {'menu': menu.id,
                    'option': 3,
                    'description': 'chicken'}
        response = self.client.post(reverse('options', kwargs={
                    'user_id': 1}), opt_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['option'], opt_dict['option'])

    def test_update_menu_option(self):
        menu_date=date.today().strftime("%Y-%m-%d")
        menu = MenuFactory(menu_date=menu_date)
        menu_opt = MenuOptionsFactory(menu=menu)
        opt_dict = {'menu': menu.id,
                    'option': menu_opt.option,
                    'description': 'chicken'}
        response = self.client.put(
            reverse('options', kwargs={'user_id': 1}), opt_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'],  opt_dict['description'])
