from django.contrib import admin
from .models import *
from .forms import *

class PastWorkTabularInline(admin.TabularInline):
    model = PastWork
    extra = 2
    
class TimeTableTabularInline(admin.TabularInline):
    model = TimeTable
    extra = 1

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [
        PastWorkTabularInline,
        TimeTableTabularInline
    ]
    form = EmployeeAdminForm
    
class PastWorkAdmin(admin.ModelAdmin):  
    form = PastWorkAdminForm
    
class CategoryAdmin(admin.ModelAdmin): 
    form = CategoryAdminForm
    


admin.site.register(Employees,EmployeeAdmin)
admin.site.register(Position)
admin.site.register(TimeTable)
admin.site.register(Nation)
admin.site.register(Category,CategoryAdmin)
admin.site.register(PastWork,PastWorkAdmin)