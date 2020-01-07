from factory import Faker, SubFactory, LazyAttribute
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger
import random
import pytz
from user.factories import UserFactory
from menu.factories import MenuOptionsFactory

from .models import UserMenu


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = UserMenu

    user = SubFactory(UserFactory)
    menu_option = SubFactory(MenuOptionsFactory)
    quantity = LazyAttribute(lambda o: random.randint(1, 4))
    customizations = Faker('text', max_nb_chars=300)
    order_date = Faker('date_time_this_year', before_now=False, after_now=True, tzinfo=pytz.utc)
