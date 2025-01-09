import unittest
from controller import Controller

class ControllerTest (unittest.TestCase):

    Controller_Instance = None
    
    @classmethod
    def setUpClass (cls):
        cls.Controller_Instance = Controller("Controller_Instance", 0, [1, 2, 3], [])

    @classmethod
    def tearDownClass (cls):
        cls.Controller_Instance = None


    def test_01_initial (self):
        frequencies = {2: 4, 1: 3, 3: 3, 6: 3, 7: 2, 4: 3, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 5: 2, 11: 1, 12: 2, 13: 1, 8: 2, 10: 2, 9: 1, 14: 1} # 18 elements
        print(self.Controller_Instance.sort_frequencies(frequencies))
        self.assertTrue(False)
        expected_sorted_frequencies = {9:1, 14:1, 16:1, 17:1, 18:1, 19:1, 20:1, 11:1, 13:1, 5:2, 7:2, 12:2, 8:2, 10:2, 1:3, 3:3, 4:3, 6:3, 2:4}
        # real_sorted_frequencies = self.Controller_Instance.sort_frequencies(frequencies)

        self.assertEqual(expected_sorted_frequencies, frequencies)
        
if __name__ == '__main__':
    unittest.main()