from dataclasses import field
from rest_framework import serializers
from .models import Employees, Nation, PastWork, Position

class PositionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Position
        fields = ('name',)

class NationSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Nation
        fields = ('name',)
        
        
class EmployeesSerializers(serializers.ModelSerializer):
    nation = serializers.CharField(source='nation.name')
    position = PositionSerializer(many=True)
    languages = NationSerializer(many=True)
    class Meta:
        model = Employees
        exclude = ('birth_place_ru', 'edu_end_ru', 'edu_place_ru', 'edu_speciality_ru', 'edu_degree_ru', 'awards_ru', 'party_affiliation_ru', 'content_ru')
        