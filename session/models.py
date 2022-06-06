from turtle import title
from django.db import models
from ckeditor.fields import RichTextField

class Solutions(models.Model):
    title = models.CharField('Описание', max_length=255)
    content = RichTextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ПЕРЕЧЕНЬ ПРИНЯТЫХ РЕШЕНИЙ'
        verbose_name_plural = 'ПЕРЕЧЕНЬ ПРИНЯТЫХ РЕШЕНИЙ'
        
class MaslihatSolution(models.Model):
    title = models.CharField('Описание', max_length=255)
    file = models.FileField('Файл', upload_to='solutions/')
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Решения маслихата'
        verbose_name_plural = 'Решения маслихата'