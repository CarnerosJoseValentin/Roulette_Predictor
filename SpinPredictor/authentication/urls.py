from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_signup, name='login_signup'),
    path('profile/', views.profile_view, name='profile'),
]
