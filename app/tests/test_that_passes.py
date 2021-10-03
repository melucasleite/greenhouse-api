from django.test import TestCase


class TestOne(TestCase):
    def test_that_fails(self):
        """This test shall pass"""
        self.assertEqual(True, True)
