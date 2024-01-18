# Importamos las clases a utilizar
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creacion objeto cuadrado".center(50,"-"))
cuadrado = Cuadrado(5,"Rojo")

# La validacion ignora el valor erroneo
cuadrado.alto = 15

print(cuadrado.ancho)
print(cuadrado.alto)
print(cuadrado.color)
print(cuadrado.calcular_area())
print(cuadrado)
#print(cuadrado.__str__())

print("Creacion objeto rectangulo".center(50,"-"))
rectangulo = Rectangulo(ancho=3,alto=8,color="Blue")

# print(rectangulo.ancho)
# print(rectangulo.alto)
# print(rectangulo.color)
# print(rectangulo.calcular_area())
# print(rectangulo)
# print(rectangulo.__str__())


# MRO - Method Resolution Order
# Se imprime en pantalla el orden de ejecucion de clases
# print(Cuadrado.mro())