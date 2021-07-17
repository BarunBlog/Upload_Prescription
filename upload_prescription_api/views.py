from rest_framework import generics

from .models import Upload_Prescription
from .serializers import Upload_Prescription_Serializer

class ListPostPrescription(generics.ListCreateAPIView):
    queryset = Upload_Prescription.objects.all()
    serializer_class = Upload_Prescription_Serializer
