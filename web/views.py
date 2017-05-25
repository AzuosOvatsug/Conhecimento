from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    Post.objects.filter(publicado_data__lte=timezone.now()).order_by('publicado_data')
    return render(request, 'web/post_list.html', {'posts': posts})
