from django.db import models
from rest_framework import serializers
from .models import Drs

class DrsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drs
        exclude = ["inserted_On", "updated_On"]