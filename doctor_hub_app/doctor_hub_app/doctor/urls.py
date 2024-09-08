from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('doctor/<int:doctor_id>/', views.doctor_info, name='doctor_info'),
]