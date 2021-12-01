from django.shortcuts import render
from rest_framework import viewsets
from .models import Slots, Persons, Vac_Centers
from .serializers import slotsSerializer, personsSerializer, vac_CenterSerializer
#############################
## login views from sei notes
#############################
from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer, TokenSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# JWT settings
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(generics.ListCreateAPIView):
    """
    POST user/login/
    """

    # This permission class will overide the global permission class setting
    # Permission checks are always run at the very start of the view, before any other code is allowed to proceed.
    # The permission class here is set to AllowAny, which overwrites the global class to allow anyone to have access to login.
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer(data={
                # using DRF JWT utility functions to generate a token
                "token": str(refresh.access_token)
                })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
#############################
## END OF login views from sei notes
#############################

#############################
## signup views from sei notes
#############################
class RegisterUsersView(generics.ListCreateAPIView):
    """
    POST user/signup/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username or not password or not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)
#############################
## END OF signup views from sei notes
#############################

#############################
## slots views 
#############################
class SlotsSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Slots.objects.all()
    # The serializer class for serializing output
    serializer_class = slotsSerializer
    # optional permission class set permission level
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #Coule be [permissions.IsAuthenticated]

class Vac_Center_ViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Vac_Centers.objects.all()
    # The serializer class for serializing output
    serializer_class = vac_CenterSerializer
    # optional permission class set permission level
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #Coule be [permissions.IsAuthenticated]

