from rest_framework import serializers
from .models import Anons, News

class AnonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anons
        fields = ('id','title', 'title_kk', 'content','content_kk', 'date')
        
    

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','title','title_kk', 'content','content_kk', 'date')