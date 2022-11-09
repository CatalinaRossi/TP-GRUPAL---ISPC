#Modulo de conexion, con desconexion automatica por defecto luego de operar.

import mysql.connector

class BDCon():
    def __init__(self):              
        print("\n")
    def Conectar(self):
        try:
            self.conexion = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = '199530Lr#',
            db = 'disqueria'
            )
            if self.conexion.is_connected():
                print("\n")

        except mysql.connector.Error as error:
            print(error)

    def Desconectar(self):                                      

        if self.conexion.is_connected():
            self.conexion.close()

    def Consulta(self,query):
        self.query = query
        if self.conexion.is_connected():
            try:
                self.cursor = self.conexion.cursor()
                self.cursor.execute(self.query)
                self.listado = self.cursor.fetchall()
                self.Desconectar()
                return self.listado
            except self.mysql.connector.Error as Error:
                print("No hay conexion",Error)

    
    def Commit(self,query,data): 
        self.query = query
        self.data = data
        if self.conexion.is_connected():
            try:
                self.cursor = self.conexion.cursor()
                self.cursor.execute(self.query,self.data)
                self.conexion.commit() #[!]
            except self.mysql.connector.Error as Error:
                print("No hay conexion",Error)
        self.Desconectar()
