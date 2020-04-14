# coding: utf-8
from __future__ import unicode_literals, print_function, division, absolute_import
import os
import unittest

from django.core.urlresolvers import reverse

from onadata.apps.main.views import clone_xlsform
from onadata.apps.logger.models import XForm
from test_base import TestBase


class TestFormGallery(TestBase):

    def setUp(self):
        TestBase.setUp(self)
        self._create_user_and_login()
        self._publish_transportation_form()
        self.url = reverse(clone_xlsform,
                           kwargs={'username': self.user.username})

    def test_require_logged_in_user(self):
        count = XForm.objects.count()
        self.anon.post(self.url)
        self.assertEqual(count, XForm.objects.count())

    def test_clone_for_other_user(self):
        self._create_user_and_login('alice', 'alice')
        count = XForm.objects.count()
        self.client.post(
            self.url, {'id_string': self.xform.id_string, 'username': 'bob'})
        self.assertEqual(count + 1, XForm.objects.count())

    @unittest.skip('Fails under Django 1.6')
    def test_clone_with_username_and_id_string_in_uppercase(self):
        self._create_user_and_login('alice', 'alice')
        count = XForm.objects.count()
        self.client.post(
            self.url, {'id_string': self.xform.id_string.upper(),
                       'username': 'bob'.upper()})
        self.assertEqual(count + 1, XForm.objects.count())

    def test_clone_id_string_starts_with_number(self):
        self._publish_transportation_id_string_starts_with_number_form()
        # The following lines are useless since `self.xform.id_string` does not
        # start with numbers.
        self._create_user_and_login('alice', 'alice')
        count = XForm.objects.count()
        self.client.post(
            self.url, {'id_string': self.xform.id_string, 'username': 'bob'})
        self.assertEqual(count + 1, XForm.objects.count())

    def _publish_transportation_id_string_starts_with_number_form(self):
        xls_path = os.path.join(self.this_directory, "fixtures",
                                "transportation",
                                "transportation.id_starts_with_num.xls")
        count = XForm.objects.count()
        response = TestBase._publish_xls_file(self, xls_path)

        self.assertContains(response, 'Names must begin with a letter')
        self.assertEqual(XForm.objects.count(), count)
        self.xform = XForm.objects.all().reverse()[0]
