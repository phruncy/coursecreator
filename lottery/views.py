from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Course
from .utils import generate

def index(request):
        template = loader.get_template('lottery/generator.html')
        course_name = generate()
        return render(request, 'lottery/generator.html', {'course_name': course_name})


def footer(request):
        response = "Dies ist der Footer."
        return HttpResponse(response)

def about(request):
        return render(request, 'lottery/about.html')

def generate_new(request):
        form = GeneratorForm()
        return(request, 'blog/generate_new', {'form': form})
