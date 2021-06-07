from django.urls import path
from . import views

urlpatterns = [
    path('', views.OverviewApi, name='api-overview'),
    path('task-list/', views.Listtask, name='task-list'),
    path('task-update/<str:pk>/', views.Updatetask, name='task-update'),
    path('task-create/', views.Createtask, name='task-Create'),
    path('task-delete/<str:pk>/', views.Deletetask, name='task-delete'),
]