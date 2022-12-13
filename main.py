import pygame
import psutil
import time
import button

pygame.init()
size = [360, 720]
screen = pygame.display.set_mode(size)
gameDisplay = pygame.display.set_mode((size))
title = "Run Puang"
pygame.display.set_caption(title)
white = (255,255,255)
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial",30, True, True)
font2 = pygame.font.SysFont("arial",20,False, False)

####icon####
pygame_icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(pygame_icon)
############

######## 버튼 설정 시작 ########
cpuimg = pygame.image.load("cpu.jpg")
cpuimg = pygame.transform.scale(cpuimg, (150, 150))
ramimg = pygame.image.load("ram.jpg")
ramimg = pygame.transform.scale(ramimg, (150, 150))
exitimg = pygame.image.load("exit.jpg")
exitimg = pygame.transform.scale(exitimg, (320, 80))

cpu_button = button.Button(20, 440, cpuimg, 1.0)
ram_button = button.Button(190, 440, ramimg, 1.0)
exit_button = button.Button(20, 600, exitimg, 1.0)  

######## 버튼 설정 끝  ########
def quitgame():
    pygame.quit()
######## 푸앙이  설정 시작 ########
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
        images.append(pygame.image.load('0.jpg'))

        self.rect = pygame.Rect(position, size)

        self.images = [pygame.transform.scale(image, size) for image in images]

        self.index = 0
        self.image = images[self.index]

    def update(self):
        self.index += 1
        
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]


def cpuRun():
    player = Puang(position=(20, 30))
    all_sprites = pygame.sprite.Group(player)
    timenow=time.strftime('%x %X')
    FPS = psutil.cpu_percent()
    
    if 0 < FPS <=5:
        speed = 5
    elif 5 < FPS <= 20:
        speed = 10
    elif 20 < FPS <= 40:
        speed = 20
    elif 40 < FPS <=60:
        speed = 40
    else:
        speed = 80
        
    text = font.render("CPU usage : {}%".format(FPS), True, (0,0,0))
    now = font2.render("time: {}".format(timenow),True,(0,0,0))
    screen.blit(text, (30,375))
    screen.blit(now, (30,410))
    for i in range(0,speed*4):
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.update()
        clock.tick(speed)

def ramRun():
    player = Puang(position=(20, 30))
    all_sprites = pygame.sprite.Group(player)
    timenow=time.strftime('%x %X')
    FPS = psutil.virtual_memory()[2]
    
    if 0 < FPS <= 45:
        speed = 5
    elif 45 < FPS <=50:
        speed = 10
    elif 50 < FPS <= 70:
        speed = 20
    elif 70 < FPS <= 85:
        speed = 40
    else:
        speed = 80
        
    text = font.render("RAM usage : {}%".format(FPS), True, (0,0,0))
    now = font2.render("time: {}".format(timenow),True,(0,0,0))
    screen.blit(text, (30,375))
    screen.blit(now, (30,410))
    for i in range(0, speed*4):
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.update()
        clock.tick(speed)

######## 푸앙이  설정 끝 ########

run = True
while run:

    screen.fill(white)
    if cpu_button.draw(screen):
        cpuRun()
    if ram_button.draw(screen):
        ramRun()
    if exit_button.draw(screen):
        quitgame()
        
            
    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()


