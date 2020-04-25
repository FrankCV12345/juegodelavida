alto = 1000
ancho = 2000 
bg = 25,25,25

nxC,nyC = 25,25

dimCW = ancho / nxC
dimCH = alto / nyC

def polygono(x,y):
     return  [
                ((x)        * dimCW, y        * dimCH),
                ((x + 1)    * dimCW, y        * dimCH),
                ((x + 1)    * dimCW, (y + 1 ) * dimCH),
                ((x)        * dimCW, (y + 1 ) * dimCH)  
            ]




