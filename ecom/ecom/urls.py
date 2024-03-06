"""
URL configuration for ecom project.

"""
from django.contrib import admin
from django.urls import path, include
from django.contrib. staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('bkndata/', include('bcknd.urls')),
    path('frnt/', include('frontnd.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

