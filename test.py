import pygame
import psutil

a = psutil.cpu_percent(2)
print(a)
c=float(a/50)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

pygame.init()


SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame Sprite")

 

clock = pygame.time.Clock()

FPS = 60*c

 

BACKGROUND_COLOR = pygame.Color('white')

 

class AnimatedSprite(pygame.sprite.Sprite):

 

    def __init__(self, position):

        super(AnimatedSprite, self).__init__()
        size = (300, 400)
     
        images = []
        images.append(pygame.image.load('PUANG_1.png'))
        images.append(pygame.image.load('PUANG_2.png'))
        images.append(pygame.image.load('PUANG_3.png'))
        images.append(pygame.image.load('PUANG_4.png'))

        self.rect = pygame.Rect(position, size)
        self.images = [pygame.transform.scale(image, size) for image in images]
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.


    def update(self):
        self.index += 1

 

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]


def main():
    player = AnimatedSprite(position=(100, 8))
    all_sprites = pygame.sprite.Group(player)  
   
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        all_sprites.update()
        SCREEN.fill(BACKGROUND_COLOR)
        all_sprites.draw(SCREEN)
        pygame.display.update()

        clock.tick(FPS)

 

if __name__ == '__main__':
    main()
