x = 1
if (x == 1 or x == 2):   #musi spełnić 1dną kondycję
    print(x)
elif (x == 3 and x >= 0): #musi spełniać obydwie kondycje
    print(f"x jest równe {x}")
else:
    print("Nie wiem ile x wynosi")

match x:
    case 1:
        print("switch: x to jeden")
    case 2:
        print("switch: x to dwa")
    case _:
        print("switch: Komunitak dla każdego innego x")

biblioteka={
    1:"tekst1", 2:"tekst2"
    }
    #dla funkcji.get("domyślna wartość")
print(biblioteka[x])

def podstawianie(wartosc):
    try:
        print(biblioteka[wartosc])
    except:
        print('błąd')
#https://stackoverflow.com/questions/21962763/using-a-dictionary-as-a-switch-statement-in-python

podstawianie(3)

def calculator(op, part1, part3):
    return {
        '+': part1+part3,
        '-': part1-part3,
        '*': part1*part3,
        '/': part1/part3
    }.get(op, f"The operation '{op}' is not supported!") # for default if op is not found

print(calculator('-+', 1, 12))

def dodawanie(x,y):
    print("wynik dodawania:", x+y)
x = lambda x, y, *args: print("Wynik dodawania (funkcja lambda):", x+y)
#funkcja x przyjmuje wiele argumentow, ale jedynie dodaje dwa pierwsze do siebie
druk = lambda *x: print(x) #drukuje podane argumenty
x(1,2, 1, 3, 4)
dodawanie(1,3)
druk(1,2,3,4,5,6,7,8,9)

def dodaj(*x): #funkcja co dodaje dowolną ilość argumentów
    suma = 0
    for el in x:
        suma += el
    return suma

print(dodaj(42,123,566,343,222,-23))

#Kod ze stackoverflow.com
#https://stackoverflow.com/questions/21962763/using-a-dictionary-as-a-switch-statement-in-python
#z małą zmianą kodu
def default():
    print("Incorrect input!")

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    return a/b

line = input("Input: ")
parts = line.split(" ")
part1 = float(parts[0])
op = parts[1];
part3 = float(parts[2])

dict = {
    '+': add(part1, part3),
    '-': sub(part1, part3),
    '*': mult(part1, part3),
    '/': div(part1, part3)
    }

try:
    print(dict[op])
except KeyError:
    default()