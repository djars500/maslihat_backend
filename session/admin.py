from django.contrib import admin
from .models import MaslihatSolution, Solutions
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class SolutionForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Solutions
        exclude = ('title_ru','content_ru',)         
        
class SolutionAdmin(admin.ModelAdmin):
    form = SolutionForm
    
class MaslihatSolutionForm(forms.ModelForm):
    class Meta:
        model = MaslihatSolution
        exclude = ('title_ru',)         
        
class MaslihatSolutionAdmin(admin.ModelAdmin):
    form = MaslihatSolutionForm



admin.site.register(Solutions, SolutionAdmin)
admin.site.register(MaslihatSolution, MaslihatSolutionAdmin)