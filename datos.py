import db
from sqlalchemy import Column, Integer, String, Float


class Datos(db.Base):

    __tablename__ = "participantes"

    id = Column(Integer, primary_key=True)
    nroID = Column(Integer, nullable=False)
    nombre = Column(String(15), nullable=False)
    apellido = Column(String(15), nullable=False)
    marca = Column(String(2), nullable=False)
    sexo = Column(String(1), nullable=False)
    primerVuelta = Column(Integer, nullable=False)
    segundoVuelta = Column(Integer, nullable=False)
    mejorVuelta = Column(Integer, nullable=True)
    promedio = Column(Float, nullable=True)

    def __init__(self,
                 nroID,
                 nombre,
                 apellido,
                 marca,
                 sexo,
                 primerVuelta,
                 segundoVuelta,
                 mejorVuelta,
                 promedio):
        self.nroID = nroID
        self.nombre = nombre
        self.apellido = apellido
        self.marca = marca
        self.sexo = sexo
        self.primerVuelta = primerVuelta
        self.segundoVuelta = segundoVuelta
        self.mejorVuelta = mejorVuelta
        self.promedio = promedio

    def __str__(self):
        return (
            f"""
            -------------------------------------------------------
            id: {self.id},
            Nro Participante: {self.nroID}
            Nombre: {self.nombre}
            Apellido: {self.apellido}
            Marca: {self.marca}
            sexo: {self.sexo}
            Vuelta 1: {self.primerVuelta}
            Vuelta 2: {self.segundoVuelta}
            Mejor vuelta: {self.mejorVuelta}
            Promedio disparos: {self.promedio}
            -------------------------------------------------------
            """
        )
