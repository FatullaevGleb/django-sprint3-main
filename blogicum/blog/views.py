from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone


POSTS_ON_PAGE = 5


def post_requirements():
    return Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    template = 'blog/index.html'
    post_list = post_requirements()[:POSTS_ON_PAGE]
    context = {'post_list': post_list}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug
    )
    post_list = post_requirements().filter(category=category)
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(post_requirements(), pk=id)
    context = {'post': post}
    return render(request, template, context)
