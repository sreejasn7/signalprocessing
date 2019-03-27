from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Measurements
from .serializers import MeasurementSerializer


class ListMeasurementSerializers(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Measurements.objects.all()
    serializer_class = MeasurementSerializer