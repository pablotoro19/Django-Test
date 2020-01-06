from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


class UserViewSet(ViewSet):

    def create(self, request):
        user_data = request.data
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            return Response(
                {'message': 'User created successfully', 'user_id': user.id},
                 status=status.HTTP_201_CREATED)
        return Response(
            user_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
