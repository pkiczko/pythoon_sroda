import math
import pygame



def test():
    '''test docstring, python'''
    print("123 test")
    return 
    

print(math.log.__doc__)

def dodaj_dwie_liczby(a, b):
    '''dodaje 2 liczby
    zastosowanie: dodaj_dwie_liczby(argument1, argument2)
    '''
    return a+b

def obwod_kola(promien):
    '''bierze promien, zwraca obwod kola'''
    return 2* math.pi *promien

#liczba1 = a
#liczba2 = b

r= 10

print('Suma dwoch liczb, 1 oraz 2: ', dodaj_dwie_liczby(1,2))
print('Obwod kola o promieniu ', r, ' to: ', obwod_kola(r))

print("#################### \nKlasy - Class \n####################")

class Osoba:
    def __init__(self, imie, nazwisko, wiek, adres, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.adres = adres
        self.telefon = telefon
    def przedstaw(self):
        print("Czesc, mam na imie " + self.imie)

    def numer_telefonu(self):
        print("Numer do tej osoby to: ", self.telefon)

os1 = Osoba("Marcin", "Kowalski", 34, "ul. Modlinska 1", "+48123456789")

os1.przedstaw()
print(os1.telefon)
os1.numer_telefonu()
print("#################### \nDziedziczenie \n####################")

class Uczen(Osoba):
    def __init__(self, imie, nazwisko, wiek, adres, telefon, oceny, rozmiar_buta):
        super().__init__(imie, nazwisko, wiek, adres, telefon)
        self.oceny = oceny
        self.rozmiar_buta = rozmiar_buta
    def jaki_but(self):
        print("Ta osoba ma rozmiar buta: ", self.rozmiar_buta)
    def ocena_anglik(self):
        print("Ocena z angielskiego: ", self.oceny["angielski"])
    def postarzenie(self):
        self.wiek += 1
        print("nowy wiek osoby: ", self.wiek)
    pass

uczen1 = Uczen("Jola", "Nowak", 14, "ul. Modlinska 12", "-", {"angielski": 2, "polski":3}, 38)

uczen1.numer_telefonu()
uczen1.jaki_but()
uczen1.ocena_anglik()
uczen1.postarzenie()

#####################################################################################


