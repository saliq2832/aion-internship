from django.urls import path
from . import views
from .views import post_list

urlpatterns = [
    
    path('simple-page/', views.simple_page, name='simple_page'),
    path('simple-api/', views.post_list),
    path('simple-api/create/', views.post_create),
    path('simple-api/<int:pk>/', views.post_retrieve),
    path('simple-api/<int:pk>/update/', views.post_update),
    path('simple-api/<int:pk>/delete/', views.post_delete),
    
    
]
