import unittest
import liczbyPierwsze

class TestPrimeFunction(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(liczbyPierwsze.check_prime('7'), 'jest liczbą pierwszą')
        self.assertEqual(liczbyPierwsze.check_prime('13'), 'jest liczbą pierwszą')
        self.assertEqual(liczbyPierwsze.check_prime('4'), 'nie jest')

    def test_decimal_numbers(self):
        self.assertEqual(liczbyPierwsze.check_prime('3.14'), 'nie jest liczbą pierwszą')

if __name__ == '__main__':
    unittest.main()
