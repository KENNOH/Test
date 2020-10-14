from django.shortcuts import render, redirect
from .forms import AssetForm
import random, string
from django.contrib import messages
from .models import Asset, Attachments
from .tables import AssetTable
from django_tables2 import RequestConfig
from django.utils import timezone
import os
from home.tasks import delete_asset
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, AssetSerializer
# Create your views here.


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, "Hey, "+str(user.username)+ " welcome back.")
            return HttpResponseRedirect('/management/base/')
        else:
            messages.info(request, "Invalid credentials were provided.")
            return HttpResponseRedirect('/management/login/')
    else:
        return render(request, 'management/login.html')

def asset_code(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@login_required(login_url='/management/login/')
def base(request):
    return render(request, 'management/base.html')


@login_required(login_url='/management/login/')
def add_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.asset_code = asset_code()
            form.save()
            if bool(request.FILES) == True:
                for file in request.FILES.getlist("attachment"):
                    Attachments.objects.create(belongs=form, attachment=file)
            messages.info(request, "Asset added successfully.")
            return redirect('base')
        else:
            args = {'form': form}
            messages.info(request, 'Sorry ,there are errors in your form, fix them to continue.')
            return render(request, 'management/add_asset.html',args)
    else:
        form = AssetForm()
        args = {'form': form}
        return render(request, 'management/add_asset.html',args)


@login_required(login_url='/management/login/')
def view_assets(request):
    assets = AssetTable(Asset.objects.all().order_by('-date_added'))
    RequestConfig(request, paginate={"per_page": 5}).configure(assets)
    return render(request, 'management/view_asset.html',{'assets':assets})


@login_required(login_url='/management/login/')
def edit(request,pk):
    asset = Asset.objects.get(pk=pk)
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES,instance=asset)
        if form.is_valid():
            form = form.save(commit=False)
            form.asset_code = asset_code()
            form.date_added = timezone.now()
            form.save()
            if bool(request.FILES) == True:
                for file in request.FILES.getlist("attachment"):
                    Attachments.objects.create(belongs=form, attachment=file)
            messages.info(request, "Asset edited successfully.")
            return redirect('view_assets')
        else:
            args = {'form': form}
            messages.info(
                request, 'Sorry ,there are errors in your form, fix them to continue.')
            return render(request, 'management/add_asset.html', args)
    else:
        form = AssetForm(instance=asset)
        args = {'form': form}
        return render(request, 'management/add_asset.html', args)


@login_required(login_url='/management/login/')
def delete(request,pk):
    if Asset.objects.filter(pk=pk).exists():
        delete_asset.delay(pk)
        messages.info(request, 'Success, instance deleted!.')
        return redirect('view_assets')
    else:
        messages.error(request, 'This record does not exist.')
        return redirect('view_assets')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

