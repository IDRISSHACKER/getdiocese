import json
import os


class dbJson:
    def __init__(self, filename):
        super().__init__()
        self.user = os.getlogin()
        self.folderName = "gestDiocese"
        self.pathToSave = os.path.join("C:","\\","Users", self.user, "Documents", self.folderName)
        self.filename = filename
        self.file = os.path.join(self.pathToSave, self.filename)
    
    def createJson(self, data={}, force=False):
        if not os.path.exists(self.pathToSave):
            os.makedirs(self.pathToSave)
        
        if os.path.exists(self.pathToSave):
            if not os.path.exists(self.file):
              with open(self.file, "w") as FILE:
                json.dump(data, FILE, indent=4)
            
            if force == True:
                with open(self.file, "w") as FILE:
                    json.dump(data, FILE, indent=4)
        

    def getJson(self, FILE = ""):
        if len(FILE) == 0:
            FILE = self.file
        else:
            FILE = os.path.join(self.pathToSave, FILE)

        data = {}

        if os.path.exists(FILE):
            with open(self.file, "r") as f:
                data = json.load(f)
                f.seek(0)
        else:
            self.createJson(data)
        return data
    
    def verifyJson(self):
        if os.path.exists(self.file):
            return True
        else:
            return False

    

if __name__ == "__main__":
    file = dbJson("ih.json")
    file.createJson([
        {
            "name": "Hacker",
            "age": "18",
            "online": True
        
        }
    ])
    
    data = file.getJson()
    print(data)