from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView


class Index(TemplateView):

    template_name = "index.html"


