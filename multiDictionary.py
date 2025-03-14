import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self):
       self.dizionari = {}
       pass

    def addDictionary(self, language, path):
        nuovo_dizionario = d.Dictionary()
        nuovo_dizionario.loadDictionary(path)
        self.dizionari[language] = nuovo_dizionario

    def printDic(self, language):
        if language in self.dizionari.keys():
            self.dizionari[language].printAll()
        else:
            print(f"Nessun dizionario trovato per {language}")

    def searchWord(self, words, language):
        if language not in self.dizionari.keys():
            print(f"Nessun dizionario trovato per {language}")
            return

        dizionario = self.dizionari[language]
        parole_risultanti = []

        for parola in words:
            parola_rich = rw.RichWord(parola)
            parola_rich.corretta = dizionario.contains(parola)
            parole_risultanti.append(parola_rich)

        return parole_risultanti


