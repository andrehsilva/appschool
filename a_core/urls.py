"""
URL configuration for a_core project.

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from a_users.views import profile_view
from a_home.views import *
from blog.views import *

urlpatterns = [
  
    path('admin/', admin.site.urls),
    #path('admin/school/', include('school.urls')),
    path('', include('blog.urls', namespace='blog')),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('a_users.urls')),
    path('contact/', include('contact.urls')),
    path('message/', include('message.urls', namespace='message')),
    path('books/', include('books.urls', namespace='books')),
    path('school/', include('school.urls')), 
    path('collection/', include('collection.urls')),
    path('notification/', include('notification.urls')),
    path('ticket/', include('ticket.urls', namespace='ticket')),
    path('notes/', include('note.urls')), # Suas notas
    path('@<username>/', profile_view, name="profile"),

    #dashboard
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),

]

# Only used when DEBUG=True, whitenoise can serve files when DEBUG=False
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

