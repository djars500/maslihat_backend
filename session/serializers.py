from rest_framework import serializers
from .models import MaslihatSolution, Solutions, CategoryFiles, CategoryContent


class CategoryFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryFiles
        exclude = ('name_ru',)
        
class CategoryContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryContent
        exclude = ('name_ru',)

class MaslihatSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaslihatSolution
        exclude = ('title_ru',)
        
class SolutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solutions
        exclude = ('title_ru', 'content_ru',)