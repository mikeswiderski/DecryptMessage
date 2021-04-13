from django.urls import path

from apps.decrypt import views

urlpatterns = [
    path('', views.decrypt, name='decrypt'),
]
