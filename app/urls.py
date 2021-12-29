"""express_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views


urlpatterns = [
    path("storefloorplan", views.storeFloorPlan_, name="storesetup"),
    path("storefixtures", views.storeFixtures_, name="gandolaShelves"),
    path("cameraService", views.cameraService_, name="cameraService"),
    path("cameraInfo", views.cameraInfo_, name="camerainfo"),
    path("groundplot", views.groundplot_, name="groundplot"),
    path("cartManager", views.cartManager_, name="cartManager"),
    path("all", views.all_, name="all"),
]
