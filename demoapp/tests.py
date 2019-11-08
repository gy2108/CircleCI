from django.test import TestCase
import unittest
from demoapp.views import dem

class doTest(unittest.TestCase):

    def test_dem(self):
        self.assertEqual(dem(),"hello")
