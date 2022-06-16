from rest_framework import serializers
from .models import Anons, News, Plan, Section

class AnonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anons
        fields = ('id','title', 'title_kk', 'content','content_kk', 'date', 'image')
        
class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','title','title_kk', 'content','content_kk', 'date', 'image')
        
class PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')
        
class SectionSerializers(serializers.ModelSerializer):
    plan_section = PlanSerializers(many=True)
    class Meta:
        model = Section
        fields = ('name','name_kk', 'plan_section')
