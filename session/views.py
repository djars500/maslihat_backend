import imp
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Solutions, MaslihatSolution
from .serializers import MaslihatSolutionSerializer, SolutionsSerializer

class MaslihatSolutionModelViewSet(ModelViewSet):
    queryset = MaslihatSolution.objects.all()
    serializer_class = MaslihatSolutionSerializer
    
class SolutionsModelViewSet(ModelViewSet):
    queryset = Solutions.objects.all()
    serializer_class = SolutionsSerializer

