alto = 500
ancho = 500 
bg = 25,25,25

#numero de  celdas
nxC,nyC = 25,25

#dimenciones de la celda
dimCW = ancho / nxC
dimCH = alto / nyC

#funcion para crear el poligono de cada celada a dibujar
def polygono(x,y):
     return  [
                ((x)        * dimCW, y        * dimCH),
                ((x + 1)    * dimCW, y        * dimCH),
                ((x + 1)    * dimCW, (y + 1 ) * dimCH),
                ((x)        * dimCW, (y + 1 ) * dimCH)  
            ]


#calculamos numero de vecinos de las celdas
def numeroCeldas( gameState,x,y):
    return      gameState[(x - 1) % nxC, (y-1)      % nyC] +    \
                gameState[(x)     % nxC, (y-1)      % nyC] +    \
                gameState[(x + 1) % nxC, (y-1)      % nyC] +    \
                gameState[(x - 1) % nxC, (y)        % nyC] +    \
                gameState[(x + 1) % nxC, (y)        % nyC] +    \
                gameState[(x - 1) % nxC, (y + 1)    % nyC] +    \
                gameState[(x)     % nxC, (y + 1)    % nyC] +    \
                gameState[(x +1 ) % nxC, (y + 1)    % nyC]


                

