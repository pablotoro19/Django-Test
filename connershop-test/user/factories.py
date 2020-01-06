import random

import pytz

from factory import Faker, LazyAttribute, SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger

from .models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    name = Faker('name')
    username = Faker('name')
    email = Faker('email')
    country_code = 'CL'
