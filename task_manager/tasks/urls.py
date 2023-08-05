from django.urls import path
from task_manager.tasks import views


urlpatterns = [
    path('', views.TasksView.as_view(),
         name='tasks-index'),
    path('<int:pk>/', views.TaskView.as_view(),
         name='task'),
    path('create/', views.TasksCreateView.as_view(),
         name='tasks-create'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(),
         name='task-update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(),
         name='task-delete')
]
