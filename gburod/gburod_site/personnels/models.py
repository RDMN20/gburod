from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


User = get_user_model()


class CommonInfo(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='Наименование'
    )
    slug = models.SlugField(unique=True, verbose_name='код')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Biography(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст биографии'
    )

    class Meta:
        verbose_name = 'Биография'
        verbose_name_plural = 'Биографии'

    def __str__(self):
        return self.text


class Speciality(CommonInfo):
    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Seat(CommonInfo):
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class AcademicDegree(CommonInfo):
    class Meta:
        verbose_name = 'Ученая степень'
        verbose_name_plural = 'Ученые степени'


class Department(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название отделения'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='код отделения'
    )
    description = models.TextField(
        verbose_name='описание отделения',
        blank=True,
    )
    add_rate = models.BooleanField(
        verobose_name='Добавить рейтинг'
    )

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

    def __str__(self):
        return self.title


class Persona(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия',
    )
    patronymic_name = models.CharField(
        max_length=60,
        verbose_name='Отчество',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seat = models.ForeignKey(
        Seat,
        related_name='persona',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='должность',
    )
    academic = models.ForeignKey(
        AcademicDegree,
        related_name='persona',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='ученая степень',
    )
    speciality = models.ForeignKey(
        Speciality,
        related_name='persona',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Специальность',
    )
    department = models.ForeignKey(
        Department,
        related_name='persona',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Отделение',
    )

    biography = models.OneToOneField(
        Biography,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        'Фотографии',
        upload_to='persons/',
        blank=True,
    )
    avg_rating = models.DecimalField(
        default=0.00,
        max_digits=2,
        decimal_places=2,
        editable=True,
        help_text='Средний рейтинг сотрудника'
    )
    persona_code = models.IntegerField(
        blank=False,
        null=True,
        verbose_name='код сотрудника',
    )

    def update_average_rating(self):
        ratings = self.rating.all()
        if ratings:
            average_rating = round(ratings.aggregate(Avg('score'))['score__avg'])
            self.average_rating = average_rating
            self.save()
        else:
            self.average_rating = 0.00
            self.save()

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Rating(models.Model):
    persona = models.ForeignKey(
        Persona,
        related_name='rating',
        on_delete=models.CASCADE,
        verbose_name='Сотрудник',
        help_text='Поставьте рейтинг от 1 до 5',
    )
    score = models.IntegerField(
        default=0.00,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'

    def __str__(self):
        return f'{self.persona.first_name} {self.persona.last_name} Оценка: {self.score}'


class Comment(models.Model):
    persona = models.ForeignKey(
        Persona,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Сотрудник',
        help_text='Комментарий на сотрудника'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
        help_text='Автор комментария',
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст комментария',
    )
    created = models.DateTimeField(
        "Дата публикации",
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий: {self.text[:30]} на {self.persona}, автор: {self.author}, {self.created}'
