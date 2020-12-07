from corredor import Corredor

class Competencia (Corredor):
    
    def __init__(self, nroID, nombre, apellido, marca, sexo, *tiempos):
        Corredor.__init__(self, nroID, nombre, apellido, marca, sexo)
        self.tiempos = tiempos
        self.calcularMejortiempo()
        self.calcularPromedio()

    def mostrarTiempo(self):
        data = ""
        count = 1
        for dis in self.tiempos[0]:
            data = data + " tiempo {}: {}".format(count, dis)
            count += 1

        print("{} | {} | Mejor tiempo: {} | Promedio: {}".format(
            self, data, self.mejorTiempo, self.promedio))

    def calcularMejortiempo(self):

        mejorTiempo = self.tiempos[0][0]

        for dis in self.tiempos[0]:
            if (dis <= mejorTiempo):
                mejorTiempo = dis

        self.mejorTiempo = mejorTiempo

    def calcularPromedio(self):
        sum = 0.0
        for dis in self.tiempos[0]:
            sum = sum + dis

        self.promedio = sum/2
