from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import get_template
# Create your views here.

from .tasks import add

def index(request):
    add.delay(4,8)
    return render(request, 'home/index.html')
