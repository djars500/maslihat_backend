from modeltranslation.translator import register,TranslationOptions
from .models import MaslihatSolution, Solutions,CategoryFiles, CategoryContent


@register(Solutions)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    
@register(MaslihatSolution)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)
    
@register(CategoryContent)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name',)
    
@register(CategoryFiles)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name',)