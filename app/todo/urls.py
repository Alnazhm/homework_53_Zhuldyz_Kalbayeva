from django.urls import path
from todo.views.base import index_view
from todo.views.create_task import add_view, detail_view, delete_task_view


urlpatterns = [
    path('', index_view, name='index'),
    path('tasks/add/', add_view, name='task_add'),
    path('tasks/<int:pk>', detail_view, name='task_detail'),
    path('tasks/del/<int:pk>', delete_task_view, name='task_deleted')
]