import pygame


class Player (pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.images = []
        self.images.append(pygame.image.load("Images/walk1.png"))
        self.images.append(pygame.image.load("Images/walk2.png"))
        self.images.append(pygame.image.load("Images/walk3.png"))
        self.images.append(pygame.image.load("Images/walk4.png"))
        self.images.append(pygame.image.load("Images/walk5.png"))
        self.images.append(pygame.image.load("Images/walk6.png"))
        self.images.append(pygame.image.load("Images/walk7.png"))
        self.images.append(pygame.image.load("Images/walk8.png"))
        self.images.append(pygame.image.load("Images/walk9.png"))
        self.images.append(pygame.image.load("Images/walk10.png"))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
