from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from content_management import views  # content_management uygulamasından views'i ekliyoruz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('content_management/', include('content_management.urls')),
    path('ckeditor/', include('django_ckeditor_5.urls')),
    path('', views.home, name='home'),  # Ana sayfa için boş path yönlendirmesi
]

# Statik ve medya dosyaları için ayar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
