from django.urls import path
from .views import ListPostPrescription

urlpatterns = [
    path('', ListPostPrescription.as_view()),
]