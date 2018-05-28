from django.shortcuts import render, redirect
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

def consultation_detail(request,year,month,day,consultation):
    return render(request,'consultation/detail.html')

def index(request):
    if request.method=='POST':
        form=ConsultationForm(request.POST)
        if form.is_valid():
            consultation=Consultation()
            consultation.owner=request.user
            consultation.motif=form.cleaned_data.get('motif')
            consultation.voyage=form.cleaned_data.get('voyage')
            consultation.enfant=form.cleaned_data.get('nombre_enfant')
            consultation.situation=form.cleaned_data.get('situation')
            consultation.ville=form.cleaned_data.get('ville')
            consultation.save()
            return redirect('consultations')
    else:
        context={
        'form':ConsultationForm(),
        'consultation':Consultation.objects.filter(owner=request.user)
        }
        return render(request,'consultation/index.html',context)
