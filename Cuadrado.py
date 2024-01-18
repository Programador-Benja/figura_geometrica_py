from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color) -> None:
        #super().__init__(lado) es confuso usar esta sintaxis
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__(self) -> str:
        #return f"{super().__str__()}, Color: {self.color}, Area: {self.calcular_area()}"
        return f"{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}, Area: {self.calcular_area()}"
    def calcular_area(self):
        return self.alto * self.ancho
    