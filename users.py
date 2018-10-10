



class Pouzivatel:
    """
    Trieda Pouzivatel obsahuje nasledovne funkcie: ...
    """
    def __init__(self, meno, priezvisko, email, heslo):
        self.meno, self.priezvisko, self.email, self.heslo = meno, priezvisko, email, heslo


    # def vytvor_pouzivatela(self):
    #     Pouzivatel.vyhladaj_pouzivatela(self.email)

        # vyhladaj / skontroluj ci pouzivatel existuje
        # ak existuje tak vrat existujuceho
        # ak neexistuje tak zaloz noveho
        # SQLdb.zapis(self, sql)

    def vyhladaj_pouzivatela(self,email):
        SQLdb.hladaj('pouzivatelia','email',email)





#    def deaktivuj_pouzivatela(self,email):
