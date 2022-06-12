from dataclasses import field
from rest_framework import serializers
from .models import Category, Employees, Nation, PastWork, Position, TimeTable

class PositionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Position
        exclude = ('name_ru',)

class NationSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Nation
        fields = '__all__'
       
class CategorySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Category
        exclude = ('name_ru',)
        
class PastWorkSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PastWork
        exclude = ('position_ru',)
        
class TimeTableSerializer(serializers.ModelSerializer): 
    employee = serializers.CharField(source='employee.position.name')
    class Meta:
        model = TimeTable
        fields = ('id','city','place','employee')
        
        
class EmployeesSerializers(serializers.ModelSerializer):
    pastwork = serializers.SerializerMethodField()
    timetable = serializers.SerializerMethodField()
    category_kk = serializers.CharField(source='category.name_kk')
    category = serializers.CharField(source='category.name')
    nation = serializers.CharField(source='nation.name')
    position = serializers.CharField(source='position.name')
    position_kk = serializers.CharField(source='position.name_kk')
    languages = NationSerializer(many=True)
    class Meta:
        model = Employees
        exclude = ('birth_place_ru', 'edu_end_ru', 'edu_place_ru', 'edu_speciality_ru', 'edu_degree_ru', 'awards_ru', 'party_affiliation_ru', 'content_ru')
        
    def get_pastwork(self, obj):
        return [PastWorkSerializer(s).data for s in obj.pastwork_set.all()]
    
    def get_timetable(self, obj):
        return [TimeTableSerializer(s).data for s in obj.timetable_set.all()]