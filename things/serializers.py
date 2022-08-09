from rest_framework import serializers

from .models import Thing


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Thing
