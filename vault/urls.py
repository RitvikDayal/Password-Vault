from django.urls import path
from . import views
urlpatterns = [
    path('', views.patterns, name='api-patterns'),
    path('cred-list/', views.credList, name='cred-list'),
    path('cred-detail/<str:pk>', views.credDetail, name='cred-detail'),
]