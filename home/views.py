from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import get_template
# Create your views here.


def index(request):
    return render(request, 'home/index.html')