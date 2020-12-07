
from competencia import Competencia


class Carrera():

    def __init__(self):
        self.listaTiempos = []

    def agregarParticipante(self):
        nroID = 0

        while nroID != 999:

            print(f"""

                ╔════════════════════════════════╗
                ║  INGRESO PARTICIPANTE (｡◕‿◕｡)  ║
                ╚════════════════════════════════╝
            """)

            nroID = int(input("Ingrese NUMERO PARTICIPANTE: \t"))
            if nroID == 999:
                break
            nombre = input("Ingrese NOMBRE: \t\t")
            apellido = input("Ingrese APELLIDO: \t\t")
            marca = input("Ingrese MARCA: \t\t\t")
            sexo = input("Ingrese SEXO (F/M): \t\t").upper()
            print("\n")

            cantVueltas = 0

            vueltas = []
            print("***** VUELTAS *****\n")
            while cantVueltas < 2:
                print("Vuelta " + str(cantVueltas+1) + " : ")
                t = int(input("Ingrese Tiempo: "))
                print("\n")
                vueltas.append(t)
                cantVueltas += 1

            self.listaTiempos.append(
                Competencia(nroID, nombre, apellido, marca, sexo, vueltas))


    def mostrarRegistros(self):
        print("\n")
        print(f"""
                ╔═══════════════════════════════════╗
                ║  LISTADO DE PARTICIPANTE (｡◕‿◕｡)  ║
                ╚═══════════════════════════════════╝
            """)

        for d in self.listaTiempos:
            d.mostrarTiempo()
        print("\n")
