from django.urls import path
from .views import ViewToDoListAPI, ViewToDoListCreateAPI, ViewToDoListDeleteAPI, ViewToDoListUpdateAPI, \
    ViewToDoListDetailAPI

urlpatterns = [
    path('', ViewToDoListAPI.as_view(), name='view-to-do-list'),
    path('create/', ViewToDoListCreateAPI.as_view(), name='view-to-do-list-create'),
    path('delete/<int:pk>/', ViewToDoListDeleteAPI.as_view(), name='view-to-do-list-delete'),
    path('update/<int:pk>/', ViewToDoListUpdateAPI.as_view(), name='view-to-do-list-update'),
    path('<int:pk>/', ViewToDoListDetailAPI.as_view(), name='view-to-do-list-detail'),
]
