from modeltranslation.translator import register,TranslationOptions
from .models import MaslihatSolution, Solutions


@register(Solutions)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    
@register(MaslihatSolution)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)