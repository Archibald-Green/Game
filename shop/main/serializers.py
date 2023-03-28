from rest_framework import serializers
from main.models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueTogetherValidator

from main import models

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data ['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            
            
        )
        return user
    
class TokenSerializer (serializers.ModelSerializer):
    class Meta:
        model = Token
        fileds = ('key', 'user')
        
