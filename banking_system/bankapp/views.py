from django.http import HttpResponse, request
from django.shortcuts import render

from django.template import loader




def demo(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

