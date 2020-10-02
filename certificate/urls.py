from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='certificate-home'),
    path('about/', views.about, name='certificate-about'),
]
