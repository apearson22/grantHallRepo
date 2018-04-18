from django.test import TestCase
from users.models import Cadet

class CadetTestCase(TestCase):
	def setUp(self):
		Cadet.objects.create(first="John", last="Doe", xnumber="x12345")
		Cadet.objects.create(first="Jane", last="Doe", xnumber="x54321")

	def test_cadets(self):
		"""Test to make sure all cadets have the name attribute, and an x number."""
		johndoe = Cadet.objects.get(xnumber="x12345")
		janedoe = Cadet.objects.get(xnumber="x54321")
		self.assertEqual(johndoe.name(), 'Doe, John')
		self.assertEqual(janedoe.name(), 'Doe, Jane')
