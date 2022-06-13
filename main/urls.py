from django.urls import path
from .views import AnonsModelViewSet, NewsModelViewSet , PlanModelViewSet, TextAPIView
from employee.views import  EmployeeCategoryAPIView, EmployeesModelViewSet, TimeTableListAPIView
from session.views import CategoryContentRetrieveAPIView, MaslihatSolutionModelViewSet, SolutionsModelViewSet, FilesCategoryRetrieveAPIView
urlpatterns = [
    path('', TextAPIView.as_view()),
    
    path('anons/', AnonsModelViewSet.as_view({'get': 'list'})),
    path('anons/<int:pk>', AnonsModelViewSet.as_view({'get': 'retrieve'})),
    path('news/', NewsModelViewSet.as_view({'get': 'list'})),
    path('news/<int:pk>', NewsModelViewSet.as_view({'get': 'retrieve'})),
    path('plan/', PlanModelViewSet.as_view({'get': 'list'})),
    path('plan/<int:pk>', PlanModelViewSet.as_view({'get': 'retrieve'})),
    
    path('employees/', EmployeesModelViewSet.as_view({'get': 'list'})),
    path('employees/<int:pk>', EmployeesModelViewSet.as_view({'get': 'retrieve'})),
    path('employees/category/<int:pk>', EmployeeCategoryAPIView.as_view()),
    path('timetable/', TimeTableListAPIView.as_view()),
    
    path('files/', MaslihatSolutionModelViewSet.as_view({'get': 'list'})),
    path('solution/', SolutionsModelViewSet.as_view({'get': 'list'})),
    path('files/category/<int:pk>', FilesCategoryRetrieveAPIView.as_view()),
    path('solution/category/<int:pk>', CategoryContentRetrieveAPIView.as_view()),

]

