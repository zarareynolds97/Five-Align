import pygame
import random
import time
import math

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height]) 

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PINK = (250,55,188)
ORANGE = (255,153,10)
YELLOW = (255,255,10) 

def random_color():
    colors = [RED, GREEN, BLUE, PINK, ORANGE, YELLOW]
    return random.choice(colors) 

screen.fill(WHITE)

blocks = {} 

def starterBlocks():
    for i in range(6): 
        A = random.randint(0,600)
        finalA = int(round(A/25.0)) * 25
        B = random.randint(0,600)
        finalB = int(round(B/25.0)) * 25
        blocks.append(pygame.draw.rect(screen, random_color(), (finalA, finalB, 25,25), 0))
        pygame.display.update()

#i want to be able to call another 3 random pieces up -- need to be a function to call
def newRandom():
    #BUT not in the points where there are already stuff - HOW TO DETECT THESE THINGS 
    for i in range(3):
        A = random.randint(0,600)
        finalA = int(round(A/25.0)) * 25
        B = random.randint(0,600)
        finalB = int(round(B/25.0)) * 25
        newRect = pygame.draw.rect(screen, random_color(), (finalA, finalB, 25, 25), 0)
    


def determine_mouseOver(valx, valy):
    if blocks.collidepoint(valx, valy): #myRectangle ERROR name not defined 
        return True
    else:
        return False

     

def main():
    starterBlocks() 
    
    running = True 
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN: 
                finalX, finalY = pygame.mouse.get_pos()
            
                
                mouseOver = determine_mouseOver(finalX, finalY)
                if mouseOver == True:
                    a = int(round(finalX/25.0)) * 25
                    b = int(round(finalY/25.0)) * 25
                    pygame.draw.rect(screen, random_color(), (a, b, 25, 25), 0)
                    newRandom() 
                    
                elif mouseOver == False:
                    a = int(round(finalX/25.0)) * 25
                    b = int(round(finalY/25.0)) * 25
                    pygame.draw.rect(screen, BLACK, (a, b, 25,25), 0) 
                
            

                #pygame.draw.rect(screen, random_color(), (finalX, finalY, 25, 25), 0) 
                
                pygame.display.update()

                

                
    #why does it only affect for one rectangle? I may need to change to a loop 
      


      
main() 
