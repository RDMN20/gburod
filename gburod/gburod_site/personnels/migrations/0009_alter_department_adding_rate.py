# Generated by Django 4.2.6 on 2023-11-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnels', '0008_remove_persona_department_personadepartment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='adding_rate',
            field=models.BooleanField(default=False, verbose_name='Добавить в рейтинг'),
        ),
    ]