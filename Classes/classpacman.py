from graphics import *
from Codigos.mapa import *


class PacMan:
    def __init__(self, win):
        self.win = win

        self.spritePacMan = "Sprites/Pacman/Pacman-Closed.png"

        self.spritesRight = ["Sprites/Pacman/Pacman-Open-R.png", "Sprites/Pacman/Pacman-Ajar-R.png"]
        self.spritesLeft = ["Sprites/Pacman/Pacman-Open-L.png", "Sprites/Pacman/Pacman-Ajar-L.png"]
        self.spritesUp = ["Sprites/Pacman/Pacman-Open-U.png", "Sprites/Pacman/Pacman-Ajar-U.png"]
        self.spritesDown = ["Sprites/Pacman/Pacman-Open-D.png", "Sprites/Pacman/Pacman-Ajar-D.png"]

        self.spriteIndice = 0

        self.pos_x = 280
        self.pos_y = 590
        self.pacman = Image(Point(self.pos_x, self.pos_y), self.spritePacMan)
        self.posiPacMan = ""

        self.map = MAPA

        self.pos_coluna = 14
        self.pos_linha = 29
        self.quadrantePac = None

        self.move = False
        self.tryMove = False

        self.truePositions = getPositions()

    def drawPac(self):
        return self.pacman.draw(self.win)
    
    def undrawPac(self):
        return self.pacman.undraw()

    def restartPacMan(self):
        self.pos_x = 280
        self.pos_y = 590
        self.pacman.undraw()
        self.pacman = Image(Point(self.pos_x, self.pos_y), self.spritePacMan)
        self.pacman.draw(self.win)

        self.pos_coluna = 14
        self.pos_linha = 29
        self.quadrantePac = None


    def getPosicaoMatriz(self):
        self.atualizaMatrizPosition()
        return int(self.pos_coluna), int(self.pos_linha)

    def getQuadrante(self):
        self.atualizaMatrizPosition()
        if self.pos_coluna >= 1 and self.pos_coluna <= 13 and self.pos_linha  < 8:
            self.quadrantePac = 1
        if self.pos_coluna >= 14 and self.pos_linha <= 8:
            self.quadrantePac = 2
        if self.pos_coluna >= 0 and self.pos_linha > 7 and self.pos_linha < 20:
            self.quadrantePac = 3
        if self.pos_coluna >= 1 and self.pos_coluna <= 13 and self.pos_linha > 19:
            self.quadrantePac = 4
        if self.pos_coluna >= 14 and self.pos_linha  > 19:
            self.quadrantePac = 5
        else:
            self.quadrantePac = 3
        
        return self.quadrantePac

    def getMovement(self):
        return self.move

    def getPosition(self):
        return f"{float(self.pos_x)},{float(self.pos_y)}"

    def getPacX(self):
        return self.pacman.getAnchor().getX()

    def getPacY(self):
        return self.pacman.getAnchor().getY()

    def movePac(self, move):
        Check = self.checkMove(move)
        if Check == True:
            self.move = move
            if self.move == "Right":
                self.pacman.move(10,0)
                self.changeSprite()
            if self.move == "Left":
                self.pacman.move(-10,0)
                self.changeSprite()
            if self.move == "Up":
                self.pacman.move(0,-10)
                self.changeSprite()
            if self.move == "Down":
                self.pacman.move(0,10)
                self.changeSprite()

        else:
            self.move = "None"

    def changeSprite(self):
        self.spriteIndice = (self.spriteIndice + 1) % 2

        if self.move == "Right":
            self.spritePacMan = self.spritesRight[self.spriteIndice]
        if self.move == "Left":
            self.spritePacMan = self.spritesLeft[self.spriteIndice]
        if self.move == "Up":
            self.spritePacMan = self.spritesUp[self.spriteIndice]
        if self.move == "Down":
            self.spritePacMan = self.spritesDown[self.spriteIndice]

        self.redrawPac()

    def redrawPac(self):
        self.pos_x = self.pacman.getAnchor().getX()
        self.pos_y = self.pacman.getAnchor().getY()

        if self.pos_x <= -10.0 and self.pos_y == 290.0:
            self.pacman.undraw()
            self.pacman = Image(Point(550,290), self.spritePacMan)
            self.pacman.draw(self.win)

        elif self.pos_x >= 550 and self.pos_y == 290.0:
            self.pacman.undraw()
            self.pacman = Image(Point(-10, 290), self.spritePacMan)
            self.pacman.draw(self.win)
        
        else:
            self.pacman.undraw()
            self.pacman = Image(Point(self.pos_x,self.pos_y), self.spritePacMan)
            self.pacman.draw(self.win)
            self.atualizaMatrizPosition()

    def checkMove(self, tryMove):
        self.atualizaMatrizPosition()

        if self.pos_linha == 14 and self.pos_coluna == 27:
            return True
        if tryMove == "Left":
            if self.map[self.pos_linha][self.pos_coluna - 1] == 0:
                return True
        if tryMove == "Right":
            if self.map[self.pos_linha][self.pos_coluna + 1] == 0:
                return True
        if tryMove == "Up":
            if self.map[self.pos_linha - 1][self.pos_coluna] == 0:
                return True
        if tryMove == "Down":
            if self.map[self.pos_linha + 1][self.pos_coluna] == 0:
                return True

        return False

    def atualizaMatrizPosition(self):
        self.posiPacMan = f"{self.pacman.getAnchor().getX()},{self.pacman.getAnchor().getY()}"
        if self.posiPacMan in self.truePositions:
            self.PosiMatriz = self.truePositions[self.posiPacMan]
            getPosi = self.pegaIndice()
            self.pos_coluna = int(getPosi[1])
            self.pos_linha = int(getPosi[0])

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

    def proxMovimento(self, tryMove):
        self.atualizaMatrizPosition()
        
        if self.move == "None" and tryMove == "Right" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha][self.pos_coluna + 1] == 0:
                return True
            return False
        if self.move == "None" and tryMove == "Left" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha][self.pos_coluna - 1] == 0:
                return True
            return False
        if self.move == "None" and tryMove == "Up" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha - 1][self.pos_coluna] == 0:
                return True
            return False  
        if self.move == "None" and tryMove == "Down" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha + 1][self.pos_coluna] == 0:
                return True
            return False
        if self.move == "Right" and tryMove == "Left" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha][self.pos_coluna - 1] == 0:
                return True
            return False   
        if self.move == "Right" and tryMove == "Up" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha - 1][self.pos_coluna] == 0:
                return True
            return False       
        if self.move == "Right" and tryMove == "Down" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha + 1][self.pos_coluna] == 0:
                return True
            return False
        
        #Se o player quiser mudar de direção no túnel (na esquerda), na borda da janela:
        try:
            if self.move == "Left" and tryMove == "Right" and self.posiPacMan in self.truePositions:
                if self.map[self.pos_linha][self.pos_coluna + 1] == 0:
                    return True
                return False  
             
        except IndexError:
            return True
        
        if self.move == "Left" and tryMove == "Up" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha - 1][self.pos_coluna] == 0:
                return True
            return False     
        if self.move == "Left" and tryMove == "Down" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha + 1][self.pos_coluna] == 0:
                return True
            return False
        if self.move == "Up" and tryMove == "Right" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha][self.pos_coluna + 1] == 0:
                return True
            return False
        if self.move == "Up" and tryMove == "Left" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha][self.pos_coluna - 1] == 0:
                return True
            return False       
        if self.move == "Up" and tryMove == "Down" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha + 1][self.pos_coluna] == 0:
                return True
            return False
        if self.move == "Down" and tryMove == "Right" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha][self.pos_coluna + 1] == 0:
                return True
            return False
        if self.move == "Down" and tryMove == "Left" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha][self.pos_coluna - 1] == 0:
                return True
            return False
        if self.move == "Down" and tryMove == "Up" and self.posiPacMan in self.truePositions:
            if self.map[self.pos_linha - 1][self.pos_coluna] == 0:
                return True
            return False