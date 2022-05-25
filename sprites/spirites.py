 
# Pygame sprite Example
import pygame
import random
import time

WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


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
        self.rect = self.image.get_rect()
        self.rect.center=(pos_x,pos_y)

    def update(self):
        if self.rect.y <= 580:
            self.rect.y += 5
        
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

all_sprites = pygame.sprite.Group()
player = Player()
enemy = Player()
klocek=Klocek(300,300)
frog = Frog(200,200)
enemy.rect.x = 100
enemy.rect.y = 100
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(frog)
all_sprites.add(klocek)
# Game loop
running = True
speed = 2
while running: #petla gry
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    
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

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
