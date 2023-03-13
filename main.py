import pygame

pygame.init()


# Declare variables and lists
screenSize = 800
screen = pygame.display.set_mode([screenSize, screenSize])
clock = pygame.time.Clock()
blockSize = screenSize//3 #Set the size of the grid block
player1 = True
col = 0
row = 0
circlePoses = []
crossPoses = []

mPos = []

# Run until the user asks to quit

running = True

while running:
    

    
    
    
    def DrawGrid():
        
        for x in range(0, screenSize, blockSize):
            for y in range(0, screenSize, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, (0,0,0), rect, 1)
    
    def DrawCircle(col, row):
        x = blockSize * col - blockSize//2
        y = blockSize * row - blockSize//2
        pygame.draw.circle(screen, (0,0,0), (x,y), blockSize//3, 4)
    
    def DrawCross(col, row):
        xLeft = blockSize * col - blockSize//2 - blockSize//3.5
        xRight = blockSize * col - blockSize//2 + blockSize//3.5
        yUp = blockSize * row - blockSize//2 - blockSize//3.5
        yDown = blockSize * row - blockSize//2 + blockSize//3.5
        
        pygame.draw.line(screen, (0,0,0), (xLeft,yUp), (xRight,yDown), 4)
        pygame.draw.line(screen, (0,0,0), (xLeft,yDown), (xRight,yUp), 4)
        
    def ClearSquare(col, row):
        x = blockSize * col - blockSize//2
        y = blockSize * row - blockSize//2
        pygame.draw.circle(screen, (255,255,255), (x,y), blockSize//2.25, 0)
        
        
    # Fill the background with white and draw the grid

    screen.fill((255, 255, 255))
    DrawGrid()
    
    if len(circlePoses) > 3:
        circlePoses.remove(circlePoses[0])
    if len(crossPoses) > 3:
        crossPoses.remove(crossPoses[0])
        
    for circlePos in circlePoses:
        DrawCircle(circlePos[0], circlePos[1])
    for crossPos in crossPoses:
        DrawCross(crossPos[0], crossPos[1])
    
        
    
        
    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            
            
            mPos = pygame.mouse.get_pos()
            if mPos[0] < blockSize:
                col = 1
            elif mPos[0] > blockSize and mPos[0] <  blockSize * 2:
                col = 2
            elif mPos[0] > blockSize * 2:
                col = 3
            
            
            if mPos[1] < blockSize:
                row = 1
            elif mPos[1] > blockSize and mPos[1] <  blockSize * 2:
                row = 2
            elif mPos[1] > blockSize * 2:
                row = 3
                
                
            if player1 == True:
                DrawCircle(col, row)
                circlePoses.append((col,row))
                player1 = False
            else:
                DrawCross(col, row)   
                crossPoses.append((col,row))
                player1 = True
    
            
                
                


    


    
   
   

    # Flip the display

    pygame.display.flip()
    clock.tick(60)


# Done! Time to quit.

pygame.quit()