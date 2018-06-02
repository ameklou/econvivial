from django.shortcuts import render, get_object_or_404
from .models import Planning
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    plans=Planning.objects.all()
    return render(request, 'planning/index.html',{'plans':plans})

@login_required()
def plan_detail(request,year, month, day, plan):
    plan = get_object_or_404(Planning, slug=plan,
                                   created_at__year=year,
                                   created_at__month=month,
                                   created_at__day=day)

    return render(request,'planning/detail.html',{'plan':plan})

@login_required()
def plan_exchange(request,year, month, day, username):
    return render(request,'planning/exchange.html')
