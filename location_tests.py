import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        """this tests the __repr__ function to see if it prints the correct string
        representation for a specific Location object"""
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("Folsom", 67.3, -90.0)
        loc3 = Location("Davis", 0.0, 100.0)

        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc2), "Location('Folsom', 67.3, -90.0)")
        self.assertEqual(repr(loc3), "Location('Davis', 0.0, 100.0)")

    def test_eq(self):
        """this tests the __eq__ function to see if two Locations are equal
        or not"""
        loc4 = Location("SLO", 35.3, -120.7)
        loc5 = Location("Sacramento", 40.0, -90.0)
        loc6 = Location("San Diego", 30.4, -150.5)
        loc7 = "San Francisco"
        loc8 = loc4
        loc9 = Location("Sacramento", 40.0, -90.0)

        self.assertFalse(loc4 == loc5)
        self.assertFalse(loc4 == loc5)
        self.assertFalse(loc7 == loc4)
        self.assertFalse(loc4 == loc7)
        self.assertFalse(loc4 == loc5)
        self.assertTrue(loc5 == loc9)
        self.assertTrue(loc4 == loc8)
        self.assertFalse(loc6 == loc5)


if __name__ == "__main__":
    unittest.main()
