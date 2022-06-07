from modeltranslation.translator import register,TranslationOptions
from .models import Category, Employees, PastWork, Position


@register(Employees)
class NewsTranslationOptions(TranslationOptions):
    fields = ('birth_place', 'edu_end', 'edu_place', 'edu_speciality', 'edu_degree', 'awards', 'party_affiliation', 'content')
    
@register(PastWork)    
class PastWorkTranslationOptions(TranslationOptions):
    fields = ('position',)
    

@register(Position)    
class PositionTranslationOptions(TranslationOptions):
    fields = ('name',)
    
@register(Category)    
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)