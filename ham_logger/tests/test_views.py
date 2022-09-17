from django.test import TestCase, Client
from django.urls import reverse
from ham_logger.models import Contact

# class to hold our test cases
class ContactTests(TestCase):
  #setup

    def setUp(self) -> None:
        self.contact1 = Contact.objects.create(
            callsign = 'test',
            name = 'joe johnson',
            country = 'foo',
            state = 'bar',
            mode =  'DMR',
            freq = 123.49,
            power = 1220

        )
    # test create views
    def test_create_view_template(self):
        response= self.client.get(reverse('contact_create'))
        self.assertTemplateUsed(response, 'contact_new')

    #def test_index_view_template(self):
    #    response= self.client.get(reverse('contact_list'))
#
    #test the create method
    def test_contact_create(self):
        response = self.client.post(reverse('contact_create'),{
            'callsign':  'test2',
            'name': 'joe blow',
            'country':  'foo',
            'state':  'bar',
            'mode':   'DMR',
            'freq':  123.49,
            'power':  1220
        })
        self.assertEqual(response.status_code, 204)
        self.assertContains(response, 'test2')