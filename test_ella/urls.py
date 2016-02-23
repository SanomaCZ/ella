try:
    from django.conf.urls import patterns, include
except ImportError:
    from django.conf.urls.defaults import patterns, include

from ella.utils.installedapps import call_modules

call_modules(('register', ))

urlpatterns = patterns('',
    (r'^', include('ella.core.urls')),
)
