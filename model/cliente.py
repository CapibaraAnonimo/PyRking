class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self._dni = dni
        self._nombre = nombre
        self._apellidos = apellidos

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, a):
        self._dni = a

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, a):
        self._nombre = a

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, a):
        self._apellidos = a

    def modificar(self, nombre, apellidos, *args, **kwargs):  # TODO comprobar que puedo usar el Liskov substitution principle
        if nombre != '':
            self.nombre = nombre
        if apellidos != '':
            self.apellidos = apellidos
