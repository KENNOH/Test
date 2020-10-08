from django.shortcuts import render, redirect
from .forms import AssetForm
import random, string
from django.contrib import messages
from .models import Asset, Attachments
from .tables import AssetTable
from django_tables2 import RequestConfig
from django.utils import timezone
# Create your views here.


def asset_code(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def base(request):
    return render(request, 'management/base.html')


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


def view_assets(request):
    assets = AssetTable(Asset.objects.all().order_by('-date_added'))
    RequestConfig(request, paginate={"per_page": 5}).configure(assets)
    return render(request, 'management/view_asset.html',{'assets':assets})



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


def delete(request):
    pass
