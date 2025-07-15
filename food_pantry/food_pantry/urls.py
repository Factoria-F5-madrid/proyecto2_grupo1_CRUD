"""
URL configuration for food_pantry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import include, path
from django.contrib import admin




urlpatterns = [
    path('admin/', admin.site.urls),
    path('food_pantry/', include('food_pantry_app.urls.urls_app')),
    #path('food_pantry/api', urls) TODO. Change this to the right file
    #path('food_pantry/doc', )      TODO.  to be completed
]
