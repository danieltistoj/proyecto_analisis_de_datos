import pymysql
class BasedeDatos:
    def __init__(self):
        self.connection = pymysql.connect(
            host ='165.227.192.109',
            user ='analisis',
            password='1234',
            db = 'analisisdatos'
        )
        try:
            self.connection.autocommit(True)
            self.cursor = self.connection.cursor()
            print("conexion exitoso con mysql")
        except:
            print("valio verga la conexion")

    def get_consulta(self,consulta):
        try:
            self.cursor.execute(consulta)
            data = self.cursor.fetchall()
            for x in data:
                print(x)
        except:
            print("Error al hacer la consulta")
