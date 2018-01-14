from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.staticfiles import views

urlpatterns = [
    url(r'^static/(?P<path>.*)$', views.serve, kwargs={'insecure':True}),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
