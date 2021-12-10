class Main:
    def __init__(self, name):
        self.name = name

    def Hello(self):
        print(f"Bonjour {self.name}")

    def Bye(self):
        print(f"Bye Bye {self.name}")

    def rename(self, newName):
        self.name = newName


