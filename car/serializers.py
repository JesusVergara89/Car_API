from rest_framework import serializers
from .models import Cars


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'
        read_only_fields = ('created_at',)

