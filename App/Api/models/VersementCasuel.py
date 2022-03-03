# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class VersementApi:
    def __init__(self):
        self.db = bdd()

    def setVersement(self, id, structure, casuel, montant, date, mois):
        try:
            self.db.save("INSERT INTO [GestDiocese].[dbo].[VERSEMENTS_C](id_vc, code_st, id_c, montant_vc, date_vc, mois_vc) VALUES(?, ?, ?, ?, ?, ?)", [int(id), str(structure), str(casuel), int(montant), str(date), str(mois)])
            return True
        except:
            return False
    def getVersements(self):
        try:
            return self.db.query("""SELECT id_vc, nom_st, int_casuel, montant_vc, date_vc, mois_vc 
            FROM [GestDiocese].[dbo].[VERSEMENTS_C]
            INNER JOIN [GestDiocese].[dbo].[STRUCTURES]
            ON [GestDiocese].[dbo].[VERSEMENTS_C].[code_st] = [GestDiocese].[dbo].[STRUCTURES].[code_st]
            INNER JOIN [GestDiocese].[dbo].[CASUELS]
            ON [GestDiocese].[dbo].[VERSEMENTS_C].[id_c] = [GestDiocese].[dbo].[CASUELS].[id_c]
            """)
        except Exception:
            print("erreur l'ors de la recuperation des versements")
            return []

    def getVersement(self, title):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[VERSEMENTS_C] WHERE [GestDiocese].[dbo].[VERSEMENTS_C].[id_vc] = ?", [int(title)])
        except Exception:
            print("erreur l'ors de la recuperation  du versement")
            return []

    def updateVersement(self, key, structure, casuel, montant, date, mois):
        try:
            return self.db.save(f"UPDATE [GestDiocese].[dbo].[VERSEMENTS_C]  SET [code_st] = ?, [id_c] = ?, [montant_vc] = ?, [date_vc] = ?, [mois_vc] = ? WHERE [id_vc] = {key}", [str(structure), str(casuel), int(montant), str(date), str(mois)])
        except Exception:
            print("erreur l'ors de la mise à jours  du versement")
            return []

    def removeVersement(self, title):
        try:
            self.db.save("DELETE FROM [GestDiocese].[dbo].[VERSEMENTS_C] WHERE [GestDiocese].[dbo].[VERSEMENTS_C].[id_vc] = ?",
                         [int(title)])
        except:
            print("Erreur lors de la supression !")


if __name__ == "__main__":
    api = VersementApi()
    if api.setVersement("4567", "intitule 45656"):
        print("Save with success")
