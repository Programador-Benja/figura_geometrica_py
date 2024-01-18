class Color:
    def __init__(self, color) -> None:
        # Encapsulamos el atributo _color
        self._color = color

    # Metodos getter and setter de color
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
        
    # Mostrar en pantalla los detalles
    def __str__(self) -> str:
        return f"Color: {self._color}"