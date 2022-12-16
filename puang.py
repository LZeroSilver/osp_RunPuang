import pygame

size = (240,240)

class cpuPuang(pygame.sprite.Sprite):
    def __init__(self, position):
        super(cpuPuang, self).__init__()
        
        images = []
        images.append(pygame.image.load('C1.jpg'))
        images.append(pygame.image.load('C2.jpg'))
        images.append(pygame.image.load('C3.jpg'))
        images.append(pygame.image.load('C4.jpg'))
        images.append(pygame.image.load('C5.jpg'))
        images.append(pygame.image.load('C6.jpg'))
        images.append(pygame.image.load('C7.jpg'))
        images.append(pygame.image.load('C8.jpg'))
        images.append(pygame.image.load('C9.jpg'))
        images.append(pygame.image.load('C10.jpg'))

        self.rect = pygame.Rect(position, size)

        self.images = [pygame.transform.scale(image, size) for image in images]

        self.index = 0
        self.image = images[self.index]

    def update(self):
        self.index += 1
        
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

class ramPuang(pygame.sprite.Sprite):
    def __init__(self, position):
        super(ramPuang, self).__init__()

        images = []
        images.append(pygame.image.load('R1.jpg'))
        images.append(pygame.image.load('R2.jpg'))
        images.append(pygame.image.load('R3.jpg'))
        images.append(pygame.image.load('R4.jpg'))
        images.append(pygame.image.load('R5.jpg'))
        images.append(pygame.image.load('R6.jpg'))
        images.append(pygame.image.load('R7.jpg'))
        images.append(pygame.image.load('R8.jpg'))
        images.append(pygame.image.load('R9.jpg'))
        images.append(pygame.image.load('R10.jpg'))

        self.rect = pygame.Rect(position, size)

        self.images = [pygame.transform.scale(image, size) for image in images]

        self.index = 0
        self.image = images[self.index]

    def update(self):
        self.index += 1
        
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]







