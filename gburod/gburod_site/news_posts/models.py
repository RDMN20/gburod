from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    """Модель новостных постов."""
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )
    content = models.TextField(
        verbose_name='Контент'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-posts:news', kwargs={})
