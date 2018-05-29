from django.shortcuts import render, redirect
from .models import Assistance
from .forms import AssistanceForm
# Create your views here.

def index(request):
    context={
    'assistances':Assistance.objects.filter(owner=request.user)

    }
    return render(request, 'assistance/index.html',context)

def assistance_detail(request,year,month,day,assistance):
    return render(request, 'assistance/detail.html')

def assistance(request):
    if request.method == 'POST':
        form=AssistanceForm(request.POST)
        if form.is_valid:
            assistance=Assistance()
            assistance.owner=request.user
            assistance.message=request.POST.get('message')
            assistance.service=request.POST.get('service')
            assistance.slug=request.POST.get('service')
            assistance.save()
            return redirect('assistance')
        else:
            return redirect('new_assistance')

    else:
        context={
        'form':AssistanceForm()
        }
        return render(request, 'assistance/assistance.html', context)
