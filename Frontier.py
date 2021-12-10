import pygame
import random
import math
pygame.init()

x = 1440
y = 785

screen = pygame.display.set_mode([x, y])
screen.fill([255, 255, 255])

pygame.display.set_caption('Frontier')
clock = pygame.time.Clock()

bul_sound = pygame.mixer.Sound("Orz-Zap.wav")
left = x/2
top = y/2
fps = 60
i = 0
prt_mouse = [0, 0]
act_mouse = [0, 0]

enemy_img = [pygame.image.load('Astroid.png')]
enemy_wait = fps * random.randint(3, 10)
enemy = []
enemy_hitbox = None

life = 1

font = pygame.font.Font('CaviarDreams.ttf', 115)
text = font.render(str(life), True, (255, 255, 255), (0, 0, 0))
textRect = text.get_rect()
textRect.center = (x/2, y/2)

ship_img = [pygame.image.load('Ship1.png'), pygame.image.load('Ship2.png')]
img = ship_img[0]
ship_hitbox = pygame.Rect(prt_mouse[0], prt_mouse[1], 65, 25)

background = pygame.image.load('Background.jpeg')

power_img = [pygame.image.load('Powerstone/Power1.png'), pygame.image.load('Powerstone/Power2.png'), pygame.image.load('Powerstone/Power3.png'),
             pygame.image.load('Powerstone/Power4.png'), pygame.image.load('Powerstone/Power5.png'), pygame.image.load('Powerstone/Power6.png'),
             pygame.image.load('Powerstone/Power7.png'), pygame.image.load('Powerstone/Power8.png'), pygame.image.load('Powerstone/Power9.png'),
             pygame.image.load('Powerstone/Power10.png'), pygame.image.load('Powerstone/Power11.png'), pygame.image.load('Powerstone/Power12.png')]

image = power_img[0]
power_y = random.randint(50, y - 50)
power_x = x
power_hitbox = pygame.Rect(power_x, power_y, 20, 20)

running = True

l = 0
j = 0
h = 0
bul = []
bul_hitbox = bul

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    ship_hitbox = pygame.Rect(prt_mouse[0], prt_mouse[1], 65, 25)
    power_hitbox = pygame.Rect(power_x, power_y, 20, 20)

    act_mouse = pygame.mouse.get_pos()
    xdif = act_mouse[0] - prt_mouse[0] - 50
    ydif = act_mouse[1] - prt_mouse[1] - 20

    prt_mouse[0] += math.ceil(xdif/(fps/2))
    prt_mouse[1] += math.ceil(ydif/(fps/2))

    if i % 20 == 0:
        if i % 40 == 0:
            img = ship_img[0]
        else:
            img = ship_img[1]

    if i % 4 == 0:
        image = power_img[l]
        l += 1
        if l == 12:
            l = 0

    screen.blit(background, (math.floor(h), 0))
    screen.blit(img, prt_mouse)
    h -= 0.3

    if i % enemy_wait == 0:
        enemy.append([x, random.randint(150, y - 150)])
        enemy_wait = fps/4 * random.randint(1, 5)

    m = 0
    for k in enemy:
        k[0] -= 5
        screen.blit(pygame.transform.rotate(enemy_img[0], 2), k)
        enemy_hitbox = pygame.Rect(k[0] + 145, k[1] + 40, 100, 100)

        if ship_hitbox.colliderect(enemy_hitbox):
            life -= 3
            prt_mouse = [0, 0]

        j = 0
        for n in bul:
            bul_hitbox = pygame.Rect(bul[j][0], bul[j][1], 3, 3)
            if enemy_hitbox.colliderect(bul_hitbox):
                bul.pop(j)
                enemy.pop(m)

            j += 1

        if k[0] < 0:
            life -= 3
            enemy.pop(m)
            # elif enemy[j][1] > y:
            #     enemy.pop(j)

        m += 1

    j = 0

    if i % int(fps/3) == 0:
        bul.append([prt_mouse[0] + 55, prt_mouse[1] + random.randint(12, 32)])
        pygame.mixer.Sound.play(bul_sound)

    for k in bul:
        bul[j][0] += 30
        pygame.draw.circle(screen, [255, 0, 255], bul[j], 6)
        bul_hitbox = pygame.Rect(bul[j][0], bul[j][1], 3, 3)

        if bul[j][0] > x:
            bul.pop(j)
        elif bul[j][1] > y:
            bul.pop(j)

        j += 1

    i += 1

    if power_x < -50 or ship_hitbox.colliderect(power_hitbox):
        if ship_hitbox.colliderect(power_hitbox):
            life += 1

        power_x = x
        power_y = random.randint(50, y-50)

    power_x -= 2
    screen.blit(image, (power_x, power_y))

    if life < 1:
        running = False

    text = font.render(str(life), True, [255, 255, 255], [0, 0, 0])
    screen.blit(text, (0, 0))

    print(clock.tick())
    pygame.display.update()
    clock.tick(fps)