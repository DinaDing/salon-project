from django.urls import path, include
from django.contrib import admin

urlpatterns = [
	path('', include('haircut.urls')),
	path('admin/', admin.site.urls),
]