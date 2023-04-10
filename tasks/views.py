from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.db.models import Q

from .models import UserPass, Task

####  Home  ####
def HelloWorld(request):
    return render(request, 'home.html')

####  tasks  ####
def Tasks_login(request):
    return render(request, 'tasks_page.html')

def Create_tasks(request):
    if request.method == 'POST':
        try:
            task = Task(title= request.POST['Title'],description= request.POST['description'],important= request.POST['important'], user= request.user)
            task.save()
            return redirect('task')
        except Exception as error:
            return render(request, 'createtasks.html', {'error' : f'threre was a mistake: the mistake calls :{error}'})
    return render(request, 'createtasks.html')

####  Login/register  ####

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

