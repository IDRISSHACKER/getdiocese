# -*- coding: utf-8 -*-
from time import sleep

import pypyodbc as pyodbc
from PyQt5.QtCore import QObject, QThread, pyqtSignal


class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, server="IDRISS-HACKER", database="GestDiocese"):
        super(Worker, self).__init__()
        self.server = server
        self.database = database
        self.conn = ""
        self.status = 0

    def run(self):
        self.log()

    def test(self):
        return self.log()

    def start(self):
        return self.log()

    def log(self):
        DRIVER = "SQL Server"
        SERVER_NAME = self.server
        DATABASE_NAME = self.database

        self.conexionStr = f"""
            Driver={DRIVER};
            Server={SERVER_NAME};
            DATABASE_NAME={DATABASE_NAME};
            Trusted_Connection=yes
            """

        try:
            self.conn = pyodbc.connect(self.conexionStr, autocommit=True)
            self.status = 1
            # sleep(60)
            self.finished.emit()
            return 1

        except Exception as e:
            print()
            print("connexion terminée")
            self.status = 0
            # self.finished.emit()
            return 0


class bdd:
    def __init__(self):
        super(bdd, self).__init__()
        self.connect = 0
        self.status2 = 0
        self.runWorkers()

    def query(self, req, params=[]):
        if not self.worker.conn == "":
            cursor = self.worker.conn.cursor()
            return cursor.execute(req, params)
            cursor.close()
            self.status2 = 1
        else:
            cursor = pyodbc.connect(self.worker.conexionStr, autocommit=True).cursor()
            return cursor.execute(req, params)
            cursor.close()

    def save(self, req, params=[]):
        if self.worker.test():
            cursor = self.worker.conn.cursor()
            cursor.execute(req, params)

            cursor.close()

    def errMsg(self):
        return self.worker.status

    def runWorkers(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.endWorker)
        # Step 6: Start the thread
        self.thread.start()

    def endWorker(self):
        print("connected")
        self.connect = 1
        # self.thread.quit()


if __name__ == "__main__":
    bd = bdd()
    if bd.worker.test():
        bd.save("INSERT INTO [GestDiocese].[dbo].[ZONE](CODE_Z, INTITULE_Z) VALUES(?,?)",
                ["23564", "DIOCESE DE BAFANG"])
        print("Saving")

        datas = bd.query("SELECT * FROM [GestDiocese].[dbo].[ZONE]")
        for row in datas:
            print(row)
    else:
        print("er")
