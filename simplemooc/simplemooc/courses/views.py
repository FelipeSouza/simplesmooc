from django.shortcuts import render, get_object_or_404
from .models import Course


def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'index.html', context)

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {

        'course':course

    }
    return render(request, 'details.html', context)
