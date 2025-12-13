from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.show_main_page, name='index'),
    path('posts/<int:id>/', views.show_post, name='post_detail'),
    path(
        'category/<slug:category_slug>/',
        views.show_category_posts,
        name='category_posts'
    ),
]
