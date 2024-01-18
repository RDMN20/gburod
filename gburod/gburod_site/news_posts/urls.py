from django.urls import path
from news_posts.views import news_list, news_detail


app_name = 'news-posts'
urlpatterns = [
    path('', news_list, name='news'),
    path('news-detail/<int:news_id>/', news_detail, name='news_detail'),
]
