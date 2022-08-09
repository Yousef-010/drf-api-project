from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Thing


class ThingTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester', password='test1234')
        test_user.save()
        test_thing = Thing.objects.create(
            purchaser=test_user,
            name="test_name",
            category = 'test_category',
            price = 15,
            description="test_description",
        )
        test_thing.save()

    def test_thing_model(self):
        thing = Thing.objects.get(pk=1)
        self.assertEqual(str(thing.purchaser), 'tester')
        self.assertEqual(str(thing.name), 'test_name')
        self.assertEqual(str(thing.description), 'test_description')
