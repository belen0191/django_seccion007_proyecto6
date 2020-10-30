from django.test import TestCase
import unittest
from .models import MisionyVision,Insumos,ImagenGaleria
# Create your tests here.


class TestUno(unittest.TestCase):
    def test_igualdad_cadenas(self):
        self.assertEqual('ii','ii')

    def test_texto_mayuscula(self):
        self.assertEqual('ii'.upper(),'II')

    def test_no_esta_el_contenido(self):
        self.assertFalse('hola' in 'es un HOLA mundo')

        

if __name__ == "__main__":
    unittest.main()

class TestDos(unittest.TestCase):
    def grabar_mision_vision(self):
        m = MisionyVision(
            ident="unico",mision="nuestra mision...",vision="nuestra vision es.."
        )
        valor = 0
        try:
            m.save()
            valor = 1
        except:
            valor = 0
            self.assertEqual(valor,1)
        
    def listar_mision_vision(self):
        lm = MisionyVision.objects.all()
        self.assertIsInstance(lm,MisionyVision)
    
if __name__ == "__main__":
    unittest.main()

class TestTres(unittest.TestCase):
    def grabar_insumo(self):
        i = Insumos(nombre="shampoo",precio="9990",descripcion="es el ....",stock="0"
        )
        valor = 0
        try:
            i.save()
            valor = 1
        except:
            valor = 0
            self.assertEqual(valor,1)
        
    def listar_insumo(self):
        li = Insumos.objects.all()
        self.assertIsInstance(li,Insumos)
    
if __name__ == "__main__":
    unittest.main()

class TestCuatro(unittest.TestCase):
    def grabar_imagen_galeria(self):
        g = ImagenGaleria(ident="4",imagen="ImagenGaleria"
        )
        valor = 0
        try:
            g.save()
            valor = 1
        except:
            valor = 0
            self.assertEqual(valor,1)
        
    def listar_imagen_galeria(self):
        lg = ImagenGaleria.objects.all()
        self.assertIsInstance(lg,ImagenGaleria)
    
if __name__ == "__main__":
    unittest.main()


        