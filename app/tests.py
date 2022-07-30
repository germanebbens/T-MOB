from django.test import TestCase
from .models import Redirect
from django.core.cache import cache

class SimpleTest(TestCase):

    def setUpTestData():                                     
        Redirect.objects.create(
            key="goo", 
            url="www.google.com",
            active=True
        )
        Redirect.objects.create(
            key="fbk", 
            url="www.facebook.com",
            active=False
        )


    def test_integration(self):
        self.assertEqual(str(cache.get("goo")), "{'key': 'goo', 'url': 'www.google.com'}")
        self.assertEqual(cache.get("fbk"), None)

