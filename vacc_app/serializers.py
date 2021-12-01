from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Persons, Slots, Vac_Centers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)


class vac_CenterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vac_Centers
    fields = "__all__"

class slotsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Slots
    fields = "__all__"

class personsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Persons
    fields = "__all__"