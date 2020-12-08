from django.urls import path
from .import views

urlpatterns = [
    path("",views.index),
    path("todo/",views.index),
    path("addTodo/",views.addTodo),
    path("delTodo/<int:del_id>",views.delTodo),
]
