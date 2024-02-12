from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.response import Response
from rest_framework import status
import json
from .models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .serializer import CustomUserSerializer, CustomUserSerializerLogin


# it return's access and refresh token
def get_tokens_for_user(user):
    try:
        refresh = RefreshToken.for_user(user)
        return {
            "success": True,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    except:
        return {
            "success": False,
            "refresh": None,
            "access": None,
        }

# In this funcation i am authenticate the users and providing them access token and refresh token
# this decorators says its that this api accept get Request 
@api_view(["GET"])
def login(request):
    # check if request is GET
    if request.method == "GET":
        # get JSON and data and using CustomUserSerializerLogin
        ser = CustomUserSerializerLogin(data=request.data)
        # check validation if provided data valid or not
        if ser.is_valid():
            #getting email and  password from validated data
            email = ser.validated_data["email"]
            password = ser.validated_data["password"]
            #checking if user does exist or not 
            user = authenticate(request, email=email, password=password)
            # if exist
            if user:
                #this function retrun Json web token
                token = get_tokens_for_user(user)
                #if we get token without any error
                if token.get("success"):
                    #return response with 200 status,message,and token
                    message = {
                        "message": "login Successfully",
                        "refresh": token.get("refresh"),
                        "access": token.get("access"),
                    }
                    return Response(status=status.HTTP_200_OK, data=message)
                else:
                    #if we get any error then retrurn with 400 bad request
                    message = {
                        "message": "login failed",
                        "refresh": None,
                        "access": None,
                    }
                    return Response(status=status.HTTP_400_BAD_REQUEST, data=message)
            else:
                #if user does not exist 
                message = {
                    "message": "User Does not exit",
                    "refresh": None,
                    "access": None,
                }
                return Response(status=status.HTTP_404_NOT_FOUND, data=message)
        else:
            #if provided data is inValid
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "message": ser.errors,
                    "refresh": None,
                    "access": None,
                },
            )

# in this funcation we create user
# this decorators says that this api accept Post Request
@api_view(["POST"])
def sing_up(request):
    # we check if request is post or not 
    if request.method == "POST":
        # by using CustomUserSerializer we get the json Data
        ser = CustomUserSerializer(data=request.data)
        #and  chekc if its valid or not
        if ser.is_valid():
            #if its valid then we create the user using serializer 
            # and return the success response
            ser.save()
            message = {"message": ser.validated_data}
            return Response(status=status.HTTP_200_OK, data=message)
        else:
            # if the data is invalid
            return Response(status=status.HTTP_400_BAD_REQUEST, data=ser.errors)


