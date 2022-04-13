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
