from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.home, name='home'),
  path('signup/', views.singup, name='signup'),
  path('tasks/', views.tasks, name='tasks'),
  path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
  path('tasks/create/', views.create_task, name='create_task'),
  path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
  path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'), # type: ignore
  path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'), # type: ignore
  path('logout/', views.logoutLocal, name='logout'),
  path('login/', views.loginLocal, name='login'),
]
