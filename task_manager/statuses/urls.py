from django.urls import path
from task_manager.statuses import views


urlpatterns = [
    path('', views.StatusesView.as_view(),
         name='statuses-index'),
    path('create/', views.StatusesCreateView.as_view(),
         name='statuses-create'),
    path('<int:pk>/update/', views.StatusUpdateView.as_view(),
         name='status-update'),
    path('<int:pk>/delete/', views.StatusDeleteView.as_view(),
         name='status-delete')
]
