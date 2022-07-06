import mysql.connector
class Employee():
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

    def employee(self):
        self.conection()
        queryselectall = "SELECT * FROM EMPLOYEE"
        self.cursor.execute(queryselectall)
        self.result = self.cursor.fetchall()
        self.cursor.close()
        self.conexion.close()
        return self.result

    def getName(self):
        self.conection()
        queryselecname = "SELECT NAME FROM EMPLOYEE"
        self.cursor.execute(queryselecname)
        self.result = self.cursor.fetchall()
        self.cursor.close()
        self.conexion.close()
        return self.result
llamado=Employee()
llamado.employee()