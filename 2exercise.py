import unittest


def is_year_leap(arg):
    if arg % 400 == 0:
        return True
    if arg % 4 == 0 and arg % 100 != 0:
        return True
    return False


class YearFuncTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_year_leap(400))

    def test_false(self):
        self.assertFalse(is_year_leap(401))


if __name__ == '__main__':
    unittest.main()
