from rest_framework import serializers
from .models import Anons, News, Plan, Section

class AnonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anons
        fields = ('id','title', 'title_kk', 'content','content_kk', 'date')
        
class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','title','title_kk', 'content','content_kk', 'date')
        
class SectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Section
        exclude = ('name_ru',)
        
class PlanSerializers(serializers.ModelSerializer):
    section_ru = serializers.CharField(source='section.name_ru')
    section_kk = serializers.CharField(source='section.name_kk')
    class Meta:
        model = Plan
        exclude = ('desc_ru','commission_ru',)
