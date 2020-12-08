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
            carrera.guardarDatos()
            clear()

        if opcion == 2:
            clear()
            carrera.consultarDB()
        
        if opcion == 3:
            clear()
            carrera.mostrarPosicion()

        if opcion == 4:
            clear()
            carrera.mostrarUltimo()

        if opcion == 5:
            clear()
            carrera.mostrarCantidad()
        
        if opcion == 6:
            clear()
            carrera.mostrarPeor()


        MostrarMenu()
        opcion = int(input("Ingrese opción: "))


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def MostrarMenu():

    print("")
    print("1.  Ingrese participante")
    print("2.  Mostrar registros")
    print("3.  Mostrar posiciones")
    print("4.  Mostrar último")
    print("5.  Mostrar cuantos participaron")
    print("6.  Mostrar peor tiempo")
    print("7.  Guardar en CSV")

if __name__ == "__main__":
    main()