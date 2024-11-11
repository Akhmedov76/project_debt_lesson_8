from rest_framework import serializers

from .models import *


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtModel
        fields = '__all__'