# sections/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page displaying sections
    path('section/<int:section_id>/', views.section_detail, name='section_detail'),  # Section detail page
]
