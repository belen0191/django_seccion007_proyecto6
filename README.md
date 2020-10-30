# django_seccion007_proyecto6
<h1> Informe de Test Pruebas <h1>

<title>lavado de autos</title>

nosotros como equipo "Locos  del Software" as GrupoN°1

a) Test 1 chequeo de maquina de pruebas

codigo:
class TestUno(unittest.TestCase):
    def test_igualdad_cadenas(self):
        self.assertEqual('ii','ii')

    def test_texto_mayuscula(self):
        self.assertEqual('ii'.upper(),'II')

    def test_no_esta_el_contenido(self):
        self.assertFalse('hola' in 'es un HOLA mundo')

        

if __name__ == "__main__":
    unittest.main()
    
 b) Test 2 grabar y listar mision y vision dentro de la base de datos
 
 codigo:
 
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


c)  Test 3 grabar y listar insumos dentro de la base de datos

codigo:

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

d)  Test 4 grabar y listar imagenes de la galeria dentro de la base de datos

codigo:

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
