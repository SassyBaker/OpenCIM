from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('core/', include('core.urls')),
    path('idc/', include('idc.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

admin.site.site_header = "OpenCIM"
admin.site.site_title = "OpenCIM Admin Area"
admin.site.index_title = "Welcome to OpenCIM admin area"
