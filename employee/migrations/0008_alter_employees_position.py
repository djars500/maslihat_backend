# Generated by Django 4.0.4 on 2022-06-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_alter_employees_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='position',
            field=models.ManyToManyField(related_name='employee_position', to='employee.position', verbose_name='Должность'),
        ),
    ]
