from django.contrib import admin
from django.urls import path, include
from fileupload.views import serve_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fileupload.urls')),  # Include the fileupload app URLs
    path('', serve_html, name='home'),  # Serve HTML at the root URL

]
