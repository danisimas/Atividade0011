import pygame

pygame.init()

walking_left = [pygame.image.load('Images/L1.png'), pygame.image.load('Images/L2.png'),
                pygame.image.load('Images/L3.png')]

walking_right = [pygame.image.load('Images/R1.png'), pygame.image.load('Images/R2.png'),
                 pygame.image.load('Images/R3.png')]

jumper = [pygame.image.load("Images/jump.png"), pygame.image.load('Images/idle.png')]


char = pygame.image.load('Images/idle.png')
x = 50
y = 400
width = 40
height = 60


isJump = False
jumpCount = 10

vel = 5

screen = pygame.display.set_mode((1000, 1000))

clock = pygame.time.Clock()

left = False
right = False
jump = False

walkCount = 0


def redrawGameWindow():
    global walkCount
    screen.fill("Black")

    if walkCount + 1 >= 10:
        walkCount = 0

    if left:
        screen.blit(walking_left[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        screen.blit(walking_right[walkCount // 3], (x, y))
        walkCount += 1

    elif jump:
        screen.blit(jumper[walkCount // 3], (x, y))
        walkCount += 1

    else:
        screen.blit(char, (x, y))
        walkCount = 0

    pygame.display.update()


run = True


while run:
    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= vel
            left = True
            right = False
            jump = False

        elif keys[pygame.K_RIGHT]:
            x += vel
            left = False
            right = True
            jump = False

        else:
            jump = False
            left = False
            right = False
            walkCount = 0

        if not isJump:
            if keys[pygame.K_SPACE]:
                isJump = True
                jump = False
                left = False
                right = False
                walkCount = 0
        else:
            jump = True
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else:
                jumpCount = 10
                isJump = False
                jump = False

        redrawGameWindow()
pygame.quit()
