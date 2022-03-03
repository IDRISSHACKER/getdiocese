# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class CasuelApi:
    def __init__(self):
        self.db = bdd()

    def setCasuel(self, id, cpt_el, int_casuel, mt_casuel):
        try:
            self.db.save("INSERT INTO [GestDiocese].[dbo].[CASUELS](id_c, cpt_el, int_casuel, mt_casuel) VALUES(?,?,?,?)", [int(id), str(cpt_el), str(int_casuel), int(mt_casuel)])
            return True
        except:
            return False

    def getCasuels(self):
        try:
            return self.db.query("SELECT id_c, intitule_e, int_casuel, mt_casuel FROM [GestDiocese].[dbo].[CASUELS] INNER JOIN [GestDiocese].[dbo].[ELEMENTS] ON [GestDiocese].[dbo].[CASUELS].[cpt_el] = [GestDiocese].[dbo].[ELEMENTS].[cpt_el]")
        except Exception:
            print("erreur l'ors de la recuperation des casuels")
            return []

    def getCasuel(self, title):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[CASUELS] WHERE [int_casuel] = ?", [title])
        except Exception:
            print("erreur l'ors de la recuperation  du casuel")
            return []

    def updateCasuel(self, key, cpt_el, int_casuel, mt_casuel):
        try:
            return self.db.save(f"UPDATE [GestDiocese].[dbo].[CASUELS]  SET [cpt_el] = ?, [int_casuel] = ?, [mt_casuel] = ? WHERE [id_c] = {key}", [cpt_el, int_casuel, mt_casuel])
        except Exception:
            print("erreur l'ors de la mise à jours du service")
            return []

    def removeCasuel(self, title):
        self.db.save("DELETE FROM [GestDiocese].[dbo].[CASUELS] WHERE [GestDiocese].[dbo].[CASUELS].[int_casuel] = ?",
                         [title])



if __name__ == "__main__":
    api = CasuelApi()
    if api.setCasuel(int("4567"), str("service"), int("45")):
        print("Save with success")

