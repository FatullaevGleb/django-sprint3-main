from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone


POSTS_ON_PAGE = 5


def get_published_posts():
    return Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def show_main_page(request):
    template = 'blog/index.html'
    post_list = get_published_posts()[:POSTS_ON_PAGE]
    context = {'post_list': post_list}
    return render(request, template, context)


def show_category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug
    )
    post_list = get_published_posts().filter(category=category)
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)


def show_post(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(get_published_posts(), pk=id)
    context = {'post': post}
    return render(request, template, context)
