from abc import ABC, abstractmethod #Importacion para clases abstractas
class Triangulo(): #Declaracion de la clase principal triangulo
 def __init__(self, Angulo1, Angulo2, Angulo3, Lado1, Lado2, Lado3): #Constructor del objeto Triangulo
  self.Angulo1=Angulo1
  self.Angulo2 = Angulo2
  self.Angulo3 = Angulo3
  self.Lado1 = Lado1
  self.Lado2 = Lado2
  self.Lado3 = Lado3

 def verificar_angulos(self, Angulo1, Angulo2, Angulo3):
  Suma = Angulo1 + Angulo2 + Angulo3
  if (Suma == 180):
   print('True')
  else:
   print('False')

 def Mi_Triangulo(self, Angulo1, Angulo2, Angulo3):
  Suma = Angulo1 + Angulo2 + Angulo3
  if (Suma == 180):
   print('Sus angulos suman 180°')
  else:
   print('Sus angulos no suman 180°')

class Isoceles(Triangulo):
 def __init__(self, Angulo1, Angulo2, Angulo3, Lado1, Lado2, Lado3):
  Triangulo.__init__(self, Angulo1, Angulo2, Angulo3, Lado1, Lado2, Lado3)
 
 def Validad_Triangulo(self, Angulo1, Angulo2, Angulo3):
  if Lado1 == Lado2 or Lado1 == Lado3 or Lado2 == Lado3:
    print('El triangulo es Isoceles')
  
class Equilatero(Triangulo):
 def __init__(self, Angulo1, Angulo2, Angulo3, Lado1, Lado2, Lado3):
  Triangulo.__init__(self, Angulo1, Angulo2, Angulo3, Lado1, Lado2, Lado3)
 
 def Validad_Triangulo(self, Angulo1, Angulo2, Angulo3):
  if Lado1 == Lado2 and Lado1 == Lado3:
    print('El triangulo es equilatero')

class Escaleno(Triangulo):
 def __init__(self, Angulo1, Angulo2, Angulo3, Lado1, Lado2, Lado3):
  Triangulo.__init__(self, Angulo1, Angulo2, Angulo3, Lado1, Lado2, Lado3)

 def Validad_Triangulo(self, Angulo1, Angulo2, Angulo3):
  if Lado1 != Lado2 and Lado1 != Lado3 and Lado2 != Lado3:
    print('El triangulo es escaleno')

if __name__ == '__main__':

 numero_de_lados = 3

 Angulo1 = int(input('Declare el angulo 1: '))
 Angulo2 = int(input('Declare el angulo 2: '))
 Angulo3 = int(input('Declare el angulo 3: '))

 Lado1 = int(input('Declare longitud de lado 1: '))
 Lado2 = int(input('Declare longitud de lado 2: '))
 Lado3 = int(input('Declare longitud de lado 3: '))
 
 Figura = Triangulo(Angulo1, Angulo2, Angulo3, Lado1, Lado2, Lado3)
 Figura.verificar_angulos(Angulo1, Angulo2, Angulo3)

 Figura2 = Triangulo(Angulo1, Angulo2, Angulo3, Lado1, Lado2, Lado3)
 Figura2.Mi_Triangulo(Angulo1, Angulo2, Angulo3)

 TipoFigura1 = Isoceles(Angulo1, Angulo2, Angulo3, Lado1, Lado2, Lado3)
 TipoFigura1.Validad_Triangulo(Angulo1, Angulo2, Angulo3)
 
 TipoFigura2 = Equilatero(Angulo1, Angulo2, Angulo3, Lado1, Lado2, Lado3)
 TipoFigura2.Validad_Triangulo(Angulo1, Angulo2, Angulo3)
 
 TipoFigura3 = Escaleno(Angulo1, Angulo2, Angulo3, Lado1, Lado2, Lado3)
 TipoFigura3.Validad_Triangulo(Angulo1, Angulo2, Angulo3)


