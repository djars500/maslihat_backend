from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class PastWorkTabularInline(admin.TabularInline):
    model = PastWork

class EmployeeAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Employees
        exclude = ('birth_place_ru','content_ru','edu_end_ru', 'edu_place_ru', 'edu_speciality_ru','edu_degree_ru', 'awards_ru', 'party_affiliation_ru', 'content_ru')

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [
        PastWorkTabularInline
    ]
    form = EmployeeAdminForm
    
class PastWorkAdminForm(forms.ModelForm):
    class Meta:
        model = PastWork
        exclude = ('position_ru',)

class PastWorkAdmin(admin.ModelAdmin):
    
    form = PastWorkAdminForm

admin.site.register(Employees,EmployeeAdmin)
admin.site.register(Position)
admin.site.register(Nation)
admin.site.register(PastWork,PastWorkAdmin)