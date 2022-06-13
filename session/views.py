from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from .models import CategoryContent, CategoryFiles, Solutions, MaslihatSolution
from .serializers import CategoryContentSerializer, CategoryFilesSerializer, MaslihatSolutionSerializer, SolutionsSerializer

class MaslihatSolutionModelViewSet(ModelViewSet):
    queryset = MaslihatSolution.objects.all()
    serializer_class = MaslihatSolutionSerializer
    
class SolutionsModelViewSet(ModelViewSet):
    queryset = Solutions.objects.all()
    serializer_class = SolutionsSerializer

class FilesCategoryRetrieveAPIView(RetrieveAPIView):
    queryset = CategoryFiles.objects.all()
    serializer_class = CategoryFilesSerializer
    
    def get(self, request, *args, **kwargs):
        instanse = self.get_object()
        data = MaslihatSolution.objects.filter(category=instanse)
        serializer = MaslihatSolutionSerializer(data, many=True, context={'request': request})
        print(serializer.data)
        return Response(serializer.data)
        # return Response({
        #     'd': 'd'
        # })
    
class CategoryContentRetrieveAPIView(RetrieveAPIView):
    queryset = CategoryContent.objects.all()
    serializer_class = SolutionsSerializer
    
    def get(self, request, *args, **kwargs):
        instanse = self.get_object()
        data = Solutions.objects.filter(category=instanse)
        serializer = self.get_serializer(data, many=True, context={'request': request})
        return Response(serializer.data)