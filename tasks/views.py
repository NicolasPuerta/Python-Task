from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import UserPass, Task

####  Home  ####
def HelloWorld(request):
    return render(request, 'home.html')

####  tasks  ####
ImportanciaL={
    '1':"Lower",
    '2':"Medium",
    '3':"High"
}

@login_required ## sirve para que cuando una pagina tenga un login requerido nos devuelva el login en ves de la pagina##
def Tasks_login(request):
    tasks = Task.objects.filter(user=request.user).order_by('-important', 'created')
    for user in tasks:
        user.important = ImportanciaL[user.important]
    ## Forma 2: url ##
    if request.GET.get('id'):
        id = int(request.GET.get('id')) ## obtener un dato por la url de forma que no se obligatorio ##
        user = tasks.get(id=id)
        return render(request, 'tasks_page.html',{'tasks': tasks, 'person' : user})
    ## Forma 1: form ## 

    # if request.method == 'POST':
    #     id = int(request.POST['value'])
    #     user = tasks.get(id=id)
    #     user.important = ImportanciaL[user.important]
    #     return render(request, 'tasks_page.html',{'tasks': tasks, 'person' : user})
    return render(request, 'tasks_page.html',{'tasks': tasks})

## ##
# def Tasks_completed(request):
#     tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-important', 'created')
#     return render(request, 'tasks_completed.html',{'tasks': tasks})

@login_required
def Create_tasks(request):
    if request.method == 'POST':
        try:
            task = Task(title= request.POST['Title'],description= request.POST['description'],important= request.POST['important'], user= request.user)
            task.save()
            return redirect('task')
        except Exception as error:
            return render(request, 'createtasks.html', {'error' : f'threre was a mistake: the mistake calls :{error}'})
    return render(request, 'createtasks.html')

@login_required
def Update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        if 'Titleischange' in request.POST:
            task.title = request.POST['Title']
        if 'descriptionischange' in request.POST:
            task.description = request.POST['description']
        if 'importantischange' in request.POST:
            task.important = request.POST['important']
        task.save()
        return redirect('task')
    return render(request, 'updatetask.html', {'task': task})

@login_required
def Completed_task(request):
    if request.method == 'POST':
        task = Task.objects.get(pk=request.POST['id'],user=request.user)
        task.datecompleted = timezone.now()
        task.save()
        return redirect('task')
    return redirect('home')

@login_required
def Delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('task')

####  Login/register  ####

def Singup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordConfirm']:
            try:
                user = UserPass(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
                user.save()
                login(request, user) 
                return redirect('task')
            except IntegrityError:
                return render(request, 'sign_up.html',{'warning' : "username alredy exists"})
        return render(request, 'sign_up.html',{'warning' : "passwords don't match"})
    else:
        return render(request, 'sign_up.html')

@login_required
def Logout(request):
    logout(request)
    return redirect('home')

def Login(request):
    if request.method == 'POST':
        try:
            person = UserPass.objects.get(Q(username=request.POST['username']) | Q(email=request.POST['username']))
            if(person.password == request.POST['password']):
                login(request, person)
                return redirect('task')
            else:
                return render(request, 'login.html',{'warning' : 'password is incorrect'})
        except:
            return render(request, 'login.html', {'warning' : 'username or email is incorrect'})
    return render(request, 'login.html')

