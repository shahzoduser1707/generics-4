from rest_framework import serializers
from .models import HomeModel

class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomeModel
        fields = '__all__'