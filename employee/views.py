from rest_framework import generics,viewsets
from .serializers import CategorySerializer, EmployeesSerializers, TimeTableSerializer
from .models import Category, Employees, TimeTable
from rest_framework.response import Response


class EmployeesModelViewSet(viewsets.ModelViewSet):
    
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializers

    
    
    
class EmployeeCategoryAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get(self, request, *args, **kwargs):
        instanse = self.get_object()
        data = Employees.objects.filter(category=instanse)
        serializer = EmployeesSerializers(data, many=True, context={'request': request})
        return Response(serializer.data)
    
class TimeTableListAPIView(generics.ListAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer


    