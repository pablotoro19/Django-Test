from django.urls import path
from .views import UserMenuViewSet

create_order = UserMenuViewSet.as_view({
    'post': 'create',
})

get_orders = UserMenuViewSet.as_view({
    'get': 'get',
})

urlpatterns = [
    path('user/<int:user_id>', create_order, name='create_order'),
    path('user/<int:user_id>/list', get_orders, name='get_orders'),
]
