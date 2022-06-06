from modeltranslation.translator import register,TranslationOptions
from .models import News, Anons


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    
@register(Anons)    
class AnonsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')