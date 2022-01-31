# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class StructureApi:
    def __init__(self):
        self.db = bdd()

    def setStructure(self, code_st, code_cs, code_z, code_s, nom_st, chef_st):
        self.db.save("INSERT INTO [GestDiocese].[dbo].[STRUCTURES](code_st, code_cs, code_z, code_s, nom_st, chef_st) VALUES(?,?,?,?,?,?)", [code_st, code_cs, code_z, code_s, nom_st, chef_st])


    def getStructures(self):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[STRUCTURES]")
        except Exception:
            print("erreur l'ors de la recuperation des Structures")
            return []

    def getStructure(self, title):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[STRUCTURES] WHERE [GestDiocese].[dbo].[STRUCTURES].[nom_st] = ?", [title])
        except Exception:
            print("erreur l'ors de la recuperation  de la structure")
            return []

    def updateStructure(self, code_st, code_cs, code_z, code_s, nom_st, chef_st):
        return self.db.save(f"UPDATE [GestDiocese].[dbo].[STRUCTURES]  SET [code_cs] = '{code_cs}', [code_z] = '{code_z}', [code_s]='{code_s}', [nom_st] = '{nom_st}', [chef_st] = '{chef_st}'  WHERE [code_st] = ?", [code_st])

    def removeStructure(self, title):
        try:
            self.db.save("DELETE FROM [GestDiocese].[dbo].[STRUCTURES] WHERE [GestDiocese].[dbo].[STRUCTURES].[nom_st] = ?",
                         [title])
        except:
            print("Erreur lors de la supression !")


if __name__ == "__main__":
    api = StructureApi()
    if api.setStructure():
        print("Save with success")
