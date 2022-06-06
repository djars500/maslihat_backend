# Generated by Django 4.0.4 on 2022-06-01 12:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaslihatSolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Описание')),
                ('file', models.FileField(upload_to='solutions/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Решения маслихата',
                'verbose_name_plural': 'Решения маслихата',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Solitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Описание')),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'ПЕРЕЧЕНЬ ПРИНЯТЫХ РЕШЕНИЙ',
                'verbose_name_plural': 'ПЕРЕЧЕНЬ ПРИНЯТЫХ РЕШЕНИЙ',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
