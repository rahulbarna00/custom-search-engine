from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('searchEngineApp.urls'))
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)