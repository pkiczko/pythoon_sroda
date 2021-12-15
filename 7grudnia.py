############ Kontynuacja klasy ##########################
import math


class Postac:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.zycie = 10
        self.umiejetnosci = ["Samoobrona", "Konna Jazda", "Walka wrecz"]
        self.statystyki = {"sila": 5, "zwinnosc": 5, "inteligencja": 5, "kondycja": 5}
        print("Postac stworzona!")
    def przedstaw(self):
        print("Ta postac nazywa sie ", self.nazwa, " HP: ", self.zycie, " Zestaw umiejetnosci ", self.umiejetnosci, " Statystyki: ", self.statystyki)
    def minusHP(self, hp):
        if (isinstance(hp, int) and hp < self.zycie):
            self.zycie += -hp
            print("Straciles ", hp, " zycia!")
            print("Zostalo ci ", self.zycie, " zycia!")
        else: 
            print("Zginales!")
        return self.zycie
    def wzrostSila(self):
        self.statystyki["sila"] += 1
        print("Sila ci wzrasta!")
    def stats(self):
        print("Lista statystyk: ", self.statystyki)
    def dodajUmiejetnosc(self, nazwa):
        self.umiejetnosci.append(nazwa)
    def odejmijUmiejetnosc(self):
        print("Straciles umiejetnosc: ", self.umiejetnosci.pop())
        print("Zycie wzroslo do ", self.minusHP(-2))

rycerz = Postac("Lancelot") #konstruktor (__init__) jest uruchamiany 
                            # przy tworzeniu Postaci rycerz

rycerz.przedstaw()          #tutaj ryczerz przedstawia sie

rycerz.minusHP(3)

rycerz.wzrostSila()
rycerz.stats()
rycerz.dodajUmiejetnosc("Skradanie sie")

rycerz.przedstaw()
rycerz.odejmijUmiejetnosc()
rycerz.przedstaw()

print("######### Funkcje z return #########\n\n")


def pogoda():
    #kod
    return "Bedzie padac snieg!"
def pogoda2():
    print("Sniezyce, przelotne deszcze!")
    return 0
def pogoda3(prognoza):
    return prognoza + "!"

#pogoda2()
print(pogoda2())
print('#####')
pogoda3("Deszcz") #odpala funkcje, ale nic nie widac w konsoli
print(pogoda3("Deszcz"))
if (pogoda2() == 0):
    print("Hurra!")