import sys, pygame, pygame.mixer
from pygame.locals import * 
from random import random
import math

# uruchomienie biblioteki pygame
pygame.init()

#Zegar
clock = pygame.time.Clock()
 
#pociski
pociski = []
  
# zdefiniowane kolory
white = (255, 255, 255)
rosso=(255,0,0)
green = (0, 255, 0)
# rozmiar okna
X = 800
Y = 500
kierunek_czolgu = True #True dla kierunek prawo, False dla kierunek lewo
  
# stworzenie okna o wymiarach X, Y
display_surface = pygame.display.set_mode((X, Y ))
  
# ustawienie nazwy okna modułu pygame
pygame.display.set_caption('Czołgi')
  
# stworzenie obiektu na płaszczyźnie okna
tank = pygame.image.load(r'./tanks/tank.png').convert_alpha()   #przypisanie zmiennej tank zdjecia
tank = pygame.transform.scale(tank, (40, 30))  #zmiana rozmiaru zdjecia do 40 na 30 pikseli
pocisk = pygame.image.load(r'./tanks/tank.png').convert_alpha()
pocisk = pygame.transform.scale(pocisk, (10, 8))
#pygame.Surface((60, 60), pygame.SRCALPHA)
pygame.draw.circle(pocisk, [255,0,0], [30, 30], 30)
#pocisk = pygame.draw.circle(display_surface, rosso, (100,100), 20).convert_alpha()
strzal = pygame.mixer.Sound("./tanks/sf_cannon_01.mp3")
#czołg przeciwnika
enemy_tank = pygame.image.load(r'./tanks/tank.png').convert_alpha()   #przypisanie zmiennej tank zdjecia
enemy_tank = pygame.transform.scale(enemy_tank, (40, 30))
enemy_tank = pygame.transform.flip(enemy_tank, True, False)
#zmienne mówiące o początkowej pozycji czołgu
minx = 20
maxx = 380 #940 dla full HD
#formula na losowa liczbe miedzy min a max:
losowa = minx + (random() * (maxx - minx))

tank_pos_x = losowa #1920 podzielone na 2 960 - gracz miedzy 20 a 940 (20 pixeli szerokosc czolgu)
tank_pos_y = 380 #poki co mamy jedna plaszczyzne, wysokosc taka sama
nachylenie = 0

#zmienne mówiące o początkowej pozycji czołgu
enemy_minx = 500
enemy_maxx = 750 #940 dla full HD
#formula na losowa liczbe miedzy min a max:
enemy_losowa = enemy_minx + (random() * (enemy_maxx - enemy_minx))
etank_pos_x = enemy_losowa 
etank_pos_y = 380


pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Kąt nachylenia: {}'.format(nachylenie), True, (155,155,155))

#definicja funkcji
def narysujOknoGry():
    display_surface.fill(white)
    pygame.draw.rect(display_surface,green,[00,410,800,100]) #rysowanie tła
    display_surface.blit(tank, (tank_pos_x, tank_pos_y))
    display_surface.blit(textsurface, (40, 50))
    display_surface.blit(enemy_tank, (etank_pos_x, etank_pos_y))
    #display_surface.blit(pocisk, (pociski[0][0], pociski[0][1]))
    #display_surface.blit(pocisk, (ball['pos']['x'], ball['pos']['y']))    
    clock.tick(60)
    pygame.display.update()
def narysujOknoGry2(x, y):
    #display_surface.fill(white)
    #pygame.draw.rect(display_surface,green,[00,410,800,100]) #rysowanie tła
    #display_surface.blit(tank, (tank_pos_x, tank_pos_y))
    display_surface.blit(textsurface, (40, 50))
    #display_surface.blit(enemy_tank, (etank_pos_x, etank_pos_y))
    display_surface.blit(pocisk, (x, y))
    pygame.display.update() 
#stałe dt. pocisku
ball={'m': 1, 'v':[0,0], 'pos':{'x': tank_pos_x, 'y':370}}
g=-9.8
v0=80
theta=nachylenie*3.14158/180        #masa kuli
ball['v']=[v0*math.cos(theta),v0*math.sin(theta)]    #wektor prędkości kuli
print(ball)
t=0
dt=0.1
zmiana = 20
# niekończąca się pętla

