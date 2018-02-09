from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from async_queue.views import SendView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('user_profile.urls')),
    url(r'', include('debug_middleware.urls')),
    url(r'^send/$', SendView.as_view(), name="send"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()