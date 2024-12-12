from django.urls import path
from .views import ProjectDetail, ProjectView, ProjectTaskView

urlpatterns = [  
    path('', ProjectView.as_view(), name='project_list'),
    path('<int:pk>/', ProjectDetail.as_view(), name='project_detail'),
    path('<int:pk>/tasks/', ProjectTaskView.as_view({'get':'get_byProject'}), name='project_tasks'),
]