import pygame
import sys
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TANK_SIZE = 50
FPS = 60
BULLET_SPEED = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank Game")

tank_image = pygame.Surface((TANK_SIZE, TANK_SIZE))
tank_image.fill(RED)
bullet_image = pygame.Surface((10, 10))
bullet_image.fill(WHITE)

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = tank_image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
tanks = pygame.sprite.Group()
bullets = pygame.sprite.Group()

tank = Tank(SCREEN_WIDTH // 2, SCREEN_HEIGHT - TANK_SIZE)
all_sprites.add(tank)
tanks.add(tank)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tank.shoot()

    all_sprites.update()

    hits = pygame.sprite.groupcollide(tanks, bullets, False, True)
    for hit in hits:
    
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
