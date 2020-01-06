from factory import Faker, SubFactory, LazyAttribute
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger
import random
import pytz

from .models import Menu, MenuOptions


class MenuFactory(DjangoModelFactory):
    class Meta:
        model = Menu

    menu_date = Faker('date_time_this_year', before_now=False, after_now=True, tzinfo=pytz.utc)


class MenuOptionsFactory(DjangoModelFactory):
    class Meta:
        model = MenuOptions

    description = Faker('text')
    option = LazyAttribute(lambda o: random.randint(1, 4))
    menu = SubFactory(MenuFactory)
