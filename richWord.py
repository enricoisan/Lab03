class RichWord:
    def __init__(self, parola):
        self._parola = parola # La parola analizzata
        self._corretta = None # Booleano: True se corretta, Falsa se errata

    @property
    def corretta(self):
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        self._corretta = boolValue

    def __str__(self):
        return self._parola