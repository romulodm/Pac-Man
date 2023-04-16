from graphics import *
from Codigos.mapa import *
from Codigos.a_star import *

from Classes.classpacman import *

#FICA TENTANDO INTERCEPTAR, BASEADO NO QUADRANTE DO PACMAN:
class Clyde:
    def __init__(self, win, pacman):
        self.win = win
        self.pacman = pacman

        self.spriteClyde = "Sprites/Clyde/Clyde-U.png"
        
        self.Clyde = Image(Point(250, 290), self.spriteClyde)
        self.posiBlinky = ""

        self.posiColunaClyde = 12
        self.posiLinhaClyde = 14

        self.move = None

        self.truePositions = getPositions()

        self.MovesClyde = [""]

        self.SpritesClyde = ["Sprites/Clyde/Clyde-R.png","Sprites/Clyde/Clyde-L.png",
                              "Sprites/Clyde/Clyde-U.png","Sprites/Clyde/Clyde-D.png",]

        self.spritesVulneravel = ["Sprites/Scared/Fear-2.png","Sprites/Scared/Fear-1.png",]
        self.modeScared = False
 
        self.quadrantePac = None
        self.movementPac = None

    def drawClyde(self):
        return self.Clyde.draw(self.win)

    def undrawClyde(self):
        return self.Clyde.undraw()

    def restartClyde(self):
        self.posiColunaClyde = 12
        self.posiLinhaClyde = 14

        self.modeScared = False

        self.Clyde.undraw()
        self.Clyde = Image(Point(250, 290), self.spriteClyde)
        self.Clyde.draw(self.win)

        self.getMovesClyde()

    def getMovesClyde(self):
        self.quadrantePac = self.pacman.getQuadrante()
        self.movementPac = self.pacman.getMovement()

        if self.movementPac == "None":
            if self.posiColunaClyde == 14 and self.posiLinhaClyde == 11:
               self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,14,17)
            else:
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,14,11)
            
        if self.quadrantePac == 1:
            if self.movementPac == "Right":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,18,5)
            if self.movementPac == "Left":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,1,4)
            if self.movementPac == "Up":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,6,1)
            if self.movementPac == "Down":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,6,11)
        if self.quadrantePac == 2:
            if self.movementPac == "Right":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,26,4)
            if self.movementPac == "Left":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,9,5)
            if self.movementPac == "Up":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,21,1)
            if self.movementPac == "Down":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,21,11)
        if self.quadrantePac == 3:
            if self.movementPac == "Right":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,18,14)
            if self.movementPac == "Left":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,9,14)
            if self.movementPac == "Up":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,14,11)
            if self.movementPac == "Down":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,14,17)
        if self.quadrantePac == 4:
            if self.movementPac == "Right":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,18,23)
            if self.movementPac == "Left":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,3,23)
            if self.movementPac == "Up":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,6,20)
            if self.movementPac == "Down":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,12,29)    
        if self.quadrantePac == 5:
            if self.movementPac == "Right":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,24,23)
            if self.movementPac == "Left":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,6,23)
            if self.movementPac == "Up":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,21,20)
            if self.movementPac == "Down":
                self.MovesClyde = a_star(self.posiColunaClyde, self.posiLinhaClyde,16,29)

    def getMoves(self):
        return self.MovesClyde   

    def moveClyde(self):

        if len(self.MovesClyde) >= 1 and self.MovesClyde[0] != "":
            x_clyde = self.MovesClyde[0][0]
            y_clyde = self.MovesClyde[0][1]

            if x_clyde > 0 and y_clyde == 0:
                self.spriteClyde = self.SpritesClyde[0]
            if x_clyde < 0 and y_clyde == 0:
                self.spriteClyde = self.SpritesClyde[1]
            if x_clyde == 0 and y_clyde < 0:
                self.spriteClyde = self.SpritesClyde[2]
            if x_clyde == 0 and y_clyde > 0:
                self.spriteClyde = self.SpritesClyde[3]

            self.Clyde.move(x_clyde, y_clyde)
            self.redrawClyde()

            del(self.MovesClyde[0])

        if len(self.MovesClyde) == 0:
            self.getMovesClyde()

    def redrawClyde(self):

        if self.modeScared == True:
            self.spriteClyde = self.spritesVulneravel[self.indiceVulneravel]

        self.Clyde.undraw()
        self.Clyde = Image(self.Clyde.getAnchor(), self.spriteClyde)
        self.Clyde.draw(self.win)

        self.getMatrizPosition()  
    
    def getMatrizPosition(self):
        self.posiClyde = f"{self.Clyde.getAnchor().getX()},{self.Clyde.getAnchor().getY()}"
        if self.posiClyde in self.truePositions:
            self.PosiMatriz = self.truePositions[self.posiClyde]
            getPosi = self.pegaIndice()
            self.posiColunaClyde = int(getPosi[1])
            self.posiLinhaClyde = int(getPosi[0])

        #return self.posiColunaClyde, self.posiLinhaClyde

    def getPosition(self):
        #return self.Clyde.getAnchor()
        return f"{self.Clyde.getAnchor().getX()},{self.Clyde.getAnchor().getY()}"

    def getClydeX(self):
        return self.Clyde.getAnchor().getX()

    def getClydeY(self):
        return self.Clyde.getAnchor().getY()

    def pegaIndice(self):        
        prim_indice = ""
        cont = 0
        while cont < 6:
            if self.PosiMatriz[cont] == "[":
                prim_indice += self.PosiMatriz[cont+1]
                if self.PosiMatriz[cont+2] != "]":
                    prim_indice += self.PosiMatriz[cont+2]
            cont += 1

        seg_indice = ""
        while cont < len(self.PosiMatriz):
            if self.PosiMatriz[cont] == "[":
                seg_indice += self.PosiMatriz[cont+1]
                if self.PosiMatriz[cont+2] != "]":
                    seg_indice += self.PosiMatriz[cont+2]
            cont += 1

        return([prim_indice, seg_indice])


    def scaredMode(self, bool):

        if bool == True:
            self.modeScared = True

            self.indiceVulneravel = 0

            self.Clyde.undraw()
            self.Clyde = Image(self.Clyde.getAnchor(), self.spritesVulneravel[self.indiceVulneravel])
            self.Clyde.draw(self.win)

        elif bool == None:
            self.indiceVulneravel = 1
            
        else:
            self.modeScared = False
            self.redrawClyde()

    def getMode(self):
        return self.modeScared



#####
#FICA SEGUINDO O PACMAN:
class Blinky:
    def __init__(self, win, pacman):

        self.win = win
        self.pacman = pacman

        self.spriteBlinky = "Sprites/Blinky/Blinky-U.png"
        
        self.Blinky = Image(Point(270, 290), self.spriteBlinky)
        self.posiBlinky = ""

        self.posiColunaBlinky = 13
        self.posiLinhaBlinky = 14

        self.move = None

        self.truePositions = getPositions()

        self.MovesBlinky = [""]

        self.SpritesBlinky = ["Sprites/Blinky/Blinky-R.png","Sprites/Blinky/Blinky-L.png",
                              "Sprites/Blinky/Blinky-U.png","Sprites/Blinky/Blinky-D.png",]

        self.spritesVulneravel = ["Sprites/Scared/Fear-2.png","Sprites/Scared/Fear-1.png",]
        self.modeScared = False
 
        self.posiColunaPac = None
        self.posiLinhaPac = None

    def drawBlinky(self):
        return self.Blinky.draw(self.win)

    def undrawBlinky(self):
        return self.Blinky.undraw()

    def restartBlinky(self):
        self.posiColunaBlinky = 13
        self.posiLinhaBlinky = 14

        self.modeScared = False

        self.Blinky.undraw()
        self.Blinky = Image(Point(270, 290), self.spriteBlinky)
        self.Blinky.draw(self.win)

        self.getMovesBlinky()

    def getMovesBlinky(self):
        self.getPosisPac()
        self.MovesBlinky = a_star(self.posiColunaBlinky, self.posiLinhaBlinky, self.posiColunaPac, self.posiLinhaPac)
        if len(self.MovesBlinky) == 0:
            self.MovesBlinky = a_star(self.posiColunaBlinky, self.posiLinhaBlinky, 14, 11)

    def getPosisPac(self):
        posicoes = self.pacman.getPosicaoMatriz()
        self.posiColunaPac = posicoes[0]
        self.posiLinhaPac = posicoes[1]

        if self.posiColunaPac >= 22 and self.posiLinhaPac == 14:
            self.posiColunaPac = 6
            self.posiLinhaPac = 14
            
                
    def moveBlinky(self):
        if len(self.MovesBlinky) >= 1 and self.MovesBlinky[0] != "":
            x_blinky = self.MovesBlinky[0][0]
            y_blinky = self.MovesBlinky[0][1]

            if x_blinky > 0 and y_blinky == 0:
                self.spriteBlinky = self.SpritesBlinky[0]
            if x_blinky < 0 and y_blinky == 0:
                self.spriteBlinky = self.SpritesBlinky[1]
            if x_blinky == 0 and y_blinky < 0:
                self.spriteBlinky = self.SpritesBlinky[2]
            if x_blinky == 0 and y_blinky > 0:
                self.spriteBlinky = self.SpritesBlinky[3]

            self.Blinky.move(x_blinky, y_blinky)
            self.redrawBlinky()

            del(self.MovesBlinky[0])

        if len(self.MovesBlinky) == 0:
            self.getMovesBlinky()

    def redrawBlinky(self):

        if self.modeScared:
            self.spriteBlinky = self.spritesVulneravel[self.indiceVulneravel]

        self.Blinky.undraw()
        self.Blinky = Image(self.Blinky.getAnchor(), self.spriteBlinky)
        self.Blinky.draw(self.win)

        self.getMatrizPosition()  
    
    def getMatrizPosition(self):
        self.posiBlinky = f"{self.Blinky.getAnchor().getX()},{self.Blinky.getAnchor().getY()}"
        if self.posiBlinky in self.truePositions:
            self.PosiMatriz = self.truePositions[self.posiBlinky]
            getPosi = self.pegaIndice()
            self.posiColunaBlinky = int(getPosi[1])
            self.posiLinhaBlinky = int(getPosi[0])

        #return self.posiColunaBlinky, self.posiLinhaBlinky

    def getPosition(self):
        #return self.Blinky.getAnchor()
        return f"{self.Blinky.getAnchor().getX()},{self.Blinky.getAnchor().getY()}"

    def getBlinkyX(self):
        return self.Blinky.getAnchor().getX()

    def getBlinkyY(self):
        return self.Blinky.getAnchor().getY()

    def pegaIndice(self):        
        prim_indice = ""
        cont = 0
        while cont < 6:
            if self.PosiMatriz[cont] == "[":
                prim_indice += self.PosiMatriz[cont+1]
                if self.PosiMatriz[cont+2] != "]":
                    prim_indice += self.PosiMatriz[cont+2]
            cont += 1

        seg_indice = ""
        while cont < len(self.PosiMatriz):
            if self.PosiMatriz[cont] == "[":
                seg_indice += self.PosiMatriz[cont+1]
                if self.PosiMatriz[cont+2] != "]":
                    seg_indice += self.PosiMatriz[cont+2]
            cont += 1

        return([prim_indice, seg_indice])

    def scaredMode(self, bool):
        if bool == True:
            self.modeScared = True

            self.indiceVulneravel = 0

            self.Blinky.undraw()
            self.Blinky = Image(self.Blinky.getAnchor(), self.spritesVulneravel[self.indiceVulneravel])
            self.Blinky.draw(self.win)

        elif bool == None:
            self.indiceVulneravel = 1

        else:
            self.modeScared = False
            self.redrawBlinky()

    def getMode(self):
        return self.modeScared

#####

#É O MAIS "BURRO", PORQUE TEM MOVIMENTOS PRÉ-DEFINIDOS:
class Pinky:
    def __init__(self, win):
        self.win = win

        self.spritePinky = "Sprites/Pinky/Pinky-U.png"
        
        self.Pinky = Image(Point(290, 290), self.spritePinky)
        self.posiPinky = ""

        self.posiColunaPinky = 14
        self.posiLinhaPinky = 14

        self.move = None

        self.truePositions = getPositions()

        self.MovesPinky = [""]
        self.moveDestinos = [[1,29],[14,23],[6,14],[18,8],[26,1],[21,20],
                             [26,29],[6,20],[12,1],[1,8],[15,20],[14,29]]
        self.moveIndice = 0

        self.SpritesPinky = ["Sprites/Pinky/Pinky-R.png","Sprites/Pinky/Pinky-L.png",
                              "Sprites/Pinky/Pinky-U.png","Sprites/Pinky/Pinky-D.png",]

        self.spritesVulneravel = ["Sprites/Scared/Fear-2.png","Sprites/Scared/Fear-1.png",]
        self.modeScared = False

    def drawPinky(self):
        return self.Pinky.draw(self.win)

    def undrawPinky(self):
        return self.Pinky.undraw()

    def restartPinky(self):
        self.posiColunaPinky = 14
        self.posiLinhaPinky = 14

        self.modeScared = False

        self.Pinky.undraw()
        self.Pinky = Image(Point(290, 290), self.spritePinky)
        self.Pinky.draw(self.win)

        self.getMovesPinky()

        
    def getMovesPinky(self):
        Destinos = self.moveDestinos[self.moveIndice]
        destinho_coluna = Destinos[0]
        destino_linha = Destinos[1]
        self.MovesPinky = a_star(self.posiColunaPinky, self.posiLinhaPinky,destinho_coluna,destino_linha)

        self.moveIndice += 1
        if self.moveIndice == 12:
            self.moveIndice = 0
                
    def movePinky(self):
        if len(self.MovesPinky) >= 1 and self.MovesPinky[0] != "":
            x_pinky = self.MovesPinky[0][0]
            y_pinky = self.MovesPinky[0][1]

            if x_pinky > 0 and y_pinky == 0:
                self.spritePinky = self.SpritesPinky[0]
            if x_pinky < 0 and y_pinky == 0:
                self.spritePinky = self.SpritesPinky[1]
            if x_pinky == 0 and y_pinky < 0:
                self.spritePinky = self.SpritesPinky[2]
            if x_pinky == 0 and y_pinky > 0:
                self.spritePinky = self.SpritesPinky[3]

            self.Pinky.move(x_pinky, y_pinky)
            self.redrawPinky()

            del(self.MovesPinky[0])

        if len(self.MovesPinky) == 0:
            self.getMovesPinky()

    def redrawPinky(self):

        if self.modeScared:
            self.spritePinky = self.spritesVulneravel[self.indiceVulneravel]

        self.Pinky.undraw()
        self.Pinky = Image(self.Pinky.getAnchor(), self.spritePinky)
        self.Pinky.draw(self.win)

        self.getMatrizPosition()  
    
    def getMatrizPosition(self):
        self.posiPinky = f"{self.Pinky.getAnchor().getX()},{self.Pinky.getAnchor().getY()}"
        if self.posiPinky in self.truePositions:
            self.PosiMatriz = self.truePositions[self.posiPinky]
            getPosi = self.pegaIndice()
            self.posiColunaPinky = int(getPosi[1])
            self.posiLinhaPinky = int(getPosi[0])

        #return self.posiColunaPinky, self.posiLinhaPinky

    def getPosition(self):
        #return self.Pinky.getAnchor()
        return f"{self.Pinky.getAnchor().getX()},{self.Pinky.getAnchor().getY()}"

    def getPinkyX(self):
        return self.Pinky.getAnchor().getX()

    def getPinkyY(self):
        return self.Pinky.getAnchor().getY()

    def pegaIndice(self):        
        prim_indice = ""
        cont = 0
        while cont < 6:
            if self.PosiMatriz[cont] == "[":
                prim_indice += self.PosiMatriz[cont+1]
                if self.PosiMatriz[cont+2] != "]":
                    prim_indice += self.PosiMatriz[cont+2]
            cont += 1

        seg_indice = ""
        while cont < len(self.PosiMatriz):
            if self.PosiMatriz[cont] == "[":
                seg_indice += self.PosiMatriz[cont+1]
                if self.PosiMatriz[cont+2] != "]":
                    seg_indice += self.PosiMatriz[cont+2]
            cont += 1

        return([prim_indice, seg_indice])
    
    def scaredMode(self, bool):
        if bool == True:
            self.modeScared = True

            self.indiceVulneravel = 0

            self.Pinky.undraw()
            self.Pinky = Image(self.Pinky.getAnchor(), self.spritesVulneravel[self.indiceVulneravel])
            self.Pinky.draw(self.win)

        elif bool == None:
            self.indiceVulneravel = 1

        else:
            self.modeScared = False
            self.redrawPinky()

    def getMode(self):
        return self.modeScared

