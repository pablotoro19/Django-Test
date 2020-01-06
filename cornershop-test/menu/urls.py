from django.urls import path

from .views import MenuViewSet

get_menu = MenuViewSet.as_view({
    'get': 'get',
})

create_menu = MenuViewSet.as_view({
    'post': 'create',
})

update_menu = MenuViewSet.as_view({
    'put': 'update',
})

urlpatterns = [
    path('', get_menu, name='get_menu'),
    path('user/<int:user_id>', create_menu, name='create_menu'),
    path('<int:id>/user/<int:user_id>', update_menu, name='update_menu'),
]
