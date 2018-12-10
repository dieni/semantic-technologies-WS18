from django.shortcuts import render
from rest_framework import viewsets
from .models import EnergyControlling
from .serializers import EnergyControllingSerializer

# Create your views here.
class EnergyControllingView(viewsets.ModelViewSet):
    queryset = EnergyControlling.objects.all()
    serializer_class = EnergyControllingSerializer