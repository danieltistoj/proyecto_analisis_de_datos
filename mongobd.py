import pymongo
class conexion:
    def __init__(self):
        self.mongo_host = "165.227.192.109"
        self.mongo_puerto = "27017"
        self.mongo_fuera = 1000
        self.mongo_uri = "mongodb://"+self.mongo_host+":"+self.mongo_puerto+"/"
        self.mongo_basedatos = "analisis"
        self.mongo_coleccion = "equipos"
        try:
            self.cliente = pymongo.MongoClient(self.mongo_uri,serverSelectionTimeoutMs=self.mongo_fuera)
            self.baseDatos = self.cliente[self.mongo_basedatos]
            self.coleccion = self.baseDatos[self.mongo_coleccion]
            print("coneccion exitosa con mongo")
        except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
            print("Tiempo exedido " + errorTiempo)
        except pymongo.errors.ConnectionFailure as errorConexion:
            print("Fallo al conectarse a mongodb " + errorConexion)

    def agregar_archivo(self,equipo,fecha_hora,informacion,fecha_hora_final):
        documento = {
            "equipo":equipo,
            "fecha_hora_inicial":fecha_hora,
            "fehca_hora_final":fecha_hora_final,
            "informacion":informacion
        }
        self.coleccion.insert(documento)