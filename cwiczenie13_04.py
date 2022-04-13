#do zrobienia
#aplikacja konsolowa
#opcja 1 - dodaje dane do "bazy danych"
#opcja 2 - wyświetla wszystko w bazie danych
#opcja 3 - wyszukiwanie rekordów z bazy danych

#http://analityk.edu.pl/rzut-moneta-z-python/
#Gra w orła i reszkę
import time 
import random
x = None
def menu():#definiowanie funkcji
    print("##################")
    print("###Baza Danych####")
    print("##################")
    print("1. Dodaj wpis do bazy")
    print("2. Wyświetl całą bazę")
    print("3. Znajdź w bazie")
    print("4. Zakończ program")
    print("")
baza=[]
def wprowadzanie():
    dane = input("Podaj dane do wpisania do bazy: ")
    baza.append(dane)
def wyswietl_baze():
    print(baza)
def znajdz_w_bazie():
    print("Szukanie w bazie...")
    szukaj = input("Podaj szukanego słowa: ")

#Tutaj wpisać kod do wczytania danych z pliku baza.txt
with open("baza.txt", "r") as f:
    plik = f.read().split('.')
    plik.pop()
    f.close()

print(plik)
baza = plik
while x!="4":    
    menu() #drukowanie menu z funkcji
    x = input("Podaj opcję:") #należałoby sprawdzić czy wprowadzono cyfrę - by zapobiec błędom
    print("Wprowadzono: ", x)
    match x:
        case "1":
            wprowadzanie()
        case "2":
            wyswietl_baze()
        case "3":
            znajdz_w_bazie()
        case "4":
            print('Zapis danych przed wyjściem...')
            with open("baza.txt", "w") as f:
                for element in baza:
                    f.write(f'{element}.')
                f.close()
        case _:
            print("Niepoprawny wybór! Wybierz ponownie.")

