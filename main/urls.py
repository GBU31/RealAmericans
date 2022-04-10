from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('login', views.Login, name='login'),
    path('signup', views.signup, name='signup'), 
    path('post/<int:pk>', views.get_post, name='get_post'),
    path('logout', views.Logout),
    path('notifications', views.notifications, name='notifications'),
    path('pfp', views.add_pfp)
]