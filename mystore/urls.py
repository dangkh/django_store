from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import login, logout

urlpatterns = [
    path('', views.index, name='index'),
    path('citys/', views.CityListView.as_view(), name='citys'),
    path('city/<int:pk>', views.CityDetailView.as_view(), name='city_detail'),
    path('city/create/', views.CityCreate.as_view(), name='city_create'),
    path('city/<int:pk>/update/', views.CityUpdate.as_view(), name='city_update'),
    path('city/<int:pk>/delete/', views.CityDelete.as_view(), name='city_delete'),
    path('stores/', views.StoreListView.as_view(), name='stores'),
    path('stores/<int:pk>', views.StoreDetailView.as_view(), name='store_detail'),
    path('stores/create/', views.StoreCreate.as_view(), name='store_create'),
    path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='store_update'),
    path('stores/<int:pk>/delete/', views.StoreDelete.as_view(), name='store_delete'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.register, name='register'),
    path('accounts/userdetail', views.user_detail, name='profile'),
    path('accounts/userdetail/edit', views.user_edit_detail, name='editprofile'),
    path('accounts/userdetail/change_password', views.change_password, name='change_password'),
]
