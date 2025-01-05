from django.urls import path
from . import views

urlpatterns = [
    path('', views.checklist, name='checklist'),  
    path('add_item/', views.add_item, name='add_item'),
    path('complete/<int:item_id>/', views.complete_item, name='complete_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('view_checklist/', views.view_checklist, name='view_checklist'),
    path('verify/', views.verify_checklist, name='verify_checklist'),
]
