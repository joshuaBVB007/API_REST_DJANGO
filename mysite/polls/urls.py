from django.urls import path


# we imported the views from views.py,then we're gonna call the methods detail,results and vote
from . import views


# Namespace for this app
app_name='polls'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:id>/vote/', views.vote, name='vote'),
]

# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:id>/vote/', views.vote, name='vote'),
# ]