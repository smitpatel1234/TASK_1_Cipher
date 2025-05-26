from rest_framework import serializers
from .models import CyptographyTool 
class CyptographyToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = CyptographyTool 
        fields ='__all__'
