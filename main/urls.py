from django.urls import path
from .views import AnonsModelViewSet, NewsModelViewSet , PlanModelViewSet
from employee.views import  EmployeeCategoryAPIView, EmployeesModelViewSet
from session.views import MaslihatSolutionModelViewSet, SolutionsModelViewSet
urlpatterns = [
    
    
    path('anons/', AnonsModelViewSet.as_view({'get': 'list'})),
    path('anons/<int:pk>', AnonsModelViewSet.as_view({'get': 'retrieve'})),
    path('news/', NewsModelViewSet.as_view({'get': 'list'})),
    path('news/<int:pk>', NewsModelViewSet.as_view({'get': 'retrieve'})),
    path('plan/', PlanModelViewSet.as_view({'get': 'list'})),
    path('plan/<int:pk>', PlanModelViewSet.as_view({'get': 'retrieve'})),
    
    path('employees/', EmployeesModelViewSet.as_view({'get': 'list'})),
    path('employees/<int:pk>', EmployeesModelViewSet.as_view({'get': 'retrieve'})),
    path('employees/category/<int:pk>', EmployeeCategoryAPIView.as_view()),
    
    path('maslihat_solution/', MaslihatSolutionModelViewSet.as_view({'get': 'list'})),
    path('solution/', SolutionsModelViewSet.as_view({'get': 'list'})),

]

