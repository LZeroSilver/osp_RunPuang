import pygame

class Puang(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Puang, self).__init__()
        size = (320, 320)

        images = []
        images.append(pygame.image.load('1.jpg'))
        images.append(pygame.image.load('2.jpg'))
        images.append(pygame.image.load('3.jpg'))
        images.append(pygame.image.load('4.jpg'))
        images.append(pygame.image.load('5.jpg'))
        images.append(pygame.image.load('6.jpg'))
        images.append(pygame.image.load('7.jpg'))
        images.append(pygame.image.load('8.jpg'))
        images.append(pygame.image.load('9.jpg'))
        images.append(pygame.image.load('10.jpg'))

        self.rect = pygame.Rect(position, size)

        self.images = [pygame.transform.scale(image, size) for image in images]

        self.index = 0
        self.image = images[self.index]

    def update(self):
        self.index += 1
        
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]







