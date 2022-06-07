import imp
from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PastWorkAdminForm(forms.ModelForm):
    class Meta:
        model = PastWork
        exclude = ('position_ru',)
        
class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('name_ru',)
        
class EmployeeAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Employees
        exclude = ('birth_place_ru','content_ru','edu_end_ru', 'edu_place_ru', 'edu_speciality_ru','edu_degree_ru', 'awards_ru', 'party_affiliation_ru', 'content_ru')
