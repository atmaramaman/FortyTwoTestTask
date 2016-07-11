# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_unicode
from apps.hello.models import Person

from django.http import HttpRequest
from django.shortcuts import render


class ContactPageTest(TestCase):
    """ Tests for main page with contacts """

    def setUp(self):
        self.response = self.client.get(reverse('contact_page_view'))

    def test_title_on_page(self):
        """ Test for contact page title """

        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, '42 Coffee Cups Test Assignment')


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


class PersonDataViewTest(TestCase):
    """Test person data view."""

    def test_displaying_person_data_on_page(self):
        """Test for displaying person data on page."""

        # The database is empty
        no_person = None
        request = HttpRequest()
        response = render(request, 'contact_page.html', {'person': no_person})
        self.assertContains(response, 'The database is empty.')

        # One person in database
        person_1 = Person.objects.first()
        self.assertEqual(1, Person.objects.count())
        response = self.client.get(reverse('contact_page_view'))
        self.assertContains(response, person_1.first_name)

        # Two and more persons in database
        person_2 = Person.objects.create(
            first_name='Second',
            last_name='Person',
            email='second0@email.com',
            jabber='jabber@test.com'
        )
        self.assertEqual(2, Person.objects.count())
        response = self.client.get(reverse('contact_page_view'))
        self.assertContains(response, person_1.first_name)
        self.assertNotContains(response, person_2.first_name)


class RequestsPageTest(TestCase):
    """ Test for requests page """

    def test_hard_coded_data_on_page(self):
        """ Test for requests page with hard-coded data """
        response = self.client.get(reverse('requests_page_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'GET')
        self.assertContains(response, '/')
        self.assertContains(response, '1989-12-22')
