from modeltranslation.translator import register,TranslationOptions
from .models import News, Anons, Section, Plan


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    
@register(Anons)    
class AnonsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    
@register(Plan)    
class PlanTranslationOptions(TranslationOptions):
    fields = ('desc', 'commission')
    
@register(Section)    
class SectionTranslationOptions(TranslationOptions):
    fields = ('name', )