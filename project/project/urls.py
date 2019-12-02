"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from squirreldata.views import sighting_list_view,sighting_update_view,sighting_create_view,sighting_delete_view,maps

urlpatterns = [
    path('maps/',maps),
    path('sightings/',sighting_list_view),
    path('sightings/<slug:update_id>/update/',sighting_update_view,name='sighting-detail'),
    path('sightings/add/',sighting_create_view), 
    path('sightings/<slug:delete_id>/delete/',sighting_delete_view,name='sighting-detail'),
    path('admin/', admin.site.urls),
]
