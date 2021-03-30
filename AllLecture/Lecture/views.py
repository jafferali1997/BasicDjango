from django.shortcuts import render
from .models import UserInfoModel
from .forms import UserSignupForm
from .loginforms import UserLoginForm,UserPortfolioForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'Lecture/index.html')

def UserInfoView(request):
    CallUser = UserInfoModel.objects.order_by('FirstName')
    Userdict = {'user': CallUser}
    return render(request,'Lecture/user.html',context=Userdict)

@login_required
def special(request):
    return HttpResponse("You are logged in nice")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def SignupForm(request):

    registered = False

    if request.method=="POST":
        user_form = UserLoginForm(data=request.POST)
        portfolio_form = UserPortfolioForm(data=request.POST)

        if user_form.is_valid() and portfolio_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            portfolio = portfolio_form.save(commit=False)
            portfolio.user = user

            if 'profile_pic' in request.FILES:
                portfolio.profile_pic= request.FILES['profile_pic']

            portfolio.save()

            registered=True
        else:
            print(user_form.errors,portfolio_form.errors)

    else:
        user_form = UserLoginForm()
        portfolio_form = UserPortfolioForm()


    return render(request,'Lecture/signup.html',context={'form': user_form,'portfolio':portfolio_form,'registered':registered})

def LoginForm(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login but failed")
            print("Username:{} Password:{}".format(username,password))
            return HttpResponse("Invalid login details")
    else:
        return render(request,'Lecture/login.html',{})