while True :
    narysujOknoGry()
    # kopiowanie obiektu do płaszczyzny na pozycję
    #(tank_pos_x, tank_pos_y)
    #mx, my = pygame.mouse.get_pos()
    #move_ticker = 0
    predkosc = 1
    pressed = False
    # pętla przez zdarzenia (np naciśnięcie klawisza)
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN: #nasłuchiwanie klawiszy
            if event.key == pygame.K_SPACE: #jeśli spacja naciśnięta to:
                print("BOOM!")
                strzal.play()
                while ball['pos']['y']<=400:
                    clock.tick(100)
                    F=ball['m']*g
                    print(ball['v'][1])
                    ball['v'][1]+=(F/ball['m'])*dt #predkosc gor/dol
                    ball['pos']['x']+=ball['v'][0]*dt
                    ball['pos']['y']-=ball['v'][1]*dt
                    t+=dt
                    #F=ma
                    #S=at^2/2
                    print(ball)
                    narysujOknoGry2(ball['pos']['x'], ball['pos']['y'])
                    
                pociski.append([losowa+10, 390])
                print(ball)#"Pociski =",pociski[0][0], pociski[0][1])
                

            if event.key == pygame.K_UP:
                if nachylenie == 90:
                    print("Osiągnęto maksymalne nachylenie!")
                else:
                    nachylenie += predkosc
                    theta=nachylenie*3.14158/180        
                    ball['v']=[v0*math.cos(theta),v0*math.sin(theta)]
                    if nachylenie > 90: #w razie przekroczenia 180 stopni
                        nachylenie = 90
                    predkosc *= 4
                    textsurface = myfont.render('Kąt nachylenia: {}'.format(nachylenie), True, (111,111, 111))
            else:
                predkosc = 1
            if event.key == pygame.K_DOWN:
                if nachylenie == 0:
                    theta=nachylenie*3.14158/180        #masa kuli
                    ball['v']=[v0*math.cos(theta),v0*math.sin(theta)]
                    print("Osiągnęto minimalne nachylenie!")
                else:
                    nachylenie -= predkosc
                    theta=nachylenie*3.14158/180        #masa kuli
                    ball['v']=[v0*math.cos(theta),v0*math.sin(theta)]
                    if nachylenie < 0: #w razie przekroczenia 180 stopni
                        nachylenie = 0
                    predkosc *= 4
                    textsurface = myfont.render('Kąt nachylenia: {}'.format(nachylenie), True, (111,111, 111))
            else:
                predkosc = 1

            '''if (event.key == pygame.K_DOWN and event.key == pygame.K_LSHIFT):
                nachylenie -= 10
                textsurface = myfont.render('Kąt nachylenia: {}'.format(nachylenie), True, (111,111, 111))
            '''
            if event.key == pygame.K_LEFT:
                if kierunek_czolgu == True: #jesli obrocony w prawo
                    tank = pygame.transform.flip(tank, True, False)
                    kierunek_czolgu = False #obracamy czołg
                    #display_surface.blit(tank, (tank_pos_x, tank_pos_y))
                if (zmiana == 0):
                    print("Dalej nie pojedziesz w tej rundzie!")
                else:
                    tank_pos_x+=-2
                    zmiana -= 1
                ball['pos']['x']=tank_pos_x
            if event.key == pygame.K_RIGHT:
                if kierunek_czolgu == False: #jesli obrocony w lewo
                    tank = pygame.transform.flip(tank, True, False)
                    kierunek_czolgu = True  #obracamy czołg
                    #display_surface.blit(tank, (tank_pos_x, tank_pos_y))
                if (zmiana == 0):
                    print("Dalej nie pojedziesz w tej rundzie!")
                else:
                    tank_pos_x+=2
                    zmiana -= 1
                ball['pos']['x']=tank_pos_x
            if event.key == pygame.K_F4: #przy nacisnieciu F4 wychodzi z gry
                # odłączenie biblioteki pygame
                pygame.quit()
            
                

            # wyjście z programu
                quit()
  
        #ustawienie zegara
    clock.tick(10)
    
        # rysowanie obiektów na ekranie
    pygame.display.update()
'''
    for b in range(len(pociski)):
        pociski[b][0] -= 10
    for p in pociski[:]:
        if p[0] < 0:
            pociski.remove(p)
'''
#Plan:
#dodac akcję strzelania
#dodać ruch paraboliczny pocisku
#dodac wykrycie kolizji z ziemia (wysokosc y =~ 360)
#dodac wykrycie kolizji z czołgiami (kwadrat kolizji wokół czołgów)
#dodać podział na tury
#wynik/zdecydowac kiedy gra sie skonczy/odswiezanie mapy etc

