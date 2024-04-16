import unittest

from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_con_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado, 0)
    
    def test_con_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)
    
    def test_con_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)
    
    def test_con_3(self):
        resultado = fibonacci(3)
        self.assertEqual(resultado, 2)
    
    def test_con_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)
    
    def test_con_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado, 8)

    def test_con_10(self):
        resultado = fibonacci(10)
        self.assertEqual(resultado, 55)

    def test_con_13(self):
        resultado = fibonacci(13)
        self.assertEqual(resultado, 233)        

unittest.main()