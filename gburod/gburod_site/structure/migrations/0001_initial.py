# Generated by Django 2.2.16 on 2023-06-06 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок лицензии')),
                ('type', models.CharField(max_length=250, verbose_name='Тип лицензии')),
                ('licenses_num', models.CharField(max_length=250, verbose_name='Номер лицензии')),
                ('file', models.FileField(help_text='Загрузите файл лицензии в формате PDF', upload_to='licenses/', verbose_name='Файл лицензии')),
            ],
            options={
                'verbose_name': 'Лицензия',
                'verbose_name_plural': 'Лицензии',
            },
        ),
    ]
