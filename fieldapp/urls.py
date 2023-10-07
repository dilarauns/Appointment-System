"""
URL configuration for fieldapp project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #included the urls in the field in my fieldapp main application.
    # A parameter to be added inside quotes will be added to the end of the URLs.
    
    #http://127.0.0.1:8000/user/  - index
    #http://127.0.0.1:8000/user/field/5  - The specified record in the database will be returned

    
    
    path('', include('field.urls'))  
    
]
