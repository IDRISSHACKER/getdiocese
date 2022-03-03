# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class ElementApi:
    def __init__(self):
        self.db = bdd()

    def setElement(self, id, ctgStructure, ctgElement, intitule, montant, ref):
        try:
            self.db.save("INSERT INTO [GestDiocese].[dbo].[ELEMENTS]([cpt_el], [code_cs], [code_ce], [intitule_e], [montant_e], [ref_e]) VALUES(?,?,?,?,?,?)", [int(id), str(ctgStructure), str(ctgElement), str(intitule), int(montant), str(ref)])
            return True
        except:
            return False

    def getElements(self):
        try:
            return self.db.query("""SELECT [cpt_el], [intitule_cs], [intitule_ce], [ref_e], [intitule_e], [montant_e] 
            FROM [GestDiocese].[dbo].[ELEMENTS] 
            INNER JOIN [GestDiocese].[dbo].[CATEGORIE_STRUCT]
            ON [GestDiocese].[dbo].[ELEMENTS].[code_cs] = [GestDiocese].[dbo].[CATEGORIE_STRUCT].[code_cs] 
            INNER JOIN [GestDiocese].[dbo].[CATEGORIE_E] 
            ON [GestDiocese].[dbo].[ELEMENTS].[code_ce] = [GestDiocese].[dbo].[CATEGORIE_E].[code_ce]""")
        except Exception:
            print("erreur l'ors de la recuperation des elements""")
            return []

    def getElement(self, title):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[ELEMENTS] WHERE [GestDiocese].[dbo].[ELEMENTS].[intitule_e] = ?", [title])
        except Exception:
            print("erreur l'ors de la recuperation  de l'element")
            return []

    def updateElement(self, key, ctgStructure, ctgElement, intitule, montant, ref):
        return self.db.save(f"UPDATE [GestDiocese].[dbo].[ELEMENTS]  SET [code_cs] = ?, [code_ce] = ?, [intitule_e] = ?, [montant_e] = ?, [ref_e] = ? WHERE [cpt_el] = {key}", [str(ctgStructure), str(ctgElement), str(intitule), int(montant), str(ref)])


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
