# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class CompteApi:
    def __init__(self):
        self.db = bdd()

    def getComptes(self):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[Compte]")
        except Exception:
            print("erreur l'ors de la recuperation des services")
            return []

    def getService(self, title):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[SERVICES] WHERE [GestDiocese].[dbo].[SERVICES].[intitule_s] = ?", [title])
        except Exception:
            print("erreur l'ors de la recuperation  du service")
            return []

    def updateService(self, key, newTitle):
        try:
            return self.db.save(f"UPDATE [GestDiocese].[dbo].[SERVICES]  SET [intitule_s] = '{newTitle}' WHERE [code_s] = ?", [key])
        except Exception:
            print("erreur l'ors de la mise à jours  du service")
            return []

    def removeService(self, title):
        try:
            self.db.save("DELETE FROM [GestDiocese].[dbo].[SERVICES] WHERE [GestDiocese].[dbo].[SERVICES].[intitule_s] = ?",
                         [title])
        except:
            print("Erreur lors de la supression !")


if __name__ == "__main__":
    api = ServiceApi()
    if api.setService("4567", "service"):
        print("Save with success")

