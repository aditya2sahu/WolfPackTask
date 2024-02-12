from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

#We are Using ModelSerializer for get input that and 
# and using create function for user creation
class CustomUserSerializer(serializers.ModelSerializer):
    # adding validation in input valuw
    # and import one is UniqueValidator which help to create unique email only
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    # in this field we added validate_password validators for creating strong password
    password = serializers.CharField(required=True,validators=[validate_password])
    class Meta:
        # define which Models we want ot use 
        model=CustomUser
        # And which fields we want to show in retrun's
        fields=['email','password']
    # create fun which create user 
    def create(self, validated_data):
        user = CustomUser.objects.create_user(email=validated_data['email'],password=validated_data['password'])
        return user
    
# This serializers use to take input form user for login
class CustomUserSerializerLogin(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True,validators=[validate_password])