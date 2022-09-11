from django.test import TestCase, Client
from django.urls import reverse


## test the ping route works

class TestPing(TestCase):
    def test_ping(self):
        response = self.client.get(reverse('test'))
        self.assert_(response.status_code, 200)

