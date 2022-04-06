#metoda na wyjątki/błędy programu/kodu
#plik źródłowy od Asabeneh'a
#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/17_Day_Exception_handling/17_exception_handling.md

try:
    print(10 + [False])
except:
    print("BŁĄD 001: dodawanie do 10 string'a")

try:
    name = input('Enter your name:')
    year_born = int(input('Year you were born:'))
    age = 2022 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('BŁĄD 002: problem z wprowadzaniem imienia i roku')

try:
    name = input('Enter your name:')
    year_born = int(input('Year you were born:'))
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:       #błąd typu
    print('błąd typu')
except ValueError:      #błąd wartości
    print('błąd wartości')
except ZeroDivisionError: #błąd dzielenia przez 0
    print('błąd dzielenia przez 0')
else:
    print('Jeśli try zadziała to wyświetlam się')
finally:
    print('Ten tekst pod finally zawsze wyświetla się')
#int('0')=0

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
#poniżej gotowe dane wpisane, dla sprawdzenia błędu podanego przez kompilator
name = "Pawel"
year_born = 0 #tu można zmienić wartość dla wygenerowania błędów 
age = 2019 - int(year_born)
print(f'You are {name}. And your age is {age}.')

#odpakowywanie list (array-ów)
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, swe, nor, *reszta = countries
print(fin)
print(reszta)

numbers = [1, 2, 3, 4, 5, 6, 7]
x, *y, szotka, z = numbers
print('wartosc x: ', x)
print('wartosc y: ', y)     #  1 [2, 3, 4, 5, 6] 7
print('wartosc z: ', z)

#Odpakowywanie bibliotek
#przypomnienie biblioteka = {'klucz':'wartosc', 'klucz2':'wartość2'}

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'country':'Finland','name':'Asabeneh', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

def sum_all(*args):  #*args to dowolna ilość danych
    suma = 0
    for element in args:
        suma += element
    return print(suma)
sum_all(11, 22, 32, 0, 0, 0, 0, 0, 0) # suma liczb to 65
sum_all(1, 2, 3, 4, 5, 6, 7)         # 28

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, lst_one, lst_two] #bez gwiazdek listy są nie wypakowane
print(lst)
lst = [0, *lst_one, *lst_two]
print(lst)                  #z gwiazdkami wypakowuje zawartość list (array-ów)

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables): #wykonywanie operacji na elementach (f, v) 2 list jednocześnie
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

def polaczenie_w_liste(*args):  #*args to dowolna ilość danych
    suma = ''
    for element in args:
        suma += element
        sume += ' '
    return suma

year_born = input('Year you were born:')

#od użytkownika zerba 5 danych (dowlonych)
#następnie połączyć te dane ze sobą (w formie string'a)
#oraz w formie array'a (listy)