

import unittest

from mymath import myaverage

class MyTest(unittest.TestCase):
    
    def test_mymath(self):
        # self is an instance of the class
        self.assertEqual(myaverage([2,3]), 2.5)

if __name__ == '__main__':
    unittest.main()