from rest_framework import serializers
from main.models import *
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueTogetherValidator

from main import models

# class UserSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'
        
#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(
#             username=validated_data ['username'],
#             email=validated_data['email'],
#             password=validated_data['password'],
            
            
#         )
#         return user
    
# class TokenSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Token
#         fileds = ('key', 'user')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = '__all__'
        

class BookPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPage 
        fields = '__all__'
        

class PageLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageLink 
        fields = '__all__'
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item 
        fields = '__all__'
        

class BoolProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoolProgress 
        fields = '__all__'
        

