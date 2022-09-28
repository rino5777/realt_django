from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class Main(TemplateView):
    template_name = 'main/main.html'


