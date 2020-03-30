from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('media/', views.media, name='media'),
]
