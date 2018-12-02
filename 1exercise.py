# модули
import unittest


# функция
def Arithmetic(a, b, oper):

    if oper == '+':
        res = a + b
    elif oper == '-':
        res = a - b
    elif oper == '*':
        res = a * b
    elif oper == '/':
        res = a/b
    else:
        res = 'Неверная операция'
    return res


# тест-кейс
class ArithmeticFuncTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(Arithmetic(6, 2, '+'), 8)

    def test_diff(self):
        self.assertEqual(Arithmetic(6, 2, '-'), 4)

    def test_mult(self):
        self.assertEqual(Arithmetic(6, 2, '*'), 12)

    def test_div(self):
        self.assertEqual(Arithmetic(6, 2, '/'), 3)

    def test_unknown(self):
        self.assertEqual(Arithmetic(6, 2, '.'), "Неверная операция")


# обозначаем выполняемую задачу
if __name__ == '__main__':
    unittest.main()
