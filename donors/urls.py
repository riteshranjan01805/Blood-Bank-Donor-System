from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_donor, name='register'),
    path('login/', views.donor_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('request/', views.request_blood, name='request_blood'),
    path('donors/', views.donor_list, name='donor_list'),
]
