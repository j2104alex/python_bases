import unittest
import cambia_texto

'''Unittest es para analizar si el codigo funciona correctamente'''
class ProbarCambiaTexto(unittest.TestCase):
    #Es obligatorio que empiece por test la funcion
    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUEN DIA')


if __name__ == '__main__':
    unittest.main()
