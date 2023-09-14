from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
def home(request):
    return render(request,"home.html")

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def newpage(request):
    return render(request,"newpage.html")


def application(request):
    return render(request, "application.html")


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        ps = request.POST['password']
        cps = request.POST['password1']

        if ps == cps:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,
                                                password=ps)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "Passwords are does not match")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        ps = request.POST['password']
        user = auth.authenticate(username=username, password=ps)
        if user is not None:
            auth.login(request, user)
            return redirect('newpage')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    return render(request, "login.html")

