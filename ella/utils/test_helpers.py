# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from PIL import Image

try:
    from io import BytesIO
except ImportError:
    from cStringIO import StringIO as BytesIO

from django.utils import six
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.template.defaultfilters import slugify

from ella.core.models import Category, Publishable, Listing
# choose Article as an example publishable
from ella.articles.models import Article
from ella.photos.models import Photo
from ella.utils.timezone import utc_localize

default_time = utc_localize(datetime(2008, 1, 10))


def create_category(title, tree_parent=None, **kwargs):
    defaults = {
        'site_id': getattr(settings, "SITE_ID", 1),
        'slug': slugify(title),
    }
    defaults.update(kwargs)
    if isinstance(tree_parent, six.string_types):
        tree_parent = Category.objects.get_by_tree_path(tree_parent)
    cat, created = Category.objects.get_or_create(tree_parent=tree_parent, title=title, defaults=defaults)
    return cat


def create_basic_categories(case):
    case.site_id = getattr(settings, "SITE_ID", 1)

    case.category = create_category("你好 category",
        description="exmple testing category",
        slug="ni-hao-category",
    )

    case.category_nested = create_category(
        "nested category",
        tree_parent=case.category,
        description="category nested in case.category",
    )

    case.category_nested_second = create_category(
        " second nested category",
        tree_parent='nested-category',
        description="category nested in case.category_nested",
        slug="second-nested-category",
    )
    case.addCleanup(Category.objects.clear_cache)


def create_and_place_a_publishable(case, **kwargs):
    defaults = dict(
        title='First Article',
        slug='first-article',
        description='Some\nlonger\ntext',
        category=case.category_nested,
        publish_from=default_time,
        published=True,
        content='Some even longer test. \n' * 5
    )
    defaults.update(kwargs)
    case.publishable = Article.objects.create(**defaults)
    case.only_publishable = Publishable.objects.get(pk=case.publishable.pk)


def create_photo(case, color="black", size=(200, 100), **kwargs):
    # prepare image in temporary directory
    file = BytesIO()
    case.image = Image.new('RGB', size, color)
    case.image.save(file, format="jpeg")

    f = InMemoryUploadedFile(
            file=file,
            field_name='image',
            name='example-photo.jpg',
            content_type='image/jpeg',
            size=len(file.getvalue()),
            charset=None
        )

    data = dict(
        title="Example 中文 photo",
        slug="example-photo",
        height=size[0],
        width=size[1],
    )
    data.update(kwargs)

    case.photo = Photo(**data)
    image_field = Photo._meta.get_field('image')
    image_field.save_form_data(case.photo, f)

    case.photo.save()
    case.photo._pil_image = case.image

    return case.photo


def list_publishable_in_category(case, publishable, category=None, publish_from=None):

    case.listing = Listing.objects.get_or_create(
        publishable=publishable,
        category=category or publishable.category,
        publish_from=publish_from or publishable.publish_from,
    )[0]
