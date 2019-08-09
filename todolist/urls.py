from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.status_report, name="status_report"),
    path('addform/', views.addForm, name="addForm"),
    path('addtask/', views.addTask, name="addTask"),
    path('updateform/<int:task_id>/', views.updateForm, name="updateForm"),
    path('updatetask/', views.updateTask, name="updateTask"),
    path('deletetask/<int:task_id>', views.deleteTask, name="deleteTask"),
]