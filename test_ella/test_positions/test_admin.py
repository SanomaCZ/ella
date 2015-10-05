# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from nose import tools

from django.contrib import admin

from ella.core.models import Source
from ella.positions.admin import PositionOptions
from ella.positions.models import Position

from test_ella.test_core import create_basic_categories, create_and_place_a_publishable


class TestPositionAdmin(TestCase):

    def setUp(self):
        super(TestPositionAdmin, self).setUp()
        create_basic_categories(self)
        create_and_place_a_publishable(self)
        self.position_admin = PositionOptions(model=Position, admin_site=admin.site)

    def test_result_of_show_title_for_obj_with_title_attr(self):
        p = Position()
        p.target = self.publishable
        tools.assert_equals('First Article [Article]', self.position_admin.show_title(p))

    def test_result_of_show_title_for_obj_without_title_attr(self):
        source = Source.objects.create(name='Hi!')
        p = Position()
        p.target = source
        tools.assert_equals('Hi! [Source]', self.position_admin.show_title(p))

    def test_result_of_show_title_for_position_without_trget(self):
        p = Position()
        tools.assert_true(self.position_admin.show_title(p).startswith('--'))
