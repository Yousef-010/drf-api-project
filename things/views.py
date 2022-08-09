from django.shortcuts import render

from rest_framework import generics

from .models import Thing
from .serializers import ThingSerializer


class ThingListView(generics.ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
