from rest_framework import serializers
from django.contrib.auth.models import User

from vaccine.vacc_app.models import persons, slots, vac_Centers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)


class vac_CenterSerializer(serializers.ModelSerializer):
  class Meta:
    model = vac_Centers
    fields = "__all__"

class slotsSerializer(serializers.ModelSerializer):
  class Meta:
    model = slots
    fields = "__all__"

class personsSerializer(serializers.ModelSerializer):
  class Meta:
    model = persons
    fields = "__all__"