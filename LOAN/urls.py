"""
URL configuration for LOAN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from loanapp.views import homepage, AddClient, ClientList, ClientDisplay, ClientUpdate, ClientDelete, CollateralDisplay 
from loanapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
     #path('', views.homepage, name='homepage'),
    path('', homepage.as_view(), name='homepage'),
    #path('addclient/', AddClient.as_view(), name='add_client'),
    path('addclient/', AddClient.as_view(), name='add_client'),
    path('clientlist/', ClientList.as_view(), name='clientlist' ),
    path('clientdisplay/<int:pk>', ClientDisplay.as_view(), name='clientdisplay'),
    path('clientupdate/<int:pk>',ClientUpdate.as_view(), name='clientupdate'),
    path('clientdelete/<int:pk>', ClientDelete.as_view(), name='clientdelete'),
    path('collateral/', views.CollateralDisplay, name='collateral'),
    
]
