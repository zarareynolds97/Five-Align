import pygame, random, time, math 

screen_width = 400
screen_height = 400
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



def starterBlocks():
    for i in range(6): 
        A = random.randint(0,screen_width)
        finalA = int(round(A/25.0)) * 25
        B = random.randint(0,screen_height)
        finalB = int(round(B/25.0)) * 25
        global rectangle
        rectangle = pygame.draw.rect(screen, random_color(), (finalA, finalB, 25,25), 0)
        pygame.display.update()

#i want to be able to call another 3 random pieces up -- need to be a function to call
def newRandom():
    #BUT not in the points where there are already stuff - HOW TO DETECT THESE THINGS 
    for i in range(3):
        A = random.randint(0,screen_width)
        finalA = int(round(A/25.0)) * 25
        B = random.randint(0,screen_height)
        finalB = int(round(B/25.0)) * 25
        newRect = pygame.draw.rect(screen, random_color(), (finalA, finalB, 25, 25), 0)





     

def main():
    starterBlocks() #calls the function which places five blocks on screen at start of programme 
    
    running = True 
    while running: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

                
                
            if event.type == pygame.MOUSEBUTTONDOWN: 
                finalX, finalY = pygame.mouse.get_pos()
                
                if rectangle.collidepoint(finalX, finalY):
                    a = int(round(finalX/25.0)) * 25
                    b = int(round(finalY/25.0)) * 25
                    pygame.draw.rect(screen, random_color(), (a, b, 25, 25), 0)
                    newRandom() 
                    
                else:
                    a = int(round(finalX/25.0)) * 25
                    b = int(round(finalY/25.0)) * 25
                    pygame.draw.rect(screen, BLACK, (a, b, 25,25), 0) 
                
            

                #pygame.draw.rect(screen, random_color(), (finalX, finalY, 25, 25), 0) 
                
                pygame.display.update()

                

                

      


      
main() 
