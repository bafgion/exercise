import unittest


def square(arg):
    S = arg*arg
    P = 4*arg
    D = arg*1.414
    return S, P, round(D, 2)


class SquareTestFunc(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(5), (25, 20, 7.07))

if __name__ == '__main__':
    unittest.main()
