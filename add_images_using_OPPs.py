#import pygame modile

import pygame


#create a window
pygame.init()

    #window size
        #window width
SCREEN_WIDTH = 800
        #window height
SCREEN_HEIGHT = int(SCREEN_WIDTH *0.8)

   #set screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

   #coption of Window
pygame.display.set_caption('Shooter')



#create a class for all soldier
class my_soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        #image loction

        img = pygame.image.load('img/player/Idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        
    #create a fucnction for drow the soldier
    def s_draw(self):
        screen.blit(self.image, self.rect)
  

#create a soldier adding width, Height and scale where you want to add
    #in here soldier means we use above soldier class
        
player = my_soldier(200, 200, 3)
player2 = my_soldier(400, 200, 3)

   #close the screen when we click close button
run = True
while run:

    #display player, player2 using s_draw function
    player.s_draw()
    player2.s_draw()
    
    
    
    
    for event in pygame.event.get():
            #quit game
        if event.type == pygame.QUIT:
            run = False

    #you must write this otherwise not display anything
    #this is for update the program        
    pygame.display.update()

#quite Program
pygame.quit()
