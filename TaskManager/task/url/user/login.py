from django.urls import path
from task.view.user.login import *

urlpatterns = [
    path('',LoginAPI.as_view()),
    path('register/',RegisterAPI.as_view()),
]