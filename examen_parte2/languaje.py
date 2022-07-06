import mysql.connector

class Languaje():
    def conection(self):
        try: 
            self.conexion = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Curso123",
                database = "empleados"
                )
            self.cursor = self.conexion.cursor()

        except Exception as e:
                print("Error al conectar con la base de datos")
                print(e)

    def getID(self):
        try:

            self.conection()
            queryselecId = "SELECT ID FROM LANGUAJE"
            self.cursor.execute(queryselecId)
            self.result = self.cursor.fetchall()
            self.cursor.close()
            self.conexion.close()
            return self.result
        except Exception as e:
            print(e)

    def getCode(self):
        try:

            self.conection()
            queryselecId = "SELECT CODIGO FROM LANGUAJE"
            self.cursor.execute(queryselecId)
            self.result = self.cursor.fetchall()
            self.cursor.close()
            self.conexion.close()
            return self.result
        except Exception as e:
            print(e)

    def getName(self):
        try: 
            self.conection()
            queryselecName = "SELECT NOMBRE FROM LANGUAJE"
            self.cursor.execute(queryselecName)
            self.result = self.cursor.fetchall()
            self.cursor.close()
            self.conexion.close()
            return self.result
        except Exception as e:
            print(e)