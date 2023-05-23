from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.home, name='home'),
  path('signup/', views.singup, name='signup'),
  path('tasks/', views.tasks, name='tasks'),
  path('tasks/create/', views.create_task, name='create_task'),
  path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
  path('logout/', views.logoutLocal, name='logout'),
  path('login/', views.loginLocal, name='login'),
]
