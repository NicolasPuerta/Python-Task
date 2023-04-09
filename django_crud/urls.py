from django.contrib import admin
from django.urls import path
from tasks.views import HelloWorld, Singup, Tasks_login,Logout,Login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HelloWorld, name='home'),
    path('signup/', Singup, name='Singup'),
    path('tasks/', Tasks_login, name='task'),
    path('logout/', Logout, name='logout'),
    path('login/', Login, name='login'),
]
