# Generated by Django 4.2.7 on 2023-11-17 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_posts', '0005_alter_news_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
