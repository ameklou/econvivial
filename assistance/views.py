from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'assistance/index.html')

def assistance_detail(request,year,month,day,assistance):
    return render(request, 'assistance/detail.html')
