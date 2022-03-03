# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class TauxApi:
    def __init__(self):
        self.db = bdd()

    def setTaux(self, id, id_part, id_c, v_taux):
        try:
            self.db.save("INSERT INTO [GestDiocese].[dbo].[TAUX]([id], [id_part], [id_c], [v_taux]) VALUES(?,?,?,?)", [int(id), int(id_part), int(id_c), int(v_taux)])
            return True
        except:
            return False

    def getTaux(self):
        try:
            return self.db.query("""SELECT id, int_part, int_casuel, v_taux 
            FROM [GestDiocese].[dbo].[TAUX]
            INNER JOIN [GestDiocese].[dbo].[PARTICIPATION2]
            ON [GestDiocese].[dbo].[PARTICIPATION2].[id_part] = [GestDiocese].[dbo].[TAUX].[id_part]
            INNER JOIN [GestDiocese].[dbo].[CASUELS]
            ON [GestDiocese].[dbo].[CASUELS].[id_c] = [GestDiocese].[dbo].[TAUX].[id_c]""")
        except Exception:
            print("erreur l'ors de la recuperation des taux""")
            return []


    def removeTaux(self, id):
        try:
            self.db.save("DELETE FROM [GestDiocese].[dbo].[TAUX] WHERE [GestDiocese].[dbo].[TAUX].[id] = ?",
                         [id])
            return True
        except:
            print("Erreur lors de la supression du tau !")
            return False

