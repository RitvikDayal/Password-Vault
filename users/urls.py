from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='signup'),
    path('user-profile/', views.profile, name='user-profile'),
    path('user-profile/update', views.updateProfile, name='profile-update'),
]