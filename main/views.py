import imp
from .serializers import AnonsSerializers, NewsSerializers, PlanSerializers
from .models import Anons, News, Plan
from rest_framework import viewsets, generics
from drf_multiple_model.views import ObjectMultipleModelAPIView
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
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers


class TextAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Anons.objects.all(), 'serializer_class': AnonsSerializers},
        {'queryset': News.objects.all(), 'serializer_class': NewsSerializers},
        {'queryset': Employees.objects.all}
        
    ]