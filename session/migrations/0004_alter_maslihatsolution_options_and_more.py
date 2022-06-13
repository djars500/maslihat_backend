# Generated by Django 4.0.4 on 2022-06-13 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_categorycontent_name_kk_categorycontent_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maslihatsolution',
            options={'managed': True, 'verbose_name': 'Файловый контент с категорией', 'verbose_name_plural': 'Файловый контент с категорией'},
        ),
        migrations.AlterField(
            model_name='maslihatsolution',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='session.categoryfiles'),
        ),
    ]
