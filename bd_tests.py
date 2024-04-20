import unittest

from buscar_datos import buscar_datos, database

class TestInDatabase(unittest.TestCase):

    def test_persona1(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado, ["persona1"])
    
    def test_persona2(self):
        resultado = buscar_datos("Juan", "Carlos", "Perez", "Sanchez", **database)
        self.assertEqual(resultado, ["persona2"])
    
    def test_persona3(self):
        resultado = buscar_datos("Juan", "Pablo","Gonzalez","Diaz", **database)
        self.assertEqual(resultado, ["persona3"])
    
    def test_persona4(self):
        resultado = buscar_datos("Alejandro", "Lionel", "Romero", "Sosa", **database)
        self.assertEqual(resultado, ["persona4"])
    
    def test_personas_iguales(self):
        resultado = buscar_datos("Juan", **database)
        self.assertEqual(resultado, ["persona2","persona3"])

    def  test_datos_mezclados(self):      
        resultado = buscar_datos("Ruiz", "Pablo", "Picasso", "Diego", **database)
        self.assertEqual(resultado, ["persona1"])

    def  test_persona_no_existe(self):      
        resultado = buscar_datos("Ignacio", "Julian", "Soria", "Lopez", **database)
        self.assertEqual(resultado, "Los datos solicitados no se encuentran dentro de la base")

unittest.main()        