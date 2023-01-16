class Plaza:
    def __init__(self, id, tipo, precio, ocupada, abonada):
        self.id = id
        self.tipo = tipo
        self.precio = precio
        self.ocupada = ocupada
        self.abonada = abonada

    def __str__(self):
        return str(self.id)
