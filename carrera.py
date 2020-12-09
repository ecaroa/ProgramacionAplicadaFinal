
from competencia import Competencia
from datos import Datos
import db
from sqlalchemy import and_, or_



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


    def guardarDatos(self):
        print(f"""
                    ╔══════════════════════════╗
                    ║      GUARDAR EN BASE     ║
                    ╚══════════════════════════╝
                """)

        db.Base.metadata.create_all(db.engine)

        for corredor in self.listaTiempos:
            nroID = corredor.nroID
            nombre = corredor.nombre
            apellido = corredor.apellido
            marca = corredor.marca
            sexo = corredor.sexo
            primerVuelta = corredor.tiempos[0][0]
            segundoVuelta = corredor.tiempos[0][1]
            mejorVuelta = corredor.mejorTiempo
            promedio = corredor.promedio

            registro = Datos(nroID, nombre, apellido, marca, sexo,
                             primerVuelta, segundoVuelta, mejorVuelta, promedio)
            db.session.add(registro)
            db.session.commit()

        print(f"""
                    ╔══════════════════════════╗
                    ║   ...Datos Guardado      ║
                    ╚══════════════════════════╝
                """)


    def consultarDB(self):
        print(f"""
                    ╔══════════════════════════════╗
                    ║    MOSTRAR DATOS DE BASE     ║
                    ╚══════════════════════════════╝
                """)

        # SELECT * FROM datos;
        for d in db.session.query(Datos).all():
            print(d)

    def mostrarPosicion(self):
        print(f"""
                    ╔════════════════════════════╗
                    ║      MOSTRAR POSICION      ║
                    ╚════════════════════════════╝
                """)

        
        query_obj = db.session.query(Datos)
        order_by_query = query_obj.order_by(Datos.mejorVuelta)

        for result in order_by_query:
            print(result)
         

    def mostrarUltimo(self):
        print(f"""
                    ╔════════════════════════════╗
                    ║      MOSTRAR ULTIMO        ║
                    ╚════════════════════════════╝
                """)

        
        query_obj = db.session.query(Datos)
        order_by_query = query_obj.order_by(Datos.mejorVuelta.desc()).limit(1)

        for result in order_by_query:
            print(result)

    def mostrarCantidad(self):
        print(f"""
                    ╔══════════════════════════════╗
                    ║  MOSTRAR CANT PARTICIPANTES  ║
                    ╚══════════════════════════════╝
                """)


        d = db.session.query(Datos).count()
        print("Formaron parte de la competencia: ")
        print(d) 

    
    def mostrarPeor(self):
        print(f"""
                    ╔════════════════════════════╗
                    ║    MOSTRAR PEOR TIEMPO     ║
                    ╚════════════════════════════╝
                """)

        
        query_obj = db.session.query(Datos)
        order_by_query = query_obj.order_by(Datos.promedio.desc()).limit(1)


        for result in order_by_query:
            print(result)

    def crearCSV(self):
        
        archivo = input("Ingrese el nombre de salida para el CSV: ")
        datos = []
        for d in db.session.query(Datos).all():
            datos.append("\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\"\n"
                         .format(
                             d.nroID,
                             d.nombre,
                             d.apellido,
                             d.marca,
                             d.sexo,
                             d.primerVuelta,
                             d.segundoVuelta,
                             d.mejorVuelta,
                             d.promedio))

        with open(f"{archivo}.csv", 'w') as f:
            f.write("\"nroID\",\"nombre\",\"apellido\",\"marca\",\"sexo\",\"vuelta 1\",\"vuelta 2\",\"mejorVuelta\",\"promedio\"\n")
            for dd in datos:
                f.write(dd)

        print(f"""
                    ╔════════════════════════╗
                    ║       CSV GENERADO     ║
                    ╚════════════════════════╝
                """)
            
                