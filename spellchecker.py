import time
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multi_dict = md.MultiDictionary()
        self.multi_dict.addDictionary("italian", "resources/Italian.txt")
        self.multi_dict.addDictionary("english", "resources/English.txt")
        self.multi_dict.addDictionary("spanish", "resources/Spanish.txt")
        pass

    def handleSentence(self, txtIn, language):
        # Pre-elaborazione del testo
        print(f"Testo in input: {txtIn}")
        txtIn = replaceChars(txtIn).lower().split()
        # Controllo ortografico
        start_time = time.time()
        risultati = self.multi_dict.searchWord(txtIn, language)
        end_time = time.time()

        # Estrazione delle parole errate
        parole_errate = [rw for rw in risultati if not rw.corretta]
        num_errori = len(parole_errate)
        tempo_impiegato = end_time - start_time

        # Output dei risultati
        if len(parole_errate) > 0:
            for parola_errata in parole_errate:
                print (parola_errata._parola)

        print(f"Hai commesso {num_errori} errori")
        print(f"Tempo di esecuzione: {tempo_impiegato}")


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\'*_{}[]()>#+-.!$%^;,=_"
    for c in chars:
        text = text.replace(c, "")
    return text