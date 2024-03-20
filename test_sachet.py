import unittest
from Grain import Grain
from Sachet import Sachet

class TestSachat(unittest.TestCase):
    def test_composition_grain(self):
        compostion_grain_valid = Grain("Vietnam", "Floral", 2020, 6)
        sachet_valid = Sachet(500,"mixte",[compostion_grain_valid],[30,40,30])
        sachet_invalid = Sachet(2001,"mixte",[],[50,40,50])
        self.assertTrue(sachet_valid.composition_grain())
        self.assertFalse(sachet_invalid.composition_grain())
    
if __name__ == "__main__":
    unittest.main()
