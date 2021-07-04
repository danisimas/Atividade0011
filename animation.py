import pygame



pygame.init()

walking_left = [pygame.image.load('Images/L1.png'), pygame.image.load('Images/L2.png'),
                pygame.image.load('Images/L3.png'), pygame.image.load('Images/L4.png'),
                pygame.image.load('Images/L5.png'), pygame.image.load('Images/L6.png'),
                pygame.image.load('Images/L7.png'), pygame.image.load('Images/L8.png'),
                pygame.image.load('Images/L9.png'), pygame.image.load('Images/L10.png')]

walking_right = [pygame.image.load('Images/R1.png'), pygame.image.load('Images/R2.png'),
                 pygame.image.load('Images/R3.png'), pygame.image.load('Images/R4.png'),
                 pygame.image.load('Images/R5.png'), pygame.image.load('Images/R6.png'),
                 pygame.image.load('Images/R7.png'), pygame.image.load('Images/R8.png'),
                 pygame.image.load('Images/R9.png'), pygame.image.load('Images/R10.png')]

bg = pygame.image.load('Images/bg.png')
# char = pygame.image.load('')
x = 50
y = 400
width = 40
height = 60


isJump = False
jumpCount = 10

vel = 5

screen = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()

left = False
right = False

walkCount = 0


def redrawGameWindow():
    global walkCount
    screen.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        screen.blit(walking_left[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        screen.blit(walking_right[walkCount // 3], (x, y))
        walkCount += 1
    else:
        # win.blit(char, (x, y))
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

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
            left = True
            right = False

        elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
            x += vel
            left = False
            right = True

        else:
            left = False
            right = False
            walkCount = 0

        if not (isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                left = False
                right = False
                walkCount = 0
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else:
                jumpCount = 10
                isJump = False

        redrawGameWindow()
pygame.quit()
