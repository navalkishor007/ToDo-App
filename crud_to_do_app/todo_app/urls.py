from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('todo/', views.to_do_task),
    path('delete/<id>', views.task_delete),
    path('update/<id>', views.task_update),
]
