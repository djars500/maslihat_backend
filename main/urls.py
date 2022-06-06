from django.urls import path
from .views import AnonsRetrieveAPIView, NewsRetrieveAPIView , AnonsListAPIView, NewsListAPIView
from employee.views import EmployeesListAPIView, EmployeeRetrieveAPIView
urlpatterns = [
    path('anons/', AnonsListAPIView.as_view()),
    path('anons/<int:pk>', AnonsRetrieveAPIView.as_view()),
    path('news/', NewsListAPIView.as_view()),
    path('news/<int:pk>', NewsRetrieveAPIView.as_view()),
    
    path('employees/', EmployeesListAPIView.as_view()),
    path('employees/<int:pk>', EmployeeRetrieveAPIView.as_view()),
]

