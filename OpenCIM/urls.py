from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('central/', include('central.urls')),
    path('idc/', include('idc.urls')),
]

admin.site.site_header = "OpenCIM"
admin.site.site_title = "OpenCIM Admin Area"
admin.site.index_title = "Welcome to OpenCIM admin area"
