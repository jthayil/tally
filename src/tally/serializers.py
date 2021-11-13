from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Drs


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class DrsModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drs
        exclude = ["inserted_On", "updated_On"]
