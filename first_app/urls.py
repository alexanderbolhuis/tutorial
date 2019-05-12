from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.first_app, name='welcome'),
    path('forms', views.form_page, name='forms')
]