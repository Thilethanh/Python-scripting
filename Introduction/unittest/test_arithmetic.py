import arithmetic
import unittest


# Testing add_numbers function from arithmetic.
class Test_addition(unittest.TestCase):
    # Testing Integers
    def test_add_numbers_int(self):
        sum = arithmetic.add_numbers(50, 50)
        self.assertEqual(sum, 100)

    # Testing Floats
    def test_add_numbers_float(self):
        sum = arithmetic.add_numbers(50.55, 78)
        self.assertEqual(sum, 128.55)

    # Testing Strings
    def test_add_numbers_string(self):
        sum = arithmetic.add_numbers('Hello', 'python')
        self.assertEqual(sum, 'Hellopython')


if __name__ == '__main__':
    unittest.main()


