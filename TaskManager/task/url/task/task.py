from django.urls import path
from task.view.task.task import *

urlpatterns = [
    path('',TaskAPI.as_view()),
    path('status/',TaskStatusAPI.as_view()),
]