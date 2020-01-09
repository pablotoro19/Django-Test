from datetime import date, timedelta

import factory
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .factories import UserFactory


class FakeHttpResponse():
    def __init__(self, status_code=200):
        self.status_code = status_code

    def json(self):
        return {}


class UserTestCase(APITestCase):

    def test_get_user(self):
        user = UserFactory()
        url = reverse('get_user', kwargs={'id': user.id})
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], user.username)

    def test_get_user_empty(self):
        user = UserFactory()
        url = reverse('get_user', kwargs={'id': user.id + 1})
        response = self.client.get(f'{url}', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_user(self):
        user_dict = self.create_user_data()
        response = self.client.post(reverse('create_user'), user_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], user_dict['username'])

    def create_user_data(self):
        return {
            "name": "Pedro",
            "username": "pedroo_o",
            "email": "pedro@gmail.com",
            "country_code": "CL"
            }
