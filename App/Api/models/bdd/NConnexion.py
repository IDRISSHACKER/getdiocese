# -*- coding: utf-8 -*-
import pypyodbc as pyodbc

class bdd:
    def __init__(self, server="IDRISS-HACKER", database="GestDiocese"):
        self.server = server
        self.database = database
        self.conn = ""
        self.status = 0
        self.log()

    def log(self):
        DRIVER = "SQL Server"
        SERVER_NAME = self.server
        DATABASE_NAME = self.database

        conexionStr = f"""
            Driver={DRIVER};
            Server={SERVER_NAME};
            DATABASE_NAME={DATABASE_NAME};
            Trusted_Connection=yes
            """

        try:
            self.conn = pyodbc.connect(conexionStr, autocommit=True)
            self.status = 1
            return 1

        except Exception as e:
            print()
            print("connexion terminée")
            self.status = 0
            return 0

    def query(self, req, params=[]):
        if self.test():
            cursor = self.conn.cursor()
            return cursor.execute(req, params)
            cursor.close()

    def save(self, req, params=[]):
        if self.test():
            cursor = self.conn.cursor()
            cursor.execute(req, params)

            cursor.close()

    def test(self):
        return self.status

    def errMsg(self):
        return self.status


if __name__ == "__main__":
    bd = bdd()
    if bd.test():
        bd.save("INSERT INTO [GestDiocese].[dbo].[ZONE](CODE_Z, INTITULE_Z) VALUES(?,?)", ["99999999", "DIOCESE DE BAFANG"])
        print("Saving")

        datas = bd.query("SELECT * FROM [GestDiocese].[dbo].[ZONE]")
        for row in datas:
            print(row)

