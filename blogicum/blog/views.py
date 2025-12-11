from django.shortcuts import render
from django.http import Http404


def index(request):
    template = 'blog/index.html'
    context = {'posts': posts[::-1]}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'

    try:
        post = POSTS_BY_ID[id]
    except KeyError:
        raise Http404("Пост не найден")

    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)
