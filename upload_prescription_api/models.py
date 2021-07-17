from django.db import models
from django.core.validators import RegexValidator
from .validators import validate_file_extension

Delivary_Choices = [
    ('Regular', 'Regular'),
    ('Express', 'Express'),
]

class Upload_Prescription(models.Model):
    #phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(max_length = 16, null=False, blank=False)
    name = models.CharField(max_length=200)
    delivary = models.CharField(max_length=10, choices=Delivary_Choices)
    store = models.CharField(max_length=200)
    prescription_file = models.FileField(upload_to='prescription/', validators=[validate_file_extension])
    apartment = models.CharField(max_length=250)
    House = models.CharField(max_length=250)
    Road = models.CharField(max_length=250)
    Area = models.CharField(max_length=250)

    def __str__(self):
        return self.name
