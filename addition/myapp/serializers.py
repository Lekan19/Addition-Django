from rest_framework import serializers
from .models import InputNum

class InputNumSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputNum
        fields = ['id', 'first_num', 'second_num', 'date']
