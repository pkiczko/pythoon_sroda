import pygame
  
# uruchomienie biblioteki pygame
pygame.init()
  
# zdefiniowane kolory
white = (255, 255, 255)
rosso=(255,0,0)
green = (0, 255, 0)
# rozmiar okna
X = 800
Y = 500
  
# stworzenie okna o wymiarach X, Y
display_surface = pygame.display.set_mode((X, Y ))
  
# ustawienie nazwy okna modułu pygame
pygame.display.set_caption('Image')
  
# stworzenie obiektu na płaszczyźnie okna
tank = pygame.image.load(r'tank.png')   #przypisanie zmiennej tank zdjecia
tank = pygame.transform.scale(tank, (40, 30))  #zmiana rozmiaru zdjecia do 40 na 30 pikseli
#zmienne mówiące o początkowej pozycji czołgu
tank_pos_x = 200    
tank_pos_y = 380
# niekończąca się pętla
while True :
    
    # wypełnienie okna kolorem białym
    display_surface.fill(white)
  
    # kopiowanie obiektu do płaszczyzny na pozycję
    #(tank_pos_x, tank_pos_y)
    display_surface.blit(tank, (tank_pos_x, tank_pos_y))
    pygame.draw.rect(display_surface,green,[00,410,800,100])
    # pętla przez zdarzenia (np naciśnięcie klawisza)
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN: #nasłuchiwanie klawiszy
            if event.key == pygame.K_SPACE: #jeśli spacja naciśnięta to:
                print("BOOM!")
                pygame.draw.rect(display_surface,rosso,[100,100,100,100])
            if event.key == pygame.K_UP:
                print("UP")
            if event.key == pygame.K_DOWN:
                print("DOWN")
            if event.key == pygame.K_LEFT:
                print("LEFT")
                tank_pos_x+=-2
            if event.key == pygame.K_RIGHT:
                print("RIGHT")
                tank_pos_x+=2
  
        # 
        if event.type == pygame.QUIT :
  
            # odłączenie biblioteki pygame
            pygame.quit()
  
            # wyjście z programu
            quit()
  
        #ustawienie zegara
        clock = pygame.time.Clock()
        clock.tick(175) 
        # rysowanie obiektów na ekranie
        pygame.display.update()