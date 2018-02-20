import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout('AAABBCD'), 210)

        self.assertEqual(checkout('AAAABBC'), 245)

        self.assertEqual(checkout('E'), -1)

        self.assertEqual(checkout('CCC'), 60)

if __name__ == '__main__':
    unittest.main()
