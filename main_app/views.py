from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# from . models import Product
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):

    template_name = "about.html"
