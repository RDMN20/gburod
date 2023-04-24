# Generated by Django 2.2.16 on 2023-04-24 11:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='код')),
            ],
            options={
                'verbose_name': 'Ученая степень',
                'verbose_name_plural': 'Ученые степени',
            },
        ),
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Текст биографии', verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Биография',
                'verbose_name_plural': 'Биографии',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название отделения')),
                ('slug', models.SlugField(unique=True, verbose_name='код отделения')),
                ('description', models.TextField(blank=True, verbose_name='описание отделения')),
                ('adding_rate', models.BooleanField(default=False, verbose_name='Добавить рейтинг')),
            ],
            options={
                'verbose_name': 'Отделение',
                'verbose_name_plural': 'Отделения',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic_name', models.CharField(max_length=60, verbose_name='Отчество')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='persons/', verbose_name='Фотографии')),
                ('avg_rating', models.DecimalField(decimal_places=100, default=0.0, help_text='Средний рейтинг сотрудника', max_digits=113)),
                ('persona_code', models.IntegerField(blank=True, null=True, verbose_name='код сотрудника')),
                ('academic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='persona', to='personnels.AcademicDegree', verbose_name='ученая степень')),
                ('biography', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personnels.Biography')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='persona', to='personnels.Department', verbose_name='Отделение')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='код')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='код')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0.0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL)),
                ('persona', models.ForeignKey(help_text='Поставьте рейтинг от 1 до 5', on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='personnels.Persona', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинг',
            },
        ),
        migrations.AddField(
            model_name='persona',
            name='seat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='persona', to='personnels.Seat', verbose_name='должность'),
        ),
        migrations.AddField(
            model_name='persona',
            name='speciality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='persona', to='personnels.Speciality', verbose_name='Специальность'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Текст комментария', verbose_name='Текст')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('author', models.ForeignKey(help_text='Автор комментария', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('persona', models.ForeignKey(help_text='Комментарий на сотрудника', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='personnels.Persona', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-created'],
            },
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('persona', 'author'), name='persona_author_unique'),
        ),
    ]
