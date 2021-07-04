import pygame

from player.Player import Player

pygame.init()

screen = pygame.display.set_mode((600, 600))
p = Player()
group = pygame.sprite.Group(p)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    group.update()
    screen.fill("white")
    group.draw(screen)
    pygame.display.update()
    clock.tick(10)


if __name__ == '__main__':
    main()
