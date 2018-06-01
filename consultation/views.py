from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . forms import  ConsultationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from . models import Consultation
from django.db.models import Q

# Create your views here.

def new_consultation(request):
    if request.method=='POST':
        form=ConsultationForm(request.POST)
        if form.is_valid():
                consultation=Consultation()
                consultation.owner=request.user
                consultation.motif=form.cleaned_data.get('motif')
                brut=form.cleaned_data.get('motif')
                brut=brut.replace(' ','-')
                consultation.slug=brut
                consultation.voyage=form.cleaned_data.get('voyage')
                consultation.enfant=form.cleaned_data.get('enfant')
                consultation.message=form.cleaned_data.get('message')
                consultation.situation=form.cleaned_data.get('situation')
                consultation.ville=form.cleaned_data.get('ville')
                consultation.save()
                return redirect('consultation')
    else:
        context={
        'form':ConsultationForm()
        }
    return render(request,'consultation/consultation.html',context)

def consultation_detail(request,pk,year,month,day,consultation):
    consultation = get_object_or_404(Consultation,
                                    slug=consultation,
                                    owner=pk,
                                    #owner=request.user,

                                   created_at__year=year,
                                   created_at__month=month,
                                   created_at__day=day)

    return render(request,'consultation/detail.html',{'consultation':consultation})

def index(request):
    if request.user.is_authenticated:
        context={
        'consultations':Consultation.objects.filter(owner=request.user)

        }
        return render(request, 'consultation/index.html',context)
    else:
        return render(request, 'consultation/index.html')
    # if request.method=='POST':
    #     form=ConsultationForm(request.POST)
    #     if form.is_valid():
    #         consultation=Consultation()
    #         consultation.owner=request.user
    #         consultation.motif=form.cleaned_data.get('motif')
    #         consultation.voyage=form.cleaned_data.get('voyage')
    #         consultation.enfant=form.cleaned_data.get('nombre_enfant')
    #         consultation.situation=form.cleaned_data.get('situation')
    #         consultation.ville=form.cleaned_data.get('ville')
    #         consultation.save()
    #         return redirect('consultation')
    # else:
    #     if request.user.is_authenticated:
    #         context={
    #         'form':ConsultationForm()
    #         #'consultation':Consultation.objects.filter(owner=request.user)
    #         }
    #         return render(request,'consultation/index.html',context)
    #     else:
    #         return rediret('dashboard')
