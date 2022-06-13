# Generated by Django 4.0.4 on 2022-06-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория файлов',
                'verbose_name_plural': 'Категория файлов',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='categorycontent',
            options={'managed': True, 'verbose_name': 'Категория контента', 'verbose_name_plural': 'Категория контента'},
        ),
    ]
