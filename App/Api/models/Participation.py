# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class ParticipationApi:
    def __init__(self):
        self.db = bdd()

    def setParticipation(self, id, intitule, taux):
        try:
            self.db.save("INSERT INTO [GestDiocese].[dbo].[PARTICIPATION2](id_part, int_part, taux_part) VALUES(?,?,?)", [int(id), str(intitule), int(taux)])
            return True
        except Exception:
            print(f"erreur lors de l'ajout de la participation")
            return False

    def getParticipations(self):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[PARTICIPATION2]")
        except Exception:
            print("erreur l'ors de la recuperation des participation")
            return []

    def getParticipation(self, title):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[PARTICIPATION2] WHERE [GestDiocese].[dbo].[PARTICIPATION2].[int_part] = ?", [title])
        except Exception:
            print("erreur l'ors de la recuperation  du service")
            return []

    def updateParticipation(self, key, newInt, newTaux):
        try:
            return self.db.save(f"UPDATE [GestDiocese].[dbo].[PARTICIPATION2]  SET [int_part] = ?, [taux_part] = ? WHERE [id_part] = {key}", [newInt, newTaux])
        except Exception:
            print("erreur l'ors de la mise à jours  du service")
            return []

    def removeParticipation(self, title):
        print(title)
        print(len(title))
        self.db.save("DELETE FROM [GestDiocese].[dbo].[PARTICIPATION2] WHERE [GestDiocese].[dbo].[PARTICIPATION2].[int_part] = ?",
                         [title])



if __name__ == "__main__":
    api = ParticipationApi()
    if api.setParticipation(int("4567"), str("service"), int("45")):
        print("Save with success")

