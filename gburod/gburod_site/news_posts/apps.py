from django.apps import AppConfig


class NewsPostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_posts'
    verbose_name = 'Посты новостей'
