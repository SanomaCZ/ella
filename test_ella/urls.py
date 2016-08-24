from django.conf.urls import include, url

from ella.utils.installedapps import call_modules

call_modules(('register', ))

urlpatterns = [
    url(r'^', include('ella.core.urls')),
]
