from modeltranslation.translator import register,TranslationOptions
from .models import Employees, PastWork, Position


@register(Employees)
class NewsTranslationOptions(TranslationOptions):
    fields = ('birth_place', 'edu_end', 'edu_place', 'edu_speciality', 'edu_degree', 'awards', 'party_affiliation', 'content')
    
@register(PastWork)    
class AnonsTranslationOptions(TranslationOptions):
    fields = ('position',)
    

@register(Position)    
class AnonsTranslationOptions(TranslationOptions):
    fields = ('name',)