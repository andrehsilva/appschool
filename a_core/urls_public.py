from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from a_users.views import profile_view
from a_tenant_manager.admin import tenant_admin_site
from a_home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_tenants/', tenant_admin_site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('a_home.urls')),
    path('profile/', include('a_users.urls')),
    path('@<username>/', profile_view, name="profile"),
]

# Only used when DEBUG=True, whitenoise can serve files when DEBUG=False
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)