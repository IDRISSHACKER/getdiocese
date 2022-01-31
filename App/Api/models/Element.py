# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class ElementApi:
    def __init__(self):
        self.db = bdd()

    def setElement(self, id, ctgStructure, ctgElement, intitule, montant):
        try:
            self.db.save("INSERT INTO [GestDiocese].[dbo].[ELEMENTS]([ref_e], [code_cs], [code_ce], [intitule_e], [montant_e]) VALUES(?,?,?,?,?)", [id, ctgStructure, ctgElement, intitule, montant])
            return True
        except:
            print("err insert e")
            return False

    def getElements(self):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[ELEMENTS]")
        except Exception:
            print("erreur l'ors de la recuperation des elements")
            return []

    def getElement(self, title):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[ELEMENTS] WHERE [GestDiocese].[dbo].[ELEMENTS].[intitule_e] = ?", [title])
        except Exception:
            print("erreur l'ors de la recuperation  de l'element")
            return []

    def updateElement(self, key, newTitle, newMontant, newCtg):
        return self.db.save(f"UPDATE [GestDiocese].[dbo].[ELEMENTS]  SET [intitule_e] = '{newTitle}', [montant_e] = '{newMontant}', [code_ce] = '{newCtg}' WHERE [ref_e] = ?", [key])


    def removeElement(self, title):
        try:
            self.db.save("DELETE FROM [GestDiocese].[dbo].[ELEMENTS] WHERE [GestDiocese].[dbo].[ELEMENTS].[intitule_e] = ?",
                         [title])
            return True
        except:
            print("Erreur lors de la supression de l'element !")
            return False


if __name__ == "__main__":
    api = ElementApi()
    if api.setElement("4567", "2", "3", "4", "5"):
        print("Save with success")
