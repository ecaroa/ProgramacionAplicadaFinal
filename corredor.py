
class Corredor():

    def __init__(self, nroID, nombre, apellido, marca, sexo):
        # super().__init__()
        self.nroID = nroID
        self.nombre = nombre
        self.apellido = apellido
        self.marca = marca
        self.sexo = sexo

    def __str__(self):
        return "Nro : {}, Nombre: {}, Apellido: {}, Marca: {}, Sexo: {}".format(
            self.nroID, self.nombre, self.apellido, self.marca, self.sexo)

