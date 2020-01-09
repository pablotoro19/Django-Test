from django.urls import path

from .views import MenuViewSet

get_menu = MenuViewSet.as_view({
    'get': 'get_menu',
})

list_menu = MenuViewSet.as_view({
    'get': 'list_menu',
})

create_menu = MenuViewSet.as_view({
    'post': 'create_menu',
})

options = MenuViewSet.as_view({
    'post': 'create_option',
    'put': 'update_option',
})


urlpatterns = [
    path('home', MenuViewSet.index),
    path('', list_menu, name='list_menu'),
    path('<uuid:uuid>', get_menu, name='get_menu'),
    path('user/<int:user_id>', create_menu, name='create_menu'),
    path('option/user/<int:user_id>', options, name='options'),
]
