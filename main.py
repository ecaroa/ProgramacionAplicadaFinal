

def main():

    MostrarMenu()
    opcion = int(input("Ingrese opcion: "))

    
    while opcion != 10:

        if opcion == 1:
            print("aca va la opcion 1")

        MostrarMenu()
        opcion = int(input("Ingrese opción: "))


def MostrarMenu():

    print("aca va el menu")

if __name__ == "__main__":
    main()