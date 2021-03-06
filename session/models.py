from django.db import models
from ckeditor.fields import RichTextField


class CategoryFiles(models.Model):
    name = models.CharField('Категория', max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Категория файлов'
        verbose_name_plural = 'Категория файлов'

class CategoryContent(models.Model):
    name = models.CharField('Категория', max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Категория контента'
        verbose_name_plural = 'Категория контента'

class Solutions(models.Model):
    category = models.ForeignKey(CategoryContent, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('Описание', max_length=255)
    content = RichTextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Контент с категориями'
        verbose_name_plural = 'Контент с категориями'
        
class MaslihatSolution(models.Model):
    category = models.ForeignKey(CategoryFiles, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('Описание', max_length=255)
    file = models.FileField('Файл', upload_to='solutions/')
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Файловый контент с категорией'
        verbose_name_plural = 'Файловый контент с категорией'