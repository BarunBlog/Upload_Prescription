from rest_framework import serializers
from .models import Upload_Prescription

class Upload_Prescription_Serializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'phone', 'name', 'delivary', 'store', 'prescription_file', 'apartment', 'House', 'Road', 'Area',)
        model = Upload_Prescription