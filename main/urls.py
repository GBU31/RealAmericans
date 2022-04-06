from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('login', views.Login),
    path('signup', views.signup),]
    