# -*- coding: utf-8 -*-
from App.Api.models.bdd.Connexion import bdd


class Reset:
    def __init__(self):
        self.db = bdd()

    def resetSettings(self):
        try:
            self.db.save("")
            return True
        except:
            return False
