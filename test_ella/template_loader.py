from unittest import TestCase

from django.template import TemplateDoesNotExist

try:
    from django.template.loaders.base import Loader as BaseLoader
except ImportError:
    from django.template.loader import BaseLoader

try:
    from django.template import Origin
except ImportError:
    has_origin = False
else:
    has_origin = True

from nose import tools


templates = {}


class GlobalMemTemplateLoader(BaseLoader):
    is_usable = True

    def __init__(self, *args, **kwargs):
        super(GlobalMemTemplateLoader, self).__init__(*args, **kwargs)

    def __call__(self, template_name, template_dirs=None):
        return self.load_template(template_name, template_dirs)

    def load_template(self, template_name, template_dirs=None):
        "Dummy template loader that returns templates from templates dictionary."
        try:
            return templates[template_name], template_name
        except KeyError as e:
            raise TemplateDoesNotExist(e)

    def get_contents(self, origin):
        try:
            return templates[origin.name]
        except KeyError:
            raise TemplateDoesNotExist(origin)

    def get_template_sources(self, template_name):
        if has_origin:
            yield Origin(
                name=template_name,
                template_name=template_name,
                loader=self,
            )

    def load_template_source(self, template_name, template_dirs=None):
        return self.load_template(template_name, template_dirs)


class TestDummyTemplateLoader(TestCase):

    def tearDown(self):
        global templates
        templates = {}

    def test_simple(self):
        loader = GlobalMemTemplateLoader()
        templates['anything.html'] = 'Something'
        source, name = loader.load_template_source('anything.html')
        tools.assert_equals('anything.html', name)
        tools.assert_equals('Something', source)

    def test_empty(self):
        loader = GlobalMemTemplateLoader()
        tools.assert_raises(TemplateDoesNotExist, loader.load_template_source, 'anything.html')
