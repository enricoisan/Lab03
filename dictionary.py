class Dictionary:
    def __init__(self):
        self._dict = [] # Lista che conterrà le parole
        pass

    def loadDictionary(self,path):
        with open(path, "r", encoding = "utf-8") as file:
            self._dict = [riga.strip() for riga in file.readlines()]

    def printAll(self):
        for parola in self._dict:
            print(parola)

    @property
    def dict(self):
        return self._dict

    # Metodo aggiunto da me
    def contains(self, parola):
        if parola in self._dict:
            return True
        else:
            return False