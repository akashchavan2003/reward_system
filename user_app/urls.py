from django.urls import path, include
from user_app import views
from reward_system import views as reward_views

urlpatterns = [
    # path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user_signup/',reward_views.register_user,name='user_signup'),
    
]
