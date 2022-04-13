x = 3
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
#https://stackoverflow.com/questions/21962763/using-a-dictionary-as-a-switch-statement-in-python