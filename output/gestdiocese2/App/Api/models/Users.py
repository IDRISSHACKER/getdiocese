from App.Api.models.bdd.Connexion import bdd


class Users:
    def __init__(self):
        super(Users, self).__init__()
        self.bd = bdd()

    def register(self, name, surname, password):
        if self.bd.save("INSERT INTO users(name, surname, password) VALUES(?,?,?)", [name, surname, password]):
            return True
        else:
            return False

    def verifyIfUsersExist(self, name):
        exist = 0
        for user in self.bd.query("SELECT * FROM users WHERE name LIKE ?", [name]):
            exist += 1
        return exist

    def getUser(self, name):
        return self.bd.query("SELECT * FROM users WHERE name = ?", [name])

    def logIn(self, name, password):
        if self.verifyIfUsersExist(name):
            pass
