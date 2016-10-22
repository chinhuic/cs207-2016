
from binsearch import binary_search
import unittest
import numbers
import numpy as np
from fractions import Fraction

input1 = range(10)
input2 = [20, 23, 23, 45, 45, 78, 79]

class MyTest(unittest.TestCase):
    # all of them have test_xxx so that unittest main can run it
    
    def test_value_found(self):
        self.assertEqual(binary_search(input1, 5),5)
        self.assertEqual(binary_search([5], 5),0)
    
    def test_value_found_dup(self):
        self.assertIn(binary_search(input2, 23), (1,2))
        self.assertIn(binary_search(input2, 45), (3,4))
    
    def test_value_not_found(self):
        self.assertEqual(binary_search(input1, -5.5),-1)
        self.assertEqual(binary_search(input1, 50),-1)
        self.assertEqual(binary_search([5], -2),-1)
    
    def test_with_inf(self):
        self.assertEqual(binary_search([1,2, np.inf], 2),1)
        self.assertEqual(binary_search([1, 2, 5 , 6,8 , np.inf], np.inf), 5)
        self.assertEqual(binary_search([1,np.inf, 2, 5 , 6], -4), -1)
        self.assertEqual(binary_search([1,np.inf, 2, 5 , 6], 10), -1)
        
    def test_with_NaN(self):
        self.assertEqual(binary_search([np.nan, 2, 5 , 6], 2),1)
        self.assertTrue(binary_search([np.nan, 2, 5 , 6], np.nan), numbers.Real)
        self.assertEqual(binary_search([1,np.nan, 2, 5 , 6], -4), -1)
        self.assertEqual(binary_search([1,np.nan, 2, 5 , 6], 10), -1)
        
    def test_with_left_right_parameters(self):
        self.assertEqual(binary_search(input1, 5, 1, 3), -1)
        self.assertEqual(binary_search(input1, 2, 1, 3), 2)
        self.assertEqual(binary_search(input1, 2, 3, 1), -1)
        self.assertEqual(binary_search(input1, 2, 2, 2), 2)
        self.assertEqual(binary_search(input1, 5, 2, 2), -1)
        
    def test_with_empty_array(self):
        self.assertEqual(binary_search([], 5),-1)
        
    def test_char(self):
        with self.assertRaises(TypeError):
            binary_search(['a', 6], 7)
            
    def test_char(self):
        with self.assertRaises(TypeError):
            binary_search([2, 6], 'a')
            
    def test_with_fraction(self):
        self.assertEqual(binary_search([Fraction(1,6),Fraction(7/9), 5, 10 ], 5), 2)
        

if __name__ == '__main__':
    unittest.main()