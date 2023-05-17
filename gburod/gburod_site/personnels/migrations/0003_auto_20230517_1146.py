# Generated by Django 2.2.16 on 2023-05-17 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnels', '0002_persona_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='education',
            field=models.TextField(blank=True, help_text='Введите информацию об образовании', null=True, verbose_name='Образование'),
        ),
        migrations.AddField(
            model_name='persona',
            name='experience',
            field=models.TextField(blank=True, help_text='Введите информацию об опыте работы', null=True, verbose_name='Опыт работы'),
        ),
        migrations.AddField(
            model_name='persona',
            name='qualification',
            field=models.TextField(blank=True, help_text='Введите информацию о квалификации', null=True, verbose_name='Квалификация'),
        ),
    ]
