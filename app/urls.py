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
   
    path("mgondola", views.mgondola_, name="mgondola"),
    path("fgondola", views.fgondola_, name="fgondola"),
    path("locationsetup", views.locationSetup_, name="locationSetup"),
    path("camera", views.cameraandGPU_, name="cameraandGPU"), 
    path("cartmanager", views.cartManager_, name="cartManager"),
    path("groundplot", views.groundplot_, name="groundplot"),  
    path("turnstile", views.turnstile_, name="turnstile"),
    path("storedimension", views.storeDimension_, name="storeDimension"),
]
