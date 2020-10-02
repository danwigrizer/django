from django.shortcuts import render
from django.conf import settings
from django.views import View
from django.http import HttpResponse
from .models import Post

# Create your views here.

blog_name = "John Doe's Blog"


def home(request):
    context = {'post': Post.objects.all()}
    return render(request,
                  'blog/home.html',
                  context
                  )


def about(request):
    context = {'post': Post.objects.all()}
    return render(request,
           'blog/about.html',
            context
           )


# class Movie(View):
#     def get(self, request, *args, **kwargs):
#         return render(
#             request, 'blog/index.html', context={
#             'director': settings.DIRECTOR,
#             'movies': movies,
#             'magazines': magazines,
#             'mag': Magclass,
#                     }
#                       )