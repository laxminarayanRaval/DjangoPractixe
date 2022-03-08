from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:que_id>/', views.detail, name='detail'),
    path('<int:que_id>/result', views.results, name='results'),
    path('<int:que_id>/vote', views.vote, name='vote')
]