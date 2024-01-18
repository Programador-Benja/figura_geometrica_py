# Importamos las clases FiguraGeometrica y Color
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color) -> None:
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._alto * self.ancho
    
    def __str__(self) -> str:
        return f"{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}, Area: {self.calcular_area()}"