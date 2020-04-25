from utilitarios import utilitarios_forma as forma
import pygame
import numpy as np

screen = pygame.display.set_mode((forma.alto,forma.ancho))
screen.fill(forma.bg)

gameState = np.zeros((forma.nxC, forma.nyC))

while True:
    for y in range(0, forma.nxC) :
        for x in range(0, forma.nyC) :

            newGameState = np.copy(gameState)

            n_neigh =   gameState[(x - 1) % forma.nxC, (y-1)      % forma.nyC] +    \
                        gameState[(x)     % forma.nxC, (y-1)      % forma.nyC] +    \
                        gameState[(x + 1) % forma.nxC, (y-1)      % forma.nyC] +    \
                        gameState[(x - 1) % forma.nxC, (y)        % forma.nyC] +    \ 
                        gameState[(x + 1) % forma.nxC, (y)        % forma.nyC] +    \
                        gameState[(x - 1) % forma.nxC, (y + 1)    % forma.nyC] +    \
                        gameState[(x)     % forma.nxC, (y + 1)    % forma.nyC] +    \
                        gameState[(x +1 ) % forma.nxC, (y + 1)    % forma.nyC]
            
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1
            
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0

            poly  = forma.polygono(x,y)
            
            if newGameState[x, y]

            pygame.draw.polygon(screen, (128,128,128), poly, 1)

    pygame.display.flip()