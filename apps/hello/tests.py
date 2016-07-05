# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_unicode
from apps.hello.models import Person


class ContactPageTest(TestCase):
    """ Tests for root page with contacts """

    def setUp(self):
        self.response = self.client.get(reverse('contact_page_view'))

    def test_title_on_page(self):
        """ Test for contact page title """

        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, '42 Coffee Cups Test Assignment')

    def test_some_person_data(self):
        """ Test for person name and surname """

        self.person = Person.objects.first()

        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, self.person.first_name)
        self.assertContains(self.response, self.person.last_name)


class PersonModelTest(TestCase):
    """ Test for Person model """

    def test_person_unicode(self):
        """ Test for person model unicode title """

        person = Person.objects.create(
            first_name="Альберт",
            last_name="Üleõle",
            email="email@email.com",
            jabber="jabber@test.com"
        )
        self.assertEqual(
            smart_unicode(person),
            "{} {}".format(person.first_name, person.last_name)
        )
