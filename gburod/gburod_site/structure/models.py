from django.db import models
from django.urls import reverse


class License(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Заголовок лицензии'
    )
    type = models.CharField(
        max_length=250,
        verbose_name='Тип лицензии'
    )
    licenses_num = models.CharField(
        max_length=250,
        verbose_name='Номер лицензии'
    )
    file = models.FileField(
        upload_to='licenses/',
        max_length=100,
        verbose_name='Файл лицензии',
        help_text='Загрузите файл лицензии в формате PDF'
    )

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('structure:licenses', kwargs={'id': self.id})
