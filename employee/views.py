import imp
from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployeesSerializers
from .models import Employees, Nation

class EmployeesListAPIView(generics.ListAPIView):
    
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializers
    
class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializers
    

# class NationListAPIView(generics.ListAPIView):
    
#     queryset = Nation.objects.all()
#     serializer_class = NationSerializer
    