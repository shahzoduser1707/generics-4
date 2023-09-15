from django.shortcuts import render
from .serializers import HomeSerializers
from .models import HomeModel
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.

class GetHome(generics.ListAPIView):
    queryset = HomeModel.objects.all()
    serializer_class = HomeSerializers

class CreateHome(generics.CreateAPIView):
    queryset = HomeModel.objects.all()
    serializer_class = HomeSerializers
    
class GetCreateHome(generics.ListCreateAPIView):
    queryset = HomeModel.objects.all()
    serializer_class = HomeSerializers

class DetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeModel.objects.all()
    serializer_class = HomeSerializers