from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cities', views.cities, name='cities'),
    path('countries', views.countries, name='countries'),
    path('page', views.page, name='page'),
    path('error/<int:question_id>', views.error, name='error'),
]