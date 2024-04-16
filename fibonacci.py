import unittest

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    resultado = fibonacci(n-1) + fibonacci(n-2)
    return resultado

if __name__ == '__main__':
    unittest.main()