# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class CategorieApi:
    def __init__(self):
        self.db = bdd()

    def setCategorie(self, id, intitule):
        try:
            self.db.save("INSERT INTO [GestDiocese].[dbo].[CATEGORIE_E](code_ce, intitule_ce) VALUES(?,?)", [id, intitule])
            return True
        except Exception:
            print(f"erreur lors de l'ajout {Exception}")
            return False

    def getCategories(self):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[CATEGORIE_E]")
        except Exception:
            print("erreur l'ors de la recuperation des categories")
            return []

    def getCategorie(self, title):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[CATEGORIE_E] WHERE [GestDiocese].[dbo].[CATEGORIE_E].[intitule_ce] = ?", [title])
        except Exception:
            print("erreur l'ors de la recuperation  de la categorie")
            return []

    def updateCategorie(self, key, newTitle):
        try:
            return self.db.save(f"UPDATE [GestDiocese].[dbo].[CATEGORIE_E]  SET [intitule_ce] = '{newTitle}' WHERE [code_ce] = ?", [key])
        except Exception:
            print("erreur l'ors de la mise à jours  de la categorie")
            return []

    def removeCategorie(self, title):
        try:
            self.db.save("DELETE FROM [GestDiocese].[dbo].[CATEGORIE_E] WHERE [GestDiocese].[dbo].[CATEGORIE_E].[intitule_ce] = ?",
                         [title])
        except:
            print("Erreur lors de la supression !")


if __name__ == "__main__":
    api = CategorieApi()
    if api.setService("4567", "service"):
        print("Save with success")

