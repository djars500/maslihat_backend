from distutils.command.upload import upload
from pyexpat import model
from tkinter import CASCADE
from turtle import position
from unicodedata import name
from django.db import models
from ckeditor.fields import RichTextField

class News(models.Model):
    title = models.CharField('Название', max_length=255)
    content = RichTextField()
    date = models.DateField('Дата', auto_now_add=False, null=True, blank=True)
    image = models.ImageField('Фото', upload_to='news/')
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        
    def __str__(self):
        return self.title
    
class Anons(models.Model):
    title = models.CharField('Название', max_length=255,null=True, blank=True)
    content = RichTextField()
    date = models.DateField('Дата', auto_now_add=False, null=True, blank=True)
    image = models.ImageField('Фото', upload_to='anons/')
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Анонсы'
        verbose_name_plural = 'Анонсы'
        
    def __str__(self):
        return self.title
    
class Section(models.Model):
    name = models.CharField('Какой квартал', max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Квартал'
        verbose_name_plural = 'Кварталы'
    
class Plan(models.Model):
    desc = models.TextField('Описание')
    commission = models.TextField('Коммисия')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='plan_section')
    
    def __str__(self):
        return self.desc
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'План'
        verbose_name_plural = 'План'
    
    
