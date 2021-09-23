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
            print("conexion exitosa con mongo")
        except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
            print("Tiempo exedido " + errorTiempo)
        except pymongo.errors.ConnectionFailure as errorConexion:
            print("Fallo al conectarse a mongodb " + errorConexion)

    def agregar_archivo(self,equipo,fecha_hora,informacion,fecha_hora_final,sub_proceso,info,CPU,memoria,swap,disco,red):
        documento = {
            "equipo":equipo,
            "Informacion Sistema" : info,
            "Informacion CPU" : CPU,
            "Informacion Memoria" : memoria,
            "SWAP": swap,
            "Disco Duro" : disco,
            "Redes" : red,
            "fecha_hora_inicial":fecha_hora,
            "fehca_hora_final":fecha_hora_final,
            "informacion":informacion,
            "ultimos_procesos":sub_proceso
        }
        self.coleccion.insert(documento)
    def agregacion(self):
        print("entro")
        query =  [{"$group":
                 {"_id": "$equipo",
                  "num_sesiones":
                      {"$sum": 1}
                  }
             }]


        resultado = self.coleccion.aggregate(query)
        ips  = [] #guarda las ips
        rep = [] #las veces que aparece cada ip
        for x in resultado:
           ips.append(x.get("_id"))
           rep.append(x.get("num_sesiones"))

        print(resultado)
        return ips,rep
