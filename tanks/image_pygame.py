import sys, pygame, pygame.mixer
from pygame.locals import * 
from random import random

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
tank = pygame.image.load(r'tank.png')   #przypisanie zmiennej tank zdjecia
tank = pygame.transform.scale(tank, (40, 30))  #zmiana rozmiaru zdjecia do 40 na 30 pikseli
pocisk = pygame.draw.circle(display_surface, rosso, (100,100), 20)
strzal = pygame.mixer.Sound("sf_cannon_01.mp3")

#zmienne mówiące o początkowej pozycji czołgu

minx = 20
maxx = 380 #940 dla full HD
#formula na losowa liczbe miedzy min a max:
losowa = minx + (random() * (maxx - minx))

tank_pos_x = losowa #1920 podzielone na 2 960 - gracz miedzy 20 a 940 (20 pixeli szerokosc czolgu)
tank_pos_y = 380 #poki co mamy jedna plaszczyzne, wysokosc taka sama
nachylenie = 0
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Kąt nachylenia: {}'.format(nachylenie), True, (155,155,155))

# niekończąca się pętla

while True :
    
    # wypełnienie okna kolorem białym
    display_surface.fill(white)
    pygame.draw.rect(display_surface,green,[00,410,800,100])
    # kopiowanie obiektu do płaszczyzny na pozycję
    #(tank_pos_x, tank_pos_y)
    display_surface.blit(tank, (tank_pos_x, tank_pos_y))
    display_surface.blit(textsurface, (40, 50))

    
    #move_ticker = 0
    predkosc = 1
    pressed = False
    # pętla przez zdarzenia (np naciśnięcie klawisza)
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN: #nasłuchiwanie klawiszy
            if event.key == pygame.K_SPACE: #jeśli spacja naciśnięta to:
                print("BOOM!")
                strzal.play()
                pygame.draw.rect(display_surface,rosso,[100,100,100,100])

            if event.key == pygame.K_UP:
                if nachylenie == 90:
                    print("Osiągnęto maksymalne nachylenie!")
                else:
                    nachylenie += predkosc
                    if nachylenie > 90: #w razie przekroczenia 180 stopni
                        nachylenie = 90
                    predkosc *= 4
                    textsurface = myfont.render('Kąt nachylenia: {}'.format(nachylenie), True, (111,111, 111))
            else:
                predkosc = 1
            
            if event.key == pygame.K_DOWN:
                if nachylenie == 0:
                    print("Osiągnęto minimalne nachylenie!")
                else:
                    nachylenie -= predkosc
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
                tank_pos_x+=-2
            if event.key == pygame.K_RIGHT:
                if kierunek_czolgu == False: #jesli obrocony w lewo
                    tank = pygame.transform.flip(tank, True, False)
                    kierunek_czolgu = True  #obracamy czołg
                    #display_surface.blit(tank, (tank_pos_x, tank_pos_y))
                tank_pos_x+=2
            if event.key == pygame.K_F4: #przy nacisnieciu F4 wychodzi z gry
                # odłączenie biblioteki pygame
                pygame.quit()
  
            # wyjście z programu
                quit()
  
        #ustawienie zegara
        clock.tick(10)
        # rysowanie obiektów na ekranie
        pygame.display.update()