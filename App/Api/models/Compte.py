# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class CompteApi:
    def __init__(self):
        self.db = bdd()

    def setCompte(self, id, structure, montant):
        try:
            self.db.save("INSERT INTO [GestDiocese].[dbo].[COMPTE](num_cpt, code_st, solde_cpt) VALUES(?,?,?)", [id, structure, montant])
            return True
        except Exception:
            print(f"erreur lors de l'ajout {Exception}")
            return False

    def getComptes(self):
        try:
            return self.db.query("""SELECT num_cpt, nom_st, solde_cpt 
            FROM [GestDiocese].[dbo].[Compte]
            INNER JOIN [GestDiocese].[dbo].[STRUCTURES]
            ON [GestDiocese].[dbo].[Compte].[code_st] = [GestDiocese].[dbo].[STRUCTURES].[code_st]

            """)
        except Exception:
            print("erreur l'ors de la recuperation des COMPTE")
            return []

    def getCompte(self, title):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[COMPTE] WHERE [GestDiocese].[dbo].[COMPTE].[num_cpt] = ?", [title])
        except Exception:
            print("erreur l'ors de la recuperation  du service")
            return []

    def updateCompte(self, key,  structure, montant):
        try:
            return self.db.save(f"UPDATE [GestDiocese].[dbo].[COMPTE]  SET [code_st] = ?, [solde_cpt] = ? WHERE [num_cpt] = {key}", [structure, montant])
        except Exception:
            print("erreur l'ors de la mise à jours  du service")
            return []

    def removeCompte(self, title):
        try:
            self.db.save("DELETE FROM [GestDiocese].[dbo].[COMPTE] WHERE [GestDiocese].[dbo].[COMPTE].[num_cpt] = ?",
                         [title])
        except:
            print("Erreur lors de la supression !")


if __name__ == "__main__":
    api = CompteApi()
    if api.setService("4567", "service"):
        print("Save with success")

