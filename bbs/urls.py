from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='message_list'),
    path('message_list/', views.index, name='message_list'),
    path('message_detail/<int:id>/', views.message_detail, name='message_detail'),
    path('message_create/', views.message_create, name='message_create'),
    path('message_update/<int:id>/', views.message_update),
    path('message_delete/<int:id>/', views.message_delete),
]