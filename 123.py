from numpy import random

result = random.randint(2)  #0 albo 1
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


##################

#wprowadzanie zmiennych do string'u:
print("Autobus linii {} skręca na skrzyżowaniu w {}.".format(112,'prawo'))

#Przydatne narządzia do formatowania tekstu:
zdanie="Nr Osiem dziewiec DziEsiEc"

#Funkcje do tekstu: capitalize(), title(), swapcase(), str.lower()
# Zmiana string'a na listę: split(), list()   - źródło materiałów: https://github.com/Asabeneh/Python-for-Everyone

print(zdanie.capitalize())
print(zdanie.title())
podzielone_zdanie = zdanie.split(' ')
print(len(podzielone_zdanie[0]))

