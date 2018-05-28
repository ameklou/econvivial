from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . forms import SignUpForm, SigninForm, ConsultationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from . models import Profile
from django.db.models import Q

# Create your views here.

def index(request):
    if request.method =='POST':
        form = SigninForm(request.POST)
        if form.is_valid:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None :
            if user.is_active:
                login(request, user)
                return render(request,"main/index.html")
            else:
                return HttpResponse('veillez activer votre compte')
        else:
            return HttpResponse("Vous n'avez pas de compte veillez vous inscrire")
    else:
        if request.user.is_authenticated():
            return redirect('dashboard')
        else:
            form= SigninForm()
            return render(request, 'account/index.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('form ok')
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.sexe = form.cleaned_data.get('sexe')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.region = form.cleaned_data.get('region')
            #user.profile.name = form.cleaned_data.get('name')
            user.profile.profession = form.cleaned_data.get('profession')
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('account/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email], from_email="dev@ecentreconvivial.org"
            )
            email.send()
            return render(request,'account/success_signup.html')
        else:
            print("error")
            return redirect('index')
    else:
        form = SignUpForm()
        #EmailMessage("openess bro", " from your big bri", to=["geekrum@gmail.com"], from_email="server@amame.org").send()
    return render(request, 'account/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request,'account/comfirmation.html')
    else:
        return HttpResponse('Activation link is invalid!')


def dashboard(request):
    return render(request, 'account/dashboard.html')
