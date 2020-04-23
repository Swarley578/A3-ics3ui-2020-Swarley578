#space invaders pygame
import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

#code for the player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

#code for the movement of your character.
    def update(self):
        self.speedx = 0
        # if key left pressed it moves left at a speed of -8
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        # if key right pressed it moves right at a speed of 8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        # code s it can't go past the borders
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if  self.rect.left < 0:
            self.rect.left = 0

#code to generate bullets
    def shoot(self):
        bullet = Weapon(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

#code for enemies
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        #code for where the blocks generate
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-105, -30)
        self.speedy = random.randrange(1, 3)
        self.speedx = random.randrange(-1, 1)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #code to regenerate enemies at the top
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-105, -30)
            self.speedy = random.randrange(1, 8)

#code for bullets
class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        #code for where weapon generates, code so that it generates in the middle of your player sprite
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -15

    def update(self):
        self.rect.y += self.speedy
        #delete if it moves off screen
        if self.rect.bottom < 0:
            self.kill()

#code to load sprites
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
            #code to fire bullets, if space bar pressed bullet fires
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()


    # Update
    all_sprites.update()

# see if bullet hits enemy
    hits = pygame.sprite.groupcollide(bullets, mobs, True, True)
    #code for if mob disapears another one respawns
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

# see if enemy hits character
    hits = pygame.sprite.spritecollide(player, mobs, False)
    # if enemy sprite hits character close the game
    if hits:
        running = False
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()