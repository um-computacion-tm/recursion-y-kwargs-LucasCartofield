import unittest

def factorial(n):
    if n == 1:
        return 1
    resultado = n * factorial(n-1)
    return resultado

if __name__ == '__main__':
    unittest.main()