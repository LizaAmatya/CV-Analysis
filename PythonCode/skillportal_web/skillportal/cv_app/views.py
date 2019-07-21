from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserLoginForm, UserSignup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.forms import ValidationError

# Create your views here.

def index(request):
    # return HttpResponse("Hello, This is test homepage-!!")
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'userLogin.html')

def userLogin(request):
    username = 'not logged in'
    if request.method == 'POST':
        loginForm = UserLoginForm(request.POST)

        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
        else:
            loginForm = UserLoginForm()

    return render(request, 'userLogin.html',{"username" : username})

#for sign up
def userSignup(request):
    if request.method == 'POST':
        print('In post')
        form = UserSignup(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            # return HttpResponse("Form Submitted")
            # login(request,user)
            return redirect('login')

        else:
            # for msg in form.error_messages:
            #     print(form.error_messages[msg])
            messages.success(request,'not success')
            form = UserSignup()

    form = UserSignup()
    return render(request, 'user_signup.html', {'form': form})

