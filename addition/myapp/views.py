from django.shortcuts import render

#Create your views here.
from rest_framework import viewsets
from .models import InputNum
from .serializers import InputNumSerializer

class InputNumViewSet(viewsets.ModelViewSet):
    queryset = InputNum.objects.all()
    serializer_class = InputNumSerializer


#