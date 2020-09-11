from utilitarios import utilitarios_forma as forma
import pygame
import numpy as np
import time

pygame.init()

screem = pygame.display.set_mode((forma.alto ,forma.ancho))

pauseExect = False

screem.fill(forma.bg)
#Estados de las celadas , viva = 1; muerta = 0
gameState = np.zeros((forma.nxC,forma.nyC))
gameState[5,6]=1
gameState[5,7]=1
gameState[5,8]=1
while True:

    newGameState = np.copy(gameState)

    screem.fill(forma.bg)
    time.sleep(0.3)
    events = pygame.event.get() 

    for event in events:
        # detectando si se pulso alguna tecla del teclado
        if event.type == pygame.KEYDOWN :
            pauseExect = not pauseExect
        # detectando si se preciona alguno boton del raton
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX,celY = int(np.floor(posX / forma.dimCW)), int(np.floor(posY/ forma.dimCH)) 
            newGameState[celX,celY] = 1

    for y in range(0,forma.nxC):
        
        for x in range(0,forma.nyC):
            if not pauseExect:
                n_neigh = forma.numeroCeldas(gameState,x,y)
                celda = gameState[x,y] 
                # Regla 1
                if celda  == 0 and n_neigh == 3 :
                    newGameState[x,y] = 1
                # Regla 2
                elif celda == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x,y] = 0

            poly = forma.polygono(x,y)

            #dibujando la celda para cada par de x e y
            if newGameState[x,y] == 0 :
                pygame.draw.polygon(screem,(128,128,128),poly,1)
            else:
                pygame.draw.polygon(screem,(255,255,255),poly,0)
            
    #Actualizamos el estado del juego
    gameState = np.copy(newGameState)
    
    pygame.display.flip()