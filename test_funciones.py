import unittest 
from funciones import * 

class TestFunciones(unittest.TestCase):
    def test_crearMatriz_values(self):
        # Estudiar comportamiento cuando el tipo de valor
        # no corresponde con el flujo correcto
        self.assertRaises(TypeError, crearMatriz, -1)
        self.assertRaises(TypeError, crearMatriz, "matriz")
        self.assertRaises(TypeError, crearMatriz, True)

    
    def test_verificarRed(self):
        self.assertTrue(verificarRed)


    def test_auxSacarNombre(self):
        self.assertRaises(TypeError,auxSacarNombre, 5)
        self.assertRaises(TypeError,auxSacarNombre, [1,2,3,4])
        self.assertRaises(TypeError,auxSacarNombre, False)

