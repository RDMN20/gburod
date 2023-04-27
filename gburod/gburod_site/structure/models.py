from django.db import models


class License(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Заголовок лицензии'
    )
    type = models.CharField(
        max_length=250,
        verbose_name='Тип лицензии'
    )
    file = models.FileField(
        upload_to='licenses/',
        max_length=100,
        verbose_name='Файл лицензии',
        help_text='Загрузите файл лицензии в формате PDF'
    )
