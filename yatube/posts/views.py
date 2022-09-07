from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    # Формируем шаблон
    template = 'posts/index.html'
    post_list = Post.objects.select_related('group').order_by('-pub_date')[:10]
    context = {
        'post_list': post_list
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts
        }
    return render(request, template, context)
    