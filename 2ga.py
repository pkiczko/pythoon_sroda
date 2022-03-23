from numpy import random
import math as m

result = random.randint(20)
print(result)


#Przydatne komendy
a=1
b='Be'
c=[ 1,"element", "mango", 0.314159]
#   0       1       2           3
dict={"element":"płoza", "teren": "górka", "wysokość": 5}
e=2.71828
fałsz=False #int(False)
tup=(1,2,3,"cztery")

print(type(a))      #<class 'int'>
print(type(b))      #<class 'str'>
print(type(c))      #<class 'list'> #print(type(c[1]))
print(type(dict))   #<class 'dict'>
print(type(e))      #<class 'float'>
print(type(fałsz))  #<class 'bool'>
print(type(tup))    #<class 'tuple'>

#wprowadzanie zmiennych do string'u:
print("Autobus linii {} skręca na skrzyżowaniu w {}.".format(112,'prawo'))

#Przydatne narządzia do formatowania tekstu:
print("Nr \t Miejsce \t Data \t\t Osoba\n")
print("1 \t Miasto \t 12.05.2021 \t Andrzej\n")
print("1 \t Wieś \t\t 13.01.2021 \t Ala\n")
print("1 \t Morze \t\t 2.07.2021 \t Ktoś inny\n")
print("1 \t Powietrze \t 22.12.2020 \t -\n")

#Funkcje do tekstu: capitalize(), title(), swapcase(), str.lower()

# Zmiana string'a na listę: split(), list()   - źródło materiałów: https://github.com/Asabeneh/Python-for-Everyone

#tzw. conditionals - warunki~
#https://github.com/Asabeneh/Python-for-Everyone

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True and False: ', True and False) #obydwa warunki musza byc spelnione
print('True or False:', True or False)      #tylko 1den musi byc spelniony
print('a in an:', 'a' in 'an')


#Wprowadzanie danych:
wiek = input("Podaj swój wiek: ")   #Można odrazu przerobić wynik do liczby całkowitej pisząc 
                                    #wiek = int(input("Podaj swój wiek: "))
print(type(wiek))


if (int(wiek) <= 6):
    print("Pewnie za młody by chodzić do szkoły")
elif (int(wiek) == 10):
    print("Tekst")
else:
    print("Chyba liczba")

#Przypomnienie pętle:
for i in range(5):  #powtórz 5 razy
    #5 razy         #co zawarte w pętli
    continue
while (a < 5):
    print("test {}".format(a))
    a=a+1




#Napisz program. Wytyczne:
# - pobiera dane od użytkownika
# - wykonuje dodatkowe operacje na danych
# - wyświetla wynik pod koniec








