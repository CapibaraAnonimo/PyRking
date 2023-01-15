class Plaza:
    def __init__(self, id, tipo, precio, ocupada):
        self.id = id
        self.tipo = tipo
        self.precio = precio
        self.ocupada = ocupada

    def __str__(self):
        return str(self.id)
