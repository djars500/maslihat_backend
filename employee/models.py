from django.db import models
from ckeditor.fields import RichTextField

class Position(models.Model):
    name = models.CharField('Должность', max_length=255)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Должность'
        verbose_name_plural = 'Должность'
    
    def __str__(self):
        return self.name

class Nation(models.Model):
    name = models.CharField('Нация', max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Национальность'
        verbose_name_plural = 'Национальность'
    
    
class PastWork(models.Model):
    join = models.DateField(auto_created=False, verbose_name='Дата вступления')
    leave = models.DateField(auto_created=False, verbose_name='Дата ухода')
    position = models.CharField('Место работы', max_length=255, null=True,blank=True)
    employee = models.ForeignKey('Employees', on_delete=models.CASCADE, verbose_name='Сотрудник')
    
    def __str__(self):
        return self.position
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Последнее место работы'
        verbose_name_plural = 'Последнее место работы'
    
class Employees(models.Model):
    image = models.ImageField(verbose_name='Фотография', upload_to='employees/')
    fio = models.CharField('ФИО', max_length=255)
    email = models.EmailField('Почта', unique=True, blank=True, null=True)
    phone = models.CharField('Номер телефона', max_length=255, null=True,blank=True)
    position = models.ManyToManyField(Position, verbose_name='Должность', related_name='employee_position')
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE, verbose_name='Нация')
    birth_date = models.DateField(auto_created=False, verbose_name='Дата рождения')
    birth_place = models.CharField('Место рождения', max_length=255, null=True,blank=True)
    edu_end = models.CharField('Окончил в', max_length=255, null=True,blank=True)
    edu_place = models.CharField('Образование в', max_length=255, null=True,blank=True)
    edu_speciality = models.CharField('Специальность по оброзованию', max_length=255, null=True,blank=True)
    edu_degree = models.CharField('Ученое звание', max_length=255, null=True,blank=True)
    languages = models.ManyToManyField(Nation, verbose_name='Какими языками владеет', related_name='employee_languages')
    awards = models.CharField('Государственные награды, почетные звания', max_length=255, null=True,blank=True)
    party_affiliation = models.CharField('Партийная принадлежность', max_length=255, null=True,blank=True)
    content = RichTextField()
    
    def __str__(self) :
        return self.fio
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудник'
    
    
