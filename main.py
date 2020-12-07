from carrera import Carrera
from os import system, name

def main():

    MostrarMenu()
    opcion = int(input("Ingrese opcion: "))

    carrera = Carrera()

    while opcion != 10:

        if opcion == 1:
            clear()
            carrera.agregarParticipante()
            clear()

        if opcion == 2:
            clear()
            carrera.mostrarRegistros()


        MostrarMenu()
        opcion = int(input("Ingrese opción: "))


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def MostrarMenu():

    print("1.  Ingrese participante")
    print("2.  Mostrar registros")

if __name__ == "__main__":
    main()