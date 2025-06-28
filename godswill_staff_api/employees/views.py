from django.shortcuts import render
from rest_framework import viewsets
from .models import StaffBase
from .serializers import StaffBaseSerializer

# Create your views here.
class StaffBaseViewSet(viewsets.ModelViewSet):
    queryset = StaffBase.objects.all()
    serializer_class = StaffBaseSerializer

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = StaffBase.objects.filter(is_staff=True, is_superuser=False)
    serializer_class = StaffBaseSerializer

class InternViewSet(viewsets.ModelViewSet):
    queryset = StaffBase.objects.filter(is_staff=False, is_superuser=False)
    serializer_class = StaffBaseSerializer
