from django.urls import path
from . import views

urlpatterns = [
    path('', views.experiment_list, name='experiment_list'),
    path('add/', views.add_experiment, name='add_experiment'),
]
