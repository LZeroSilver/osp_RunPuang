import pygame
import psutil
import time
import button
import puang


#basic setting
pygame.init()

size = [485, 300]
screen = pygame.display.set_mode(size)
gameDisplay = pygame.display.set_mode((size))

title = "Run Puang"
pygame.display.set_caption(title)


ground = pygame.image.load("ground.jpg")
ground = pygame.transform.scale(ground, (485, 300))

f = pygame.font.SysFont("neodgm_pro", 27, True, False)
f2 = pygame.font.SysFont("neodgm_pro", 20, False, True)

clock = pygame.time.Clock()

#icon settings
pygame_icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(pygame_icon)


#button setting
cpuimg = pygame.image.load("cpu.jpg")
ramimg = pygame.image.load("ram.jpg")
exitimg = pygame.image.load("exit.jpg")

cpu_button = button.Button(158, 66, 300, 43, cpuimg)
ram_button = button.Button(158, 66, 300, 117, ramimg)
exit_button = button.Button(158, 66, 300, 191, exitimg)  


#message function
def textmessage(a,b,c):
    if a==0:
        what = "CPU"
    else:
        what = "RAM"
    use = b
    text = f.render("{} usage : {}%".format(what,use), True, (0,0,0))
    now = f2.render("{}".format(c),True,(0,0,0))
    screen.blit(text, (33,35))
    screen.blit(now, (33,55))


# main code
run = True
while run:
    screen.blit(ground, (0,0))
    
    if cpu_button.draw(screen):
        player = puang.cpuPuang(position=(30, 30))
        all_sprites = pygame.sprite.Group(player)
        timenow=time.strftime('%X %x')
        usage = psutil.cpu_percent()
        
        if 0 < usage <=5:
            speed = 5
        elif 5 < usage <= 20:
            speed = 10
        elif 20 < usage <= 40:
            speed = 20
        elif 40 < usage <=60:
            speed = 40
        else:
            speed = 80
            
        for i in range(0,speed*4):
            all_sprites.update()
            all_sprites.draw(screen)
            textmessage(0,usage,timenow)
            pygame.display.update()
            clock.tick(speed)
            
    if ram_button.draw(screen):
        player = puang.ramPuang(position=(30, 30))
        all_sprites = pygame.sprite.Group(player)
        timenow=time.strftime('%X %x')
        usage = psutil.virtual_memory()[2]
        
        if 0 < usage <= 45:
            speed = 5
        elif 45 < usage <=50:
            speed = 10
        elif 50 < usage <= 70:
            speed = 20
        elif 70 < usage <= 85:
            speed = 40
        else:
            speed = 80
            
        for i in range(0, speed*4):
            all_sprites.update()
            all_sprites.draw(screen)
            textmessage(1,usage,timenow)
            pygame.display.update()
            clock.tick(speed)

        
    if exit_button.draw(screen):
        pygame.quit()
        
    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()


