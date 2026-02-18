import unittest
import calc


class testAdd(unittest.TestCase):
    def test_add(self):
        res = calc.add(10, 5)
        self.assertNotEqual(res, 18)


if __name__ == "__main__":
    unittest.main()
