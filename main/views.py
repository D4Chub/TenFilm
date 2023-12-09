from django.shortcuts import render
from .models import Movies


def movies_home(request):
    movies = Movies.objects.all()
    return render(request, 'main/index.html', {'movies': movies})