from rest_framework import serializers
from .models import MaslihatSolution, Solutions

class MaslihatSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaslihatSolution
        exclude = ('title_ru', 'content_ru',)
        
class SolutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solutions
        exclude = ('title_ru', 'content_ru',)