from django.urls import path
from . import views

app_name = 'shortener_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/', views.redirect_url, name='redirect_url'),
]