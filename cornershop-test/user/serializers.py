from user.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email', 'country_code')


    def validate(self, data):
        if 'username' not in data:
            raise ValidationError({'username': 'Username cannot be empty'})
        if 'country_code' not in data:
            raise ValidationError(
                {'country_code': 'Country Code cannot be empty'})
        return data

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            username=validated_data['username'],
            email=validated_data['email'],
            country_code=validated_data['country_code'])

        return user
