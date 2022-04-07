from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('login', views.Login, name='login'),
    path('signup', views.signup, name='signup'), 
    path('logout', views.Logout)
]