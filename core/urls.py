"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home.views import *
from add_form.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('home/',home,name='home'),
    path('Result/',result_page,name='res_page'),
    path('Addmission_form/',Addmission_form,name='Addmission_form'),
    path('show_data/',show_data,name='show_data'), 
    path('delete_data/<id>/',delete_data,name='delete_data'), 
    path('update_data/<id>/',update_data,name='update_data'), 
    path('',log_in,name='login'),
    path('logout/',log_out,name='logout'),
    path('sign_up/',sign_up,name='sign_up'),
    path('About/',about_page,name='about'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()
     