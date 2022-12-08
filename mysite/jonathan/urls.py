from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.view, name='results'),
    path('<int:id>/surname/', views.surname, name='results'),
]