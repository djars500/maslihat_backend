from multiprocessing import context
from rest_framework.response import Response
from .serializers import AnonsSerializers, NewsSerializers, PlanSerializers, SectionSerializers
from .models import Anons, News, Plan, Section
from rest_framework import viewsets, generics
from drf_multiple_model.views import ObjectMultipleModelAPIView, FlatMultipleModelAPIView
from employee.serializers import EmployeesSerializers
from employee.views import EmployeeCategoryAPIView
from employee.models import Employees

class AnonsModelViewSet(viewsets.ModelViewSet):
    serializer_class = AnonsSerializers
    queryset = Anons.objects.all()

class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
      
class PlanModelViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers


class TextAPIView(generics.ListAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializers
    
    def get(self, request, *args, **kwargs):
        
        anons = Anons.objects.all().order_by('id')[:5]
        anons_data = AnonsSerializers(anons, many=True,context={
            'request': request
        })
        news = News.objects.all().order_by('id')[:5]
        news_data = NewsSerializers(news, many=True, context={'request': request})
        employees = Employees.objects.all().order_by('id')[:5]
        employees_data = EmployeesSerializers(employees, many=True, context={
            'request': request
        })
        return Response({
        
           'anons': anons_data.data,
           'news': news_data.data,
           'employees': employees_data.data,
          
        },
        )
        
    