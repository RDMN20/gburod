from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg

User = get_user_model()


# def validate_unique_rating(value): persona, device_id = value['persona'],
# value['device_id'] if Rating.objects.filter(persona=persona,
# device_id=device_id).exists(): raise ValidationError('Рейтинг уже
# существует для данного устройства')


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
    adding_rate = models.BooleanField(
        default=False,
        verbose_name='Добавить в рейтинг',
    )

    def get_personas(self):
        return self.personadepartment_set.all().values_list(
            'persona',
            flat=True,
        )

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

    def __str__(self):
        return self.title


class Office(models.Model):
    number = models.CharField(
        max_length=10,
        verbose_name='Номер кабинета',
    )

    class Meta:
        verbose_name = 'Номер кабинет'
        verbose_name_plural = 'Нумерация кабинетов'

    def __str__(self):
        return self.number


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
    education = models.TextField(
        blank=True,
        null=True,
        verbose_name='Образование',
        help_text='Введите информацию об образовании'
    )
    qualification = models.TextField(
        blank=True,
        null=True,
        verbose_name='Квалификация',
        help_text='Введите информацию о квалификации'
    )
    experience = models.TextField(
        blank=True,
        null=True,
        verbose_name='Опыт работы',
        help_text='Введите информацию об опыте работы',
    )
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
    office = models.ForeignKey(
        Office,
        related_name='persona',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Кабинет',
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
        max_digits=113,
        decimal_places=100,
        editable=True,
        help_text='Средний рейтинг сотрудника'
    )
    persona_code = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='код сотрудника',
    )
    published = models.BooleanField(
        default=False,
        verbose_name='Опубликовать',
    )

    def update_average_rating(self):
        ratings = self.rating.all()
        if ratings:
            average_rating = round(
                ratings.aggregate(Avg('score'))['score__avg'],
                2
            )
            self.average_rating = average_rating
            self.save()
        else:
            self.average_rating = 0.00
            self.save()

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class PersonaDepartment(models.Model):
    persona = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
        related_name='persona_departments',
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'отделение сотрудника'
        verbose_name_plural = 'отделение сотрудников'


class Rating(models.Model):
    persona = models.ForeignKey(
        Persona,
        related_name='rating',
        on_delete=models.CASCADE,
        verbose_name='Сотрудник',
        help_text='Поставьте рейтинг от 1 до 5',
    )
    author = models.CharField(max_length=255, null=True, )
    score = models.IntegerField(
        default=0.00,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f'Сотруник: {self.persona.first_name} {self.persona.last_name}'
            f'Оценка: {self.score} '
            f'Автор: {self.author}'
        )


class Comment(models.Model):
    persona = models.ForeignKey(
        Persona,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Сотрудник',
        help_text='Комментарий на сотрудника'
    )
    author = models.CharField(
        max_length=80,
        null=True,
    )
    comment_email = models.EmailField()
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
