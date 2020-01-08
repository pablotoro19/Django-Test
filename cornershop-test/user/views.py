from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import User
from .serializers import UserSerializer


class UserViewSet(ViewSet):

    def index(request):
        return render(request, 'user/index.html')

    def create_user(self, request):
        user_data = request.data
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            user_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get_user(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user_serializer = UserSerializer(user)

        return Response(user_serializer.data)
