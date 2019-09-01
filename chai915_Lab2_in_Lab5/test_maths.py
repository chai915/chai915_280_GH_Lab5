import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        
        self.assertEqual(maths.add(4, 8), 12)
        self.assertEqual(maths.add(5, 12, None), 17)
        self.assertEqual(maths.add(6, 23, 6), '45')
        self.assertEqual(maths.add(88, 45, 16), '85')
        
        

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''

        self.assertEqual(maths.fibonacci(5), 5)
        self.assertEqual(maths.fibonacci(0), 1)
        self.assertEqual(maths.fibonacci(8), 21)


    def test_convert_base(self):
        ''' Tests the convert base function. '''
        
        self.assertEqual(maths.convert_base(16, 2), '10000')
        self.assertEqual(maths.convert_base(40, 16), '28')
        
        
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
