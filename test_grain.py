import unittest
from Grain import Grain

class TestGrain(unittest.TestCase):
    def test_is_valid(self):
        grain_valid = Grain("Vietnam", "Floral", 2019, 6)
        grain_invalid = Grain("France", "Fruite",2023,10)
        self.assertTrue(grain_valid.is_valid())
        self.assertFalse(grain_invalid.is_valid())

if __name__ == "__main__":
    unittest.main()
