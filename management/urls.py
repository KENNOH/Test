from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^edit/(?P<pk>[0-9]+)', views.edit, name="edit"),
    url(r'^delete/', views.delete, name="delete"),
    url(r'^view_assets/', views.view_assets, name="view_assets"),
    url(r'^add_asset/', views.add_asset, name="add_asset"),
    url(r'^', views.base,name="base"),
    
]
