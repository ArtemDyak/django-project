from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='forum_index'),
    path('new_message', views.new_message, name='new_message')
]
