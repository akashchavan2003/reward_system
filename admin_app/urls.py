from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from reward_system import views as reward_views


urlpatterns = [
    # path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # path('admin_signup/', include('reward_system.urls')),
    path('add_app/',add_app_view,name='add_app'),
    path('logout/', logout_view, name='logout'), 
    path('admin_signup',reward_views.register_admin,name='admin_signup')
    
]
