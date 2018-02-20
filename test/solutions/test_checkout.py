import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout('AAABBCD'), 210)

        self.assertEqual(checkout('AAAABBC'), 245)

        self.assertEqual(checkout('Z'), -1)

        self.assertEqual(checkout('CCC'), 60)

    def test_E_discount(self):
        self.assertEqual(checkout('AAABBBCDEE'), 290)
        self.assertEqual(checkout('AAABBCDEE'), 275)
        self.assertEqual(checkout('EEB'), 80)
        self.assertEqual(checkout('EEEB'), 120)
        self.assertEqual(checkout('EEEEBB'), 160)

    def test_A_new_discount(self):
        self.assertEqual(checkout('AAAA'), 180)
        self.assertEqual(checkout('AAAAA'), 200)
        self.assertEqual(checkout('AAAAAA'), 250)
        self.assertEqual(checkout('AAAAAAA'), 300)
        self.assertEqual(checkout('AAAAAAAA'), 330)
        self.assertEqual(checkout('AAAAAAAAA'), 380)
        self.assertEqual(checkout('AAAAAAAAAA'), 400)

if __name__ == '__main__':
    unittest.main()
