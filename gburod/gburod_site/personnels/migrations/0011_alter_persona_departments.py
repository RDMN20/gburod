# Generated by Django 4.2.6 on 2023-11-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnels', '0010_office_persona_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='departments',
            field=models.ManyToManyField(related_name='persona', through='personnels.PersonaDepartment', to='personnels.department', verbose_name='Отделение сотрудника'),
        ),
    ]