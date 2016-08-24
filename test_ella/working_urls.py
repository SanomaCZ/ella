from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from test_ella.urls import urlpatterns


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
