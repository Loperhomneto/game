import pygame
pygame.init()

x = 1360
y = 816

screen = pygame.display.set_mode([x, y])
screen.fill([0, 0, 0])

class PongSticks:
    def __init__(self, key_up, key_down, left):
        self.key_up = key_up
        self.key_down = key_down
        self.if_up_pressed = False
        self.if_down_pressed = False
        self.left = left
        self.top = 400
        self.rectan = pygame.Rect([self.left, self.top, 7, 75])

    def detect(self):
        if event.type == pygame.KEYDOWN and event.key == self.key_up:
            self.if_up_pressed = True
        elif event.type == pygame.KEYDOWN and event.key == self.key_down:
            self.if_down_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == self.key_up:
                self.if_up_pressed = False
            elif event.key == self.key_down:
                self.if_down_pressed = False
        elif event.type == pygame.KEYUP:
            self.if_up_pressed = False
            self.if_down_pressed = False

    def action(self):
        if self.if_up_pressed:
            self.top = self.top - 3

        elif self.if_down_pressed:
            self.top = self.top + 3
        self.rectan = pygame.Rect([self.left, self.top, 7, 75])
        pygame.draw.rect(screen, [255, 255, 255], [self.left, self.top, 7, 75])


border1 = pygame.Rect([0, 0, x, 5])
border2 = pygame.Rect([0, 0, 5, x])
border3 = pygame.Rect([0, y - 5, x, 5])
border4 = pygame.Rect([x - 5, 0, 5, y])

pong_stick_one = PongSticks(pygame.K_UP, pygame.K_DOWN, x-20)
pong_stick_two = PongSticks(pygame.K_w, pygame.K_s, 13)

pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

win_left = 0
win_right = 0

font = pygame.font.Font('CaviarDreams.ttf', 115)
text = font.render(str(win_right), True, (255, 255, 255), (0, 0, 0))
textRect = text.get_rect()
textRect.center = (x/2, y/2)

left = x-50
top = y/2
ball_direction_vertical = 1
ball_direction_horizontal = 1
ball = pygame.Rect([left, top, 4, 4])
if_up_pressed = False
if_down_pressed = False
running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        pong_stick_one.detect()
        pong_stick_two.detect()

    ball.colliderect(border4)
    ball_collide_vertical = ball.colliderect(pong_stick_one.rectan) or ball.colliderect(pong_stick_two.rectan)
    ball_collide_horizontal = ball.colliderect(border1) or ball.colliderect(border3)

    if ball_collide_vertical:
        ball_direction_vertical += 1
    elif ball_collide_horizontal:
        ball_direction_horizontal += 1

    if ball.colliderect(border2) or ball.colliderect(border4):
        if ball.colliderect(border2):
            left = x-50
            top = y/2
            win_right += 1
        else:
            left = 50
            top = y/2
            win_left += 1

        ball = pygame.Rect([left, top, 4, 4])
        pygame.time.delay(2000)

    if ball_direction_vertical % 2:
        left -= 4
    else:
        left += 4

    if ball_direction_horizontal % 2:
        top -= 4
    else:
        top += 4

    screen.fill([0, 0, 0])

    text = font.render(str(win_left), True, [255, 255, 255], [0, 0, 0])
    screen.blit(text, (300, 0))
    text = font.render(str(win_right), True, [255, 255, 255], [0, 0, 0])
    screen.blit(text, (x-370, 0))

    pong_stick_one.action()
    pong_stick_two.action()

    ball = pygame.Rect([left, top, 4, 4])
    pygame.draw.rect(screen, [255, 255, 255], ball)

    pygame.draw.rect(screen, [255, 255, 255], border1)
    pygame.draw.rect(screen, [255, 255, 255], border2)
    pygame.draw.rect(screen, [255, 255, 255], border3)
    pygame.draw.rect(screen, [255, 255, 255], border4)

    pygame.display.update()
    clock.tick(60)
    # print(clock.get_time())

pygame.quit()
quit()