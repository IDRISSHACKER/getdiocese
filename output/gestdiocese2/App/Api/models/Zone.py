# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class ZoneApi:
    def __init__(self):
        self.db = bdd()

    def setZone(self, id, intitule):
        try:
            self.db.save("INSERT INTO [GestDiocese].[dbo].[ZONE](code_z, intitule_z) VALUES(?,?)", [id, intitule])
            return True
        except Exception:
            print(f"erreur lors de l'ajout {Exception}")
            return False

    def getZones(self):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[ZONE]")
        except Exception:
            print("erreur l'ors de la recuperation des zones")
            return []

    def getZone(self, title):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[ZONE] WHERE [GestDiocese].[dbo].[ZONE].[intitule_z] = ?", [title])
        except Exception:
            print("erreur l'ors de la recuperation  de la zone")
            return []

    def updateZone(self, key, newTitle):
        try:
            return self.db.save(f"UPDATE [GestDiocese].[dbo].[ZONE]  SET [intitule_z] = '{newTitle}' WHERE [code_z] = ?", [key])
        except Exception:
            print("erreur l'ors de la mise à jours  de la zone")
            return []

    def removeZone(self, title):
        try:
            self.db.save("DELETE FROM [GestDiocese].[dbo].[ZONE] WHERE [GestDiocese].[dbo].[ZONE].[intitule_z] = ?",
                         [title])
        except:
            print("Erreur lors de la supression !")


if __name__ == "__main__":
    api = ZoneApi()
    if api.setZone("4567", "intitule 45656"):
        print("Save with success")
