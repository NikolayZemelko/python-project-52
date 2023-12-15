from django.urls import path
from task_manager.labels import views

urlpatterns = [
    path('', views.LabelsView.as_view(),
         name='labels-index'),
    path('create/', views.LabelsCreateView.as_view(),
         name='labels-create'),
    path('<int:pk>/update/', views.LabelUpdateView.as_view(),
         name='label-update'),
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(),
         name='label-delete')
]
