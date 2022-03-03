# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class VersementApi:
    def __init__(self):
        self.db = bdd()

    def setVersement(self, id, compte, montant, date, mois):
        try:
            self.db.save("INSERT INTO [GestDiocese].[dbo].[VERSEMENTS](id_v, num_cpt, montant_v, date_v, mois_v) VALUES(?,?,?,?,?)", [int(id), int(compte), int(montant), str(date), str(mois)])
            return True
        except:
            return False

    def getVersements(self):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[VERSEMENTS]")
        except Exception:
            print("erreur l'ors de la recuperation des versements")
            return []

    def getVersement(self, title):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[VERSEMENTS] WHERE [GestDiocese].[dbo].[VERSEMENTS].[id_v] = ?", [int(title)])
        except Exception:
            print("erreur l'ors de la recuperation  du versement")
            return []

    def updateVersement(self, key, compte, montant, date, mois):
        try:
            return self.db.save(f"UPDATE [GestDiocese].[dbo].[VERSEMENTS]  SET [num_cpt] = ?, [montant_v] = ?, [date_v] = ?, [mois_v] = ? WHERE [id_v] = {key}", [int(compte), int(montant), str(date), str(mois)])
        except Exception:
            print("erreur l'ors de la mise à jours  du versement")
            return []

    def removeVersement(self, title):
        try:
            self.db.save("DELETE FROM [GestDiocese].[dbo].[VERSEMENTS] WHERE [GestDiocese].[dbo].[VERSEMENTS].[id_v] = ?",
                         [int(title)])
        except:
            print("Erreur lors de la supression !")


if __name__ == "__main__":
    api = VersementApi()
    if api.setVersement("4567", "intitule 45656"):
        print("Save with success")
