from rest_framework import serializers
from .models import *

class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
    
class CsvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitcoin
        fields = '__all__'