from django.shortcuts import render, redirect, get_object_or_404
from .models import Assistance
from .forms import AssistanceForm
# Create your views here.

def index(request):
    context={
    'assistances':Assistance.objects.filter(owner=request.user)

    }
    return render(request, 'assistance/index.html',context)

def assistance_detail(request,pk,year,month,day,assistance):
    if request.method == 'POST':
        pass
    else:
        assistance = get_object_or_404(Assistance,
                                    slug=assistance,
                                    owner=pk,
                                    #owner=request.user,

                                   created_at__year=year,
                                   created_at__month=month,
                                   created_at__day=day)

    return render(request, 'assistance/detail.html',{'assistance':assistance})

def assistance(request):
    if request.method == 'POST':
        form=AssistanceForm(request.POST)
        if form.is_valid:
            assistance=Assistance()
            assistance.owner=request.user
            assistance.message=request.POST.get('message')
            assistance.service=request.POST.get('service')
            brut=request.POST.get('service')
            brut=brut.replace(' ','-')
            assistance.slug=brut
            assistance.save()
            return redirect('assistance')
        else:
            return redirect('new_assistance')

    else:
        context={
        'form':AssistanceForm()
        }
        return render(request, 'assistance/assistance.html', context)
