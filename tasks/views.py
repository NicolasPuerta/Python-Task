from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.db.models import Q

from .models import UserPass


def HelloWorld(request):
    return render(request, 'home.html')

def Tasks_login(request):
    return render(request, 'tasks_page.html')

def Singup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordConfirm']:
            try:
                user = UserPass(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
                user.save()
                login(request, user) # crea la cockie del login
                return redirect('task')
            except IntegrityError:
                return render(request, 'sign_up.html',{'warning' : "username alredy exists"})
        return render(request, 'sign_up.html',{'warning' : "passwords don't match"})
    else:
        return render(request, 'sign_up.html')

def Logout(request):
    logout(request)
    return redirect('home')

def Login(request):
    if request.method == 'POST':
        try:
            person = UserPass.objects.get(Q(username=request.POST['username']) | Q(email=request.POST['username']))
            if(person.password == request.POST['password']):
                login(request, person) # crea la cockie del login
                return redirect('task')
            else:
                return render(request, 'login.html',{'warning' : 'password is incorrect'})
        except:
            return render(request, 'login.html', {'warning' : 'username or email is incorrect'})
    return render(request, 'login.html')

