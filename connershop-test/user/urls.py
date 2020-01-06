from django.urls import path
from .views import UserViewSet

user = UserViewSet.as_view({
    'post': 'create',
})

urlpatterns = [
    path('', user, name='user'),
]
