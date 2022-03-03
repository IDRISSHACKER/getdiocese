# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class MesseApi:
    def __init__(self):
        self.db = bdd()

    def setMesse(self, id, element_id, intitule):
        try:
            self.db.save("INSERT INTO [GestDiocese].[dbo].[MESSES](id_m, cpt_el, int_m) VALUES(?,?,?)", [int(id), str(element_id), str(intitule)])
            return True
        except:
            return False

    def getMesses(self):
        try:
            return self.db.query("""SELECT id_m, intitule_e, int_m 
            FROM [GestDiocese].[dbo].[MESSES]
            INNER JOIN [GestDiocese].[dbo].[ELEMENTS]
            ON [GestDiocese].[dbo].[MESSES].[cpt_el] = [GestDiocese].[dbo].[ELEMENTS].[cpt_el]
            """)
        except Exception:
            print("erreur l'ors de la recuperation des messes")
            return []

    def getMesse(self, title):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[MESSES] WHERE [GestDiocese].[dbo].[MESSES].[int_m] = ?", [title])
        except Exception:
            print("erreur l'ors de la recuperation  de la messe")
            return []

    def updateMesse(self, key, new_element_id, newInt):
        try:
            return self.db.save(f"UPDATE [GestDiocese].[dbo].[MESSES]  SET [cpt_el] = ?, [int_m] = ? WHERE [id_m] = {key}", [new_element_id, newInt])
        except Exception:
            print("erreur l'ors de la mise à jours du service")
            return []

    def removeMesse(self, title):
        self.db.save("DELETE FROM [GestDiocese].[dbo].[MESSES] WHERE [GestDiocese].[dbo].[MESSES].[int_m] = ?",
                         [title])



if __name__ == "__main__":
    api = MesseApi()
    if api.setMesse(int("4567"), str("service"), int("45")):
        print("Save with success")

