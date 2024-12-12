from django.urls import path
from users.views import UserView, user_projects

urlpatterns = [  
    path('', UserView.as_view(), name='users_list'),
    path('<int:user_id>/projects/', user_projects, name='projects-by-user'),
]
