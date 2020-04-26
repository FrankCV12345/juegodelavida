from utilitarios import utilitarios_forma as forma
import pygame
import numpy as np
import time
pygame.init()

screem = pygame.display.set_mode((forma.alto ,forma.ancho))

screem.fill(forma.bg)
#Estados de las celadas , viva = 1; muerta = 0
gameState = np.zeros((forma.nxC,forma.nyC))
gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1
while True:

    newGameState = np.copy(gameState)
    #yo lo agregue
    pygame.event.get() 

    screem.fill(forma.bg)
    time.sleep(0.2)
    for y in range(0,forma.nxC):
        
        for x in range(0,forma.nyC):
            n_neigh = forma.numeroCeldas(gameState,x,y)
            celda = gameState[x,y] 
            # Regla 1
            if celda  == 0 and n_neigh == 3 :
                newGameState[x,y] = 1
            elif celda == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x,y] = 0

            poly = forma.polygono(x,y)

            #dibujando la celda para cada par de x e y
            if newGameState[x,y] == 0 :
                pygame.draw.polygon(screem,(128,128,128),poly,1)
            else:
                pygame.draw.polygon(screem,(255,255,255),poly,1)
            
    #Actualizamos el estado del juego
    gameState = np.copy(newGameState)
    
    pygame.display.flip()