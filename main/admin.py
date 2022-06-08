from django.contrib import admin

from .models import News, Anons, Section, Plan
from .forms import *

class PlanTabularInline(admin.StackedInline):
    model = Plan
    exclude = ('desc_ru','commission_ru',)   
        
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm 
        
class AnonsAdmin(admin.ModelAdmin):
    form = AnonsAdminForm
    
class PlanAdmin(admin.ModelAdmin):
    
    form = PlanAdminForm

class SectionAdmin(admin.ModelAdmin):
    inlines = [
        PlanTabularInline
    ]
    form = SectionAdminForm
    
admin.site.register(Plan,PlanAdmin)
admin.site.register(Section,SectionAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Anons,AnonsAdmin)