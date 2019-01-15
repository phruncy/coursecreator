from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

def index(request):
        template = loader.get_template('lottery/index.html')
        course_name = "Noch nichts generiert."
        return render(request, 'lottery/index.html', {'course_name': course_name})

def generator(request):
        return render(request, 'lottery/generator.html')

def footer(request):
        response = "Dies ist der Footer."
        return HttpResponse(response)

def about(request):
        return render(request, 'lottery/about.html')
