from django.shortcuts import render, redirect
from .forms import AssetForm
# Create your views here.


def base(request):
    return render(request, 'management/base.html')


def add_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES)
        if form.is_valid():
            # h = form.save(commit=False)
            # h.sender = request.user
            # date = str(form.cleaned_data['due_date'])
            # time = str(form.cleaned_data['time'])
            # g = ''.join(date)+" " + str(time)
            # h.due_date = g
            # h.urlhash = trans_id()
            # h.save()
            # if bool(request.FILES) == True:
            #     for file in request.FILES.getlist("attachment"):
            #         Dispatch_attach.objects.create(belongs=h, attachment=file)
            # messages.info(request, "Task added successfully.")
            return redirect('base')
        else:
            args = {'form': form}
            messages.info(request, 'Sorry ,there are errors in your form, fix them to continue.')
            return render(request, 'management/add_asset.html',args)
    else:
        form = AssetForm()
        args = {'form': form}
        return render(request, 'management/add_asset.html',args)

