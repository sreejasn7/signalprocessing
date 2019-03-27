from rest_framework import serializers
from .models import Measurements , Detail_measurements


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements

    fields = ("name", "no")