#####

class Inky:
    def __init__(self, win, pacman):
        self.win = win
        self.pacman = pacman

        self.spriteInky = "Sprites/Inky/Inky-U.png"
        
        self.Inky = Image(Point(310, 290), self.spriteInky)
        self.posiBlinky = ""

        self.posiColunaInky = 15
        self.posiLinhaInky = 14

        self.move = None

        self.truePositions = getPositions()

        self.movesInky = [""]
    
        self.moveDestinos = [[6,1],[15,5],[21,23],[6,23],[9,11],[21,23],
                             [1,29],[14,17],[26,1],[1,5],[6,14],[20,5],
                             [1,1],[21,23],[1,20],[26,20],[21,26],[21,5]]

        self.moveIndice = 0

        self.SpritesInky = ["Sprites/Inky/Inky-R.png","Sprites/Inky/Inky-L.png",
                              "Sprites/Inky/Inky-U.png","Sprites/Inky/Inky-D.png",]

        self.spritesVulneravel = ["Sprites/Scared/Fear-2.png","Sprites/Scared/Fear-1.png",]
        self.modeScared = False

    def drawInky(self):
        return self.Inky.draw(self.win)

    def undrawInky(self):
        return self.Inky.undraw()

    def restartInky(self):
        self.posiColunaInky = 15
        self.posiLinhaInky = 14

        self.modeScared = False
        
        self.Inky.undraw()
        self.Inky = Image(Point(310, 290), self.spriteInky)
        self.Inky.draw(self.win)

        self.getMovesInky()


    def getMovesInky(self):
        Destinos = self.moveDestinos[self.moveIndice]
        destinho_coluna = Destinos[0]
        destino_linha = Destinos[1]
        self.MovesInky = a_star(self.posiColunaInky, self.posiLinhaInky,destinho_coluna,destino_linha)

        self.moveIndice += 1

        if self.moveIndice == 18:
            self.moveIndice = 0
                
                
    def moveInky(self):
        if len(self.MovesInky) >= 1 and self.MovesInky[0] != "":
            x_inky = self.MovesInky[0][0]
            y_inky = self.MovesInky[0][1]

            if x_inky > 0 and y_inky == 0:
                self.spriteInky = self.SpritesInky[0]
            if x_inky < 0 and y_inky == 0:
                self.spriteInky = self.SpritesInky[1]
            if x_inky == 0 and y_inky < 0:
                self.spriteInky = self.SpritesInky[2]
            if x_inky == 0 and y_inky > 0:
                self.spriteInky = self.SpritesInky[3]

            self.Inky.move(x_inky, y_inky)
            self.redrawInky()

            del(self.MovesInky[0])

        if len(self.MovesInky) == 0:
            self.getMovesInky()

    def redrawInky(self):

        if self.modeScared:
            self.spriteInky = self.spritesVulneravel[self.indiceVulneravel]

        self.Inky.undraw()
        self.Inky = Image(self.Inky.getAnchor(), self.spriteInky)
        self.Inky.draw(self.win)

        self.getMatrizPosition()  
    
    def getMatrizPosition(self):
        self.posiInky = f"{self.Inky.getAnchor().getX()},{self.Inky.getAnchor().getY()}"
        if self.posiInky in self.truePositions:
            self.PosiMatriz = self.truePositions[self.posiInky]
            getPosi = self.pegaIndice()
            self.posiColunaInky = int(getPosi[1])
            self.posiLinhaInky = int(getPosi[0])

        #return self.posiColunaInky, self.posiLinhaInky

    def getPosition(self):
        #return self.Inky.getAnchor()
        return f"{self.Inky.getAnchor().getX()},{self.Inky.getAnchor().getY()}"

    def getInkyX(self):
        return self.Inky.getAnchor().getX()

    def getInkyY(self):
        return self.Inky.getAnchor().getY()

    def pegaIndice(self):        
        prim_indice = ""
        cont = 0
        while cont < 6:
            if self.PosiMatriz[cont] == "[":
                prim_indice += self.PosiMatriz[cont+1]
                if self.PosiMatriz[cont+2] != "]":
                    prim_indice += self.PosiMatriz[cont+2]
            cont += 1

        seg_indice = ""
        while cont < len(self.PosiMatriz):
            if self.PosiMatriz[cont] == "[":
                seg_indice += self.PosiMatriz[cont+1]
                if self.PosiMatriz[cont+2] != "]":
                    seg_indice += self.PosiMatriz[cont+2]
            cont += 1

        return([prim_indice, seg_indice])

    def scaredMode(self, bool):
        if bool == True:
            self.modeScared = True

            self.indiceVulneravel = 0

            self.Inky.undraw()
            self.Inky = Image(self.Inky.getAnchor(), self.spritesVulneravel[self.indiceVulneravel])
            self.Inky.draw(self.win)

        elif bool == None:
            self.indiceVulneravel = 1

        else:
            self.modeScared = False
            self.redrawInky()

    def getMode(self):
        return self.modeScared