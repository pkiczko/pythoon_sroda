#http://analityk.edu.pl/fizzbuzz/

lista = [0]*100 #ta komenda tworzy listę zer, ilość 100
for i in range(1,101): #iteracja dla i od 1 do 101 (czyli wykonuje zawartość pętli 100 razy)
    if i % 15 == 0: #komenda sprawdza czy i podzielone przez 15 daje resztę 0
        lista[i-1]='FizzBuzz' #(i-1) ponieważ pierwszy element listy ma indeks 0
    elif i % 3 == 0:
        lista[i-1]='Fizz'
    elif i % 5 == 0:
        lista[i-1]='Buzz'    
    else: 
        lista[i-1]=i


print(lista)

#alternatywna metoda, bez deklaracji listy 100 zer
'''
lista = [] #deklaracja listy
for i in range(1,101):
    if i % 15 == 0:
        lista.append('FizzBuzz')  #komenda append dodawaje element na koniec listy
    elif i % 3 == 0:
        lista.append('Fizz')
    elif i % 5 == 0:
        lista.append('Buzz')   
    else: 
        lista.append(i)


print(lista)
'''

#http://analityk.edu.pl/najmniejsza-oraz-najwieksza-liczba-na-liscie-w-python/

lista2 = [1,3,7,11,2,-6,0]  #lista przypadkowych zmiennych
minimum = None #deklaracja zmiennej o wartości None
maximum = None
for element in lista2:      #porównuje kolejne elementy w lista2
    if minimum == None:     #jeśli minimum nie zdefiniowane przypisuje pierwszą liczbę do niej
        minimum = element
    elif minimum > element: #porównuje minimum z kolejnym elementem
        minimum = element   #jeśli element mniejszy niż zapisane minimum, minimum przyjmuje wartość elementu

    if maximum == None:     #jeśli maximum nie zdefiniowane przypisuje pierwszą liczbę do niej
        maximum = element 
    elif maximum < element: #jeśli element większy niż zapisane maximum, maximum przyjmuje wartość elementu
        maximum = element
print('Minimum to: ', minimum)
print('Maximum to: ', maximum)
#Alternatywna metoda (mniej kodu, więcej obliczeń dla komputera)
lista2.sort() #sortuje całą lista2
print("Posortowana lista: ", lista2)
print('Minimum to: ', lista2[0])             #minimum to pierwszy element posortowanej listy
print('Maximum to: ', lista2[len(lista2)-1]) #maximum to ostatni element posortowanej listy
#http://analityk.edu.pl/zliczanie-liter/
inwokacja = "Litwo! Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie."
inwo2 = inwokacja.replace('!', '').replace('.', '').replace(',', '') #usuwanie interpunkcji
inwo3 = inwo2.replace(' ', '') #usunięcie spacji celem wyświetlenia ilości liter
print("Ilosc liter w tekscie: ", len(inwo3))
poszatkowane = inwo2.split(" ") #podzielenie elementu string na elementy listy - separator to " ", czyli spacja

print(poszatkowane)
print("Ilosc slow: ", len(poszatkowane)) #długość listy to ilość elementów listy
print(poszatkowane[0].lower()) #litwo
slownik = {}  #definiowanie pustego elementu dictionary
for slowa in poszatkowane:  #pętla po wszystkich elementach listy poszatkowane (czyli po wszystkich słowach)
    if slowa.lower() in slownik:    #metoda lower() zmienia wszystkie litery słów na małe litery
        slownik[slowa.lower()]+=1   #dodajemy jeden do wartości do każdego słowa które już jest w dictionary (słowniku)
    else:
        slownik[slowa.lower()]=1    #jeśli słowa nie ma w dictionary (słowniku), tworzymy nowy klucz (słowo), przypisujemy wartość 1
najczestsze_slowo = max(slownik, key=slownik.get) #wyświetla najczęściej używane słowo (w przypadku 2óch słów występujących 
                                                  #równie często pokazuje jedynie pierwsze z nich)
print(najczestsze_slowo,' - ilosc wystapien: ', slownik[najczestsze_slowo] )

#http://analityk.edu.pl/sortowanie-babelkowe/
#sortowanie bąbelkowe

A = [2,1,5,3,6,0]
B = [2,1,5,3,6,0]
#max2 = 0
#min2 = 0
print('dlugosc A: ', len(A))
zmiany=None
iteracje = 0

while zmiany!=0:
    zmiany = 0   #jeśli zmian 0 w całej iteracji, wyjdzie z pętli while
    iteracje +=1 #dla naszej informacji, ile razy pętla while była użyta
    print(iteracje, " - numer iteracji")
    print(A)
    for i in range(0,len(A)-1): #porównuje kolejne elementy lista, przestawia wg wielkości    
        if A[i] > A[i+1]:
            zmiany += 1            
            A[i], A[i+1] = A[i+1], A[i] #zamiana miejscami 2 wartości w liście

print(A)
#rozwiązanie w 2óch linijkach
B.sort()
print("Rozwiązanie z użyciem funkcji sort(): ", B)

#http://analityk.edu.pl/suma-dwoch-liczb/
#czy suma dwóch elementów listy i których równa 9
S = [1,3,5,2,11,7]
    #0,1,2,3, 4,5] - indeksy listy
suma9 = False #fałsz
print('Długość S to : ', len(S))
print(S[len(S)-2])
for i in range(0, len(S)-1): #największe i powinno być przedostatnim elementem na liście
    #i = 0 - pierwsza iteracja
    #i = 1 - druga iteracja tej pętli
    for j in range(i+1, len(S)):
        #i=0, j=0 - 1wsza iteracja 
        #i=0, j=1 - 2ga iteracja
        print("Pary liczb użyte: ", S[i], ', ', S[j])
        if S[i] + S[j] == 9:
            print("Znalazłem elementy których suma to 9! Są to: ", S[i], " oraz ", S[j] )
            suma9 = True #prawda
print("Czy któreś dwie liczby dają sumę 9? : ", suma9)

#http://analityk.edu.pl/rzut-moneta-z-python/
#Gra w orła i reszkę
import time #Biblioteka czasu, dla wprowadzania opóźnień
import random

def menu():#definiowanie funkcji
    print("##################")
    print("0. Zakończ program")
    print("1. Wybierz Reszkę")
    print("2. Wybierz Orła")
    print("")
def odliczanie():
    print("3!")
    time.sleep(1) #opóźnienie 1s
    print("2!")
    time.sleep(1) #opóźnienie 1s
    print("1!")
    time.sleep(1) #opóźnienie 1s
def wybor_gracza(i):
    if i == 2:
        return "reszka"
    if i == 1:
        return "orzeł"

x = None
wynik = {"gracz":0, "komputer":0}
while x!=0:
    
    menu()
    x = input("Podaj opcję: ")
    odliczanie()
    if random.choice(["orzeł", "reszka"]) == wybor_gracza(x):
        wynik.gracz += 1
    else:
        wynik.komputer += 1
    #1den Reszka, 2 orzeł

    print("Wynik: ", wynik)
        



        
