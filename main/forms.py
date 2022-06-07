from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


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
        
class PlanAdminForm(forms.ModelForm):
    class Meta:
        model = Plan
        exclude = ('desc_ru','commission_ru',)
               
class SectionAdminForm(forms.ModelForm):
    class Meta:
        model = Section
        exclude = ('name_ru',)