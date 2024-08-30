"""reward_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reward_system import views
from admin_app import views as admin_view
from user_app import views as user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('admin_signup/',views.register_admin,name='admin_signup'),
    path('user_signup/',views.register_user,name='user_signup'),
    path('add_app/',include('admin_app.urls')),
    path('logout',include('admin_app.urls')),
    path('admin_dash/<int:id>/', views.admin_dash_view, name='admin_dash'),
    path('user_dash/<int:id>', user_view.user_dash_view, name='user_dash'),
    path('edit_app/<int:id>/', admin_view.edit_app, name='edit_app'),
    path('delete_app/<int:id>/', admin_view.delete_app, name='delete_app'),
    path('download_action/<int:id>/<int:user_id>/<int:points>/',user_view.download_done,name='download_action')
]



