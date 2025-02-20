import unittest
from script import abrir_bloc_notas 

class TestAutomatizacion(unittest.TestCase):
    def test_abrir_bloc_notas(self):
        """Verifica que la función se ejecuta sin errores."""
        try:
            abrir_bloc_notas()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado, "La automatización falló.")

if __name__ == '__main__':
    unittest.main()
