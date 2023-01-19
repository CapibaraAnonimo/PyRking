class Plaza:
    def __init__(self, id_plaza, tipo, precio, ocupada, abonada):
        self._id = id_plaza
        self._tipo = tipo
        self._precio = precio
        self._ocupada = ocupada
        self._abonada = abonada

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, a):
        self._id = a

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, a):
        self._tipo = a

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, a):
        self._precio = a

    @property
    def ocupada(self):
        return self._ocupada

    @ocupada.setter
    def ocupada(self, a):
        self._ocupada = a

    @property
    def abonada(self):
        return self._abonada

    @abonada.setter
    def abonada(self, a):
        self._abonada = a

    def __str__(self):
        return str(self.id)
