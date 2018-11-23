from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import login, logout

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.register, name='register'),
    path('accounts/userdetail', views.user_detail, name='profile'),
    path('accounts/userdetail/edit', views.user_edit_detail, name='editprofile'),
    path('accounts/userdetail/change_password', views.change_password, name='change_password'),
]
