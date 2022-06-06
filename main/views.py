from django.http import JsonResponse
from django.shortcuts import render
from .serializers import AnonsSerializers, NewsSerializers
from .models import Anons, News
from rest_framework import generics

class AnonsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Anons.objects.all()
    serializer_class = AnonsSerializers
    

class NewsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    

class AnonsListAPIView(generics.ListAPIView):
    queryset = Anons.objects.all()
    serializer_class = AnonsSerializers
    

class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers