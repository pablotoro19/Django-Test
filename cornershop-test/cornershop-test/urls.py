from django.urls import include, path

urlpatterns = [
    path('menu/', include('menu.urls')),
    path('user/', include('user.urls')),
    path('order/', include('user_menu.urls')),
]
