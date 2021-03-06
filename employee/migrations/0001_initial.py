# Generated by Django 4.0.4 on 2022-06-08 08:03

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Категория')),
                ('name_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Категория')),
                ('name_kk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='employees/', verbose_name='Фотография')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Почта')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефона')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('birth_place', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место рождения')),
                ('birth_place_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место рождения')),
                ('birth_place_kk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место рождения')),
                ('edu_end', models.CharField(blank=True, max_length=255, null=True, verbose_name='Окончил в')),
                ('edu_end_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Окончил в')),
                ('edu_end_kk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Окончил в')),
                ('edu_place', models.CharField(blank=True, max_length=255, null=True, verbose_name='Образование в')),
                ('edu_place_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Образование в')),
                ('edu_place_kk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Образование в')),
                ('edu_speciality', models.CharField(blank=True, max_length=255, null=True, verbose_name='Специальность по оброзованию')),
                ('edu_speciality_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Специальность по оброзованию')),
                ('edu_speciality_kk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Специальность по оброзованию')),
                ('edu_degree', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ученое звание')),
                ('edu_degree_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ученое звание')),
                ('edu_degree_kk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ученое звание')),
                ('awards', models.CharField(blank=True, max_length=255, null=True, verbose_name='Государственные награды, почетные звания')),
                ('awards_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Государственные награды, почетные звания')),
                ('awards_kk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Государственные награды, почетные звания')),
                ('party_affiliation', models.CharField(blank=True, max_length=255, null=True, verbose_name='Партийная принадлежность')),
                ('party_affiliation_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Партийная принадлежность')),
                ('party_affiliation_kk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Партийная принадлежность')),
                ('content', ckeditor.fields.RichTextField()),
                ('content_ru', ckeditor.fields.RichTextField(null=True)),
                ('content_kk', ckeditor.fields.RichTextField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_category', to='employee.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудник',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Нация')),
            ],
            options={
                'verbose_name': 'Национальность',
                'verbose_name_plural': 'Национальность',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Должность')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Должность')),
                ('name_kk', models.CharField(max_length=255, null=True, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должность',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, verbose_name='Город или район')),
                ('place', models.TextField(verbose_name='Расписание, место')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employees', verbose_name='Депутат')),
            ],
            options={
                'verbose_name': 'График приема граждан',
                'verbose_name_plural': 'График приема граждан',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PastWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join', models.DateField(verbose_name='Дата вступления')),
                ('leave', models.DateField(verbose_name='Дата ухода')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место работы')),
                ('position_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место работы')),
                ('position_kk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место работы')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employees', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Последнее место работы',
                'verbose_name_plural': 'Последнее место работы',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='employees',
            name='languages',
            field=models.ManyToManyField(related_name='employee_languages', to='employee.nation', verbose_name='Какими языками владеет'),
        ),
        migrations.AddField(
            model_name='employees',
            name='nation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.nation', verbose_name='Нация'),
        ),
        migrations.AddField(
            model_name='employees',
            name='position',
            field=models.ManyToManyField(related_name='employee_position', to='employee.position', verbose_name='Должность'),
        ),
    ]
