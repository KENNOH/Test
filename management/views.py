from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, 'management/base.html')


def add_asset(request):
    return render(request, 'management/add_asset.html')

