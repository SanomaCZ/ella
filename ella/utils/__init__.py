from django.core.exceptions import ImproperlyConfigured

try:
    from django.apps import apps
except ImportError:  # django < 1.7
    from django.db.models.loading import get_model, get_models
else:
    get_model = apps.get_model
    get_models = apps.get_models

try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module


def import_module_member(modstr, noun=''):
    module, attr = modstr.rsplit('.', 1)
    try:
        mod = import_module(module)
    except ImportError as e:
        raise ImproperlyConfigured('Error importing %s %s: "%s"' % (noun, modstr, e))
    try:
        member = getattr(mod, attr)
    except AttributeError as e:
        raise ImproperlyConfigured('Error importing %s %s: "%s"' % (noun, modstr, e))
    return member
