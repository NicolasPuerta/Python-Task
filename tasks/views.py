from django.shortcuts import render
from django.http import HttpResponse
from .models import UserPass


def HelloWorld(request):
    return HttpResponse('Hello Worl!')

def Singup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordConfirm']:
            try:
                user = UserPass(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
                user.save()
                return HttpResponse('user created successfully')
            except:
                return render(request, 'sign_up.html',{'warning' : "username alredy exists"})
        return render(request, 'sign_up.html',{'warning' : "passwords don't match"})
    else:
        return render(request, 'sign_up.html')