from django.contrib import admin
from django.urls import path
from tasks import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HelloWorld, name='home'),
    path('signup/', views.Singup, name='Singup'),
    path('tasks/', views.Tasks_login, name='task'),
    path('logout/', views.Logout, name='logout'),
    path('login/', views.Login, name='login'),
    path('task/create/', views.Create_tasks, name='createtasks'),
    path('task/update/<int:id>/', views.Update_task, name='taskupdate'),
    path('task/complete/', views.Completed_task, name='taskcomplete'),
    path('task/delete/<int:id>/', views.Delete_task, name='taskdelete'),
    path('task/uncompleted/<int:id>/', views.uncompleted_task, name='uncompleted'),
]
