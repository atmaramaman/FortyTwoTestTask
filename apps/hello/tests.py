# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class ContactPageTest(TestCase):
    """ Test for root page with contacts """

    def setUp(self):
        self.response = self.client.get(reverse('contact_page_view'))

    def test_title_on_page(self):
        """ Test for contact page title """

        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, '42 Coffee Cups Test Assignment')
