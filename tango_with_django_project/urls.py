from django.conf.urls import url, include
from django.contrib import admin
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)