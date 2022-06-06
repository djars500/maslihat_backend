import imp
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import News, Anons

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        exclude = ('title_ru', 'content_ru',)        

class AnonsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Anons
        exclude = ('title_ru','content_ru',)
        
        
        
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
   
        
class AnonsAdmin(admin.ModelAdmin):
    form = AnonsAdminForm
    
    
    
admin.site.register(News,NewsAdmin)
admin.site.register(Anons,AnonsAdmin)