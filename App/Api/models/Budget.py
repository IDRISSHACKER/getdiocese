# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class BudgetApi:
    def __init__(self):
        self.db = bdd()

    def setBudget(self, id, structure, annee, montant):
        self.db.save("INSERT INTO [GestDiocese].[dbo].[BUDGET_PRE]([id_b], [code_st], [annee_b], [montant_b]) VALUES(?,?,?,?)", [id, structure, annee, montant])
        return True

    def getBudgets(self):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[BUDGET_PRE]")
        except Exception:
            print("erreur l'ors de la recuperation des budgets")
            return []

    def getBudget(self, date, montant):
        try:
            return self.db.query("SELECT * FROM [GestDiocese].[dbo].[BUDGET_PRE] WHERE [GestDiocese].[dbo].[BUDGET_PRE].[annee_b] = ? AND [GestDiocese].[dbo].[BUDGET_PRE].[montant_b] = ?", [date, montant])
        except Exception:
            print("erreur l'ors de la recuperation  du budget")
            return []

    def updateBudget(self, key, newTitle):
        try:
            return self.db.save(f"UPDATE [GestDiocese].[dbo].[SERVICES]  SET [intitule_s] = '{newTitle}' WHERE [code_s] = ?", [key])
        except Exception:
            print("erreur l'ors de la mise à jours  du budget")
            return []

    def removeBudget(self, annee, montant):
        try:
            self.db.save("DELETE FROM [GestDiocese].[dbo].[BUDGET_PRE] WHERE [GestDiocese].[dbo].[BUDGET_PRE].[annee_b] = ? AND [GestDiocese].[dbo].[BUDGET_PRE].[annee_b] = ?",
                         [annee, montant])
            return True
        except:
            print("Erreur lors de la supression du budget!")


if __name__ == "__main__":
    api = BudgetApi()
    if api.setBudget():
        print("Save with success")

