from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.template import loader


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, "form.html")


        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')


            else:
                user = User.objects.create_user(username=username, password=password )
                user.save();
                return redirect('login')
        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def messages(request):

    return render(request,"msg.html")
