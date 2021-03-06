"""health_up URL Configuration

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
from django.urls import path
from health.views import client_view
from health.views import service_view
from health.views import booking_view
from health.views import search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', client_view),
    path('service/', service_view),
    path('booking/', booking_view),
    path('search/', search_view)
]
