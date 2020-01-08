from django.urls import path
from .views import UserViewSet

create_user = UserViewSet.as_view({
    'post': 'create_user',
})

get_user = UserViewSet.as_view({
    'get': 'get_user',
})

urlpatterns = [
    path('login', UserViewSet.index),
    path('', create_user, name='create_user'),
    path('<int:id>', get_user, name='get_user'),
]
