import pygame
import random

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Dino Jumper")
gameGoing = False
clock = pygame.time.Clock()

CactusImg = pygame.image.load('cactus.png')
CactusImg = pygame.transform.scale(CactusImg, (100, 100))

# Variables
p1x = 0
p1y = 0

yVel = 0

jumping = False
jump_count = 15  


CactusHeights = [40, 20, 60, 30, 80]
CactusXpos = []
for x in range(1, 5):
    CactusXpos.append(random.randrange(200, 3000))

while not gameGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameGoing = True

    keys = pygame.key.get_pressed()

    # Jumping logic
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_count >= -15:
            neg = 1
            if jump_count < 0:
                neg = -1
            
            p1y -= (jump_count ** 2) * 0.4 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 15

    p1y += yVel

    # Timer
    clock.tick(60)
    CactusXpos = [x - 5 for x in CactusXpos]

    for x in range(len(CactusXpos)):
        if CactusXpos[x] < 0:
            CactusXpos[x] = random.randrange(640, 5000)
            print("reset to ", CactusXpos[x])

    for x, y in zip(CactusXpos, CactusHeights):
        a = pygame.Rect((x, 500-y), (30, 80))
        b = pygame.Rect((p1x, p1y), (30, 30))
        if a.colliderect(b) == True:
            print("Collision")
            gameGoing = True

    # Gravity
    if (p1y + 30) < 500:
        yVel += 0.3   
    else:
        p1y = 470
        yVel = 0

    # Render Section
    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (255, 255, 255), [349, 0], [349, 500], 5)
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 60, 60), 1)

    for x, y in zip(CactusXpos, CactusHeights):
        screen.blit(CactusImg, (x-15, 475-y))

    pygame.display.flip()

pygame.quit()
