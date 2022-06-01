 
# Pygame sprite Example
import pygame
from pygame.locals import *
from random import random
import time
import math

WIDTH = 800
HEIGHT = 600
FPS = 120

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#funkcja wyliczająca dystans między dwoma punktami
def dystans(pkt1, pkt2): #wymaga biblioteki math - import math
    return ((pkt1[0]-pkt2[0])**2+(pkt1[1]-pkt2[1])**2)**0.5 #w przypadku pierwiastka 3ciego stopnia (1/3)

def losx():
    return int(random() * 800)
def losy():
    return int(random() * 600)
def losowy_punkt():
    return [int(random() * 800), int(random() * 600)]

def ilosc_odleglosci_w_zbiorze_punktow(x):
    suma = 0
    while x !=0:
        x -= 1
        suma += x
    return suma
print('ilosc_odleglosci_w_zbiorze_punktow: ', ilosc_odleglosci_w_zbiorze_punktow(5))
def dodaj_punkty(ilosc):
    for i in range(ilosc):
        zbior_elementow.append(losowy_punkt())


#print(zbior_elementow)
#print('losowy pkt: ', losowy_punkt())
#ilosc_losowych = 1
#losowa_x2 = losx()
#losowa_y2 = losy()
#zbior_elementow.append([losowa_x2, losowa_y2])
#print(zbior_elementow)
#print(zbior_elementow[0])
#print(zbior_elementow[1])
#print('pierwsze x: ',losowa_x1, 'pierwsze y: ', losowa_y1)
#odleglosc = dystans(zbior_elementow[0], zbior_elementow[1])
#if odleglosc >= 100:
#        ilosc_losowych += 1
#print('Propozyjca punktu: x:', losowa_x2, 'nowa y: ', losowa_y2)
#print(f'Odległość: {odleglosc}') #string injection

#dodajemy 4 pkt
zbior_elementow = []
zbior_prawd = 0
ilosc_punktow = 15 #ile punktow losowo dodac
odleglosc_puntkow = 50 #minimalna odleglosc miedzy wszystkimi punktami
while zbior_prawd != ilosc_odleglosci_w_zbiorze_punktow(ilosc_punktow): #dla 5ciu punktów ilość odległóści między punktami to 4+3+2+1 = 10
    zbior_odleglosci = []
    zbior_elementow = []
    dodaj_punkty(ilosc_punktow) #dodajemy 5 nowych puntkow do zbior_elementow
    zbior_punktow = zbior_elementow[:] #zapisujemy wynik w dodatkowej zmiennej
    z = 0
    for i in range(len(zbior_elementow)-1):
        z = 0    
        for i in range(len(zbior_elementow)-1):
            z += 1
            zbior_odleglosci.append(dystans(zbior_elementow[0],zbior_elementow[z]))
        zbior_elementow.pop(0) #ta funkcja psuje nam oryginalny zbior - stad
        #koniecznosc zapisania oryginalnych punktow w dodatkowym zbiorze
    print('zbior_odleglosci:', zbior_odleglosci)
    zbior_prawd = 0
    for d in zbior_odleglosci: #odleglosc miedzy pierwszym a reszta punktow
        if d < odleglosc_puntkow:
            print("za mało")
        else:
            zbior_prawd += 1
    
print("Zbiór punktow: ", zbior_punktow)

class Frog(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('./sprites/attack_1.png'))
		self.sprites.append(pygame.image.load('./sprites/attack_2.png'))
		self.sprites.append(pygame.image.load('./sprites/attack_3.png'))
		self.sprites.append(pygame.image.load('./sprites/attack_4.png'))
		self.sprites.append(pygame.image.load('./sprites/attack_5.png'))
		self.sprites.append(pygame.image.load('./sprites/attack_6.png'))
		self.sprites.append(pygame.image.load('./sprites/attack_7.png'))
		self.sprites.append(pygame.image.load('./sprites/attack_8.png'))
		self.sprites.append(pygame.image.load('./sprites/attack_9.png'))
		self.sprites.append(pygame.image.load('./sprites/attack_10.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = (pos_x, pos_y, 50, 50)  

	def attack(self):
		self.attack_animation = True

	def update(self):
		if self.attack_animation == True:
			self.current_sprite += 0.25
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False
		self.image = self.sprites[int(self.current_sprite)]
class Klocek(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self, pos_x, pos_y):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(GREEN)
        self.stop=False
        self.rect = self.image.get_rect()
        self.rect.center=(pos_x,pos_y)

    def update(self):
        collide = [s for s in pygame.sprite.spritecollide(self, self.groups()[0], False, pygame.sprite.collide_mask) if s != self]
        if (self.rect.y <= 580 and self.stop == False and not collide):
            self.rect.y += 1

        
class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image
        self.image = pygame.Surface((40, 30))
        self.image.fill(GREEN)
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # center the sprite on the screen
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        # any code here will happen every time the game loop updates
        #self.rect.x -= 4
        #self.rect.y += 3
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if self.rect.colliderect(enemy.rect):
            self.image.fill(RED)
        else:
            self.image.fill(GREEN)
        if self.rect.colliderect(frog.rect):
            self.image.fill(WHITE)
            frog.attack()
        


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Example")
clock = pygame.time.Clock()

all_blocks = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
enemy = Player()
klocek1=Klocek(400,00)
klocek2=Klocek(411,200)
klocek3=Klocek(404,100)
klocek4=Klocek(410,320)
#for klocek in zbior_punktow:
    #klocuszek+i = Klocek(klocek[0], klocek[1])
var_holder = {}
for i in range(10):
    var_holder['my_var_' + str(i)] = "iterationNumber=="+str(i)
print('var_holder:', var_holder)
frog = Frog(200,200)
enemy.rect.x = 100
enemy.rect.y = 100
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(frog)
all_blocks.add(klocek1)
all_blocks.add(klocek2)
all_blocks.add(klocek3)
all_blocks.add(klocek4)
# Game loop
running = True
speed = 2
while running: #petla gry
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    '''for klocek in all_blocks:
            gets_hit = pygame.sprite.spritecollideany(klocek, all_blocks)
            if klocek == gets_hit:
                klocek.stop = True'''
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
        frog.attack()
    if keys_pressed[pygame.K_RIGHT]:
        player.rect.x+=5
        #if player.rect.right == enemy.rect.left:
            #enemy.image.fill(BLUE)       
    if keys_pressed[pygame.K_LEFT]:
        player.rect.x-=5
        #if player.rect.left == enemy.rect.right:
            #enemy.image.fill(WHITE) 
    if keys_pressed[pygame.K_UP]:
        player.rect.y-=5
        if (player.rect.top == enemy.rect.bottom and player.rect.x < enemy.rect.x + 40 and player.rect.x > enemy.rect.x - 40):
            enemy.image.fill(RED)
    if keys_pressed[pygame.K_DOWN]:
        player.rect.y+=5
        #if player.rect.bottom == enemy.rect.top:
        enemy.image.fill(GREEN)
    if keys_pressed[pygame.K_ESCAPE]:
        running = False
    # Update
    all_sprites.update()
    all_blocks.update()
    # Draw / render
    screen.fill(BLACK)
    all_blocks.draw(screen)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
