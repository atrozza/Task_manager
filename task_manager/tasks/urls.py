from django.urls import path, include
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDoneView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/<int:pk>/done/', TaskDoneView.as_view(), name='task-done'),
    path('accounts/', include('django.contrib.auth.urls')),
]