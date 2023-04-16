from graphics import *

from Codigos.mapa import *
from Codigos.a_star import *

import Codigos.comidas as com

#Tela Inicial e de Game Over:
from Codigos.GameOver import *
from Codigos.TelaInicial import *

class Game:
    def __init__(self, win, usuario, pontos, vidas, comidas, comidas_especiais, pacman, blinky, pinky, clyde, inky):
        
        self.win = win
        self.username = usuario
        self.usuario = Text(Point(510, 637), f"{self.username}")
        self.pontos = pontos #qtd de pontos
        self.vidas = vidas

        self.timer = Timer()

        self.comidas = comidas
        self.posiComidas = getPosComidas()

        self.comidas_especiais = comidas_especiais
        self.posiEspeciais = getPosEspeciais()

        self.pac_especial = False

        self.total_comidas = 244

        self.pacman = pacman
        
        self.blinky = blinky
        self.stardedBlinky = False
        self.pinky = pinky
        self.stardedPinky = False
        self.clyde = clyde
        self.stardedClyde = False
        self.inky = inky
        self.stardedInky = False

        self.done = False # variável que interrompe o looping principal

    def startGame(self):
        self.pacman.drawPac()

        self.blinky.drawBlinky()
        self.pinky.drawPinky()
        self.clyde.drawClyde()
        self.inky.drawInky()

        for item in self.vidas:
            item.draw(self.win)

        for item in self.comidas:
            if type(item) != str:
                item.draw(self.win)

        for item in self.comidas_especiais:
            if type(item) != str:
                item.draw(self.win)

        self.setUsuario()
        self.setPontuacao()

        #Início do jogo:
        self.gameLoop()

    def atualizaVidas(self):
        if len(self.vidas) > 1:
            for item in self.vidas:
                item.undraw()
            del(self.vidas[-1])
            for item in self.vidas:
                item.draw(self.win)
            self.restartGame()
        else:
            self.vidas = []
            self.GameOver()

    def setUsuario(self):
        self.usuario.setTextColor("white")
        self.usuario.setSize(10)
        self.usuario.setStyle("bold")
        self.usuario.draw(self.win)
        
    def setPontuacao(self):
        self.pontuacao = Text(Point(280, 640), self.pontos)
        self.pontuacao.setTextColor("white")
        self.pontuacao.setStyle("bold")
        self.pontuacao.draw(self.win)

    def atualizaPontuacao(self):
        self.pontuacao.undraw()
        self.setPontuacao()

    def moveFantasmas(self):
        if self.stardedPinky == True:
            self.pinky.movePinky()
        if self.stardedClyde == True:
            self.clyde.moveClyde()
        if self.stardedBlinky == True:
            self.blinky.moveBlinky()
        if self.stardedInky == True:
            self.inky.moveInky()


    def comeFantasma(self, fantasma):
        if fantasma == "Blinky":
            self.blinky.restartBlinky()

            self.pontos += 200
            self.atualizaPontuacao()

        if fantasma == "Clyde":
            self.clyde.restartClyde()

            self.pontos += 200
            self.atualizaPontuacao()

        if fantasma == "Inky":
            self.inky.restartInky()

            self.pontos += 200
            self.atualizaPontuacao()

        if fantasma == "Pinky":
            self.pinky.restartPinky() 

            self.pontos += 200
            self.atualizaPontuacao()

    def checkColisao(self):

        x_pac = self.pacman.getPacX()
        y_pac = self.pacman.getPacY()

        x_blinky = self.blinky.getBlinkyX()
        y_blinky = self.blinky.getBlinkyY()
        dx = abs(x_pac - x_blinky)
        dy = abs(y_pac - y_blinky)
        if 12**2 >= (dx*dx) + (dy*dy):
            update(10)

            checkMode = self.blinky.getMode()
            if self.pac_especial and checkMode == True:
                self.comeFantasma("Blinky")
            else:
                self.atualizaVidas()

        x_pinky = self.pinky.getPinkyX()
        y_pinky = self.pinky.getPinkyY()
        dx = abs(x_pac - x_pinky)
        dy = abs(y_pac - y_pinky)
        if 12**2 >= (dx*dx) + (dy*dy):
            update(10)
            
            checkMode = self.pinky.getMode()
            if self.pac_especial and checkMode == True:
                self.comeFantasma("Pinky")
            else:
                self.atualizaVidas()

        x_clyde = self.clyde.getClydeX()
        y_clyde = self.clyde.getClydeY()
        dx = abs(x_pac - x_clyde)
        dy = abs(y_pac - y_clyde)
        if 12**2 >= (dx*dx) + (dy*dy):
            update(10)
            
            checkMode = self.clyde.getMode()
            if self.pac_especial and checkMode == True:
                self.comeFantasma("Clyde")
            else:
                self.atualizaVidas()

        x_inky = self.inky.getInkyX()
        y_inky = self.inky.getInkyY()
        dx = abs(x_pac - x_inky)
        dy = abs(y_pac - y_inky)
        if 12**2 >= (dx*dx) + (dy*dy):
            update(10)
            
            checkMode = self.inky.getMode()
            if self.pac_especial and checkMode == True:
                self.comeFantasma("Inky")
            else:
                self.atualizaVidas()

        self.line.undraw()
        self.line = Line(Point(x_pac,y_pac), Point(x_blinky,y_blinky))
        self.line.setWidth(2)
        self.line.setFill("white")
        self.line.draw(self.win)

        self.line2.undraw()
        self.line2 = Line(Point(x_pac,y_pac), Point(x_clyde,y_clyde))
        self.line2.setWidth(2)
        self.line2.setFill("white")
        self.line2.draw(self.win)

        self.line3.undraw()
        self.line3 = Line(Point(x_pac,y_pac), Point(x_inky,y_inky))
        self.line3.setWidth(2)
        self.line3.setFill("white")
        self.line3.draw(self.win)
        
        self.line4.undraw()
        self.line4 = Line(Point(x_pac,y_pac), Point(x_pinky,y_pinky))
        self.line4.setWidth(2)
        self.line4.setFill("white")
        self.line4.draw(self.win)
        
       
        

    def checkComidas(self):
        self.posicaoPacMan = self.pacman.getPosition()
        if self.posicaoPacMan in self.posiComidas:
            IndiceComidas = int(self.posiComidas[self.posicaoPacMan])
            if self.comidas[IndiceComidas-1] != "JA PASSEI":
                self.comidas[IndiceComidas-1].undraw()
                self.comidas[IndiceComidas-1] = "JA PASSEI"
                
                self.total_comidas -= 1
                self.pontos += 10

                self.atualizaPontuacao()

                if self.total_comidas == 0:
                    self.resetarGame(False, "")

    def checkEspeciais(self):
        self.posicaoPacMan = self.pacman.getPosition()
        if self.posicaoPacMan in self.posiEspeciais:
            IndiceEspeciais = int(self.posiEspeciais[self.posicaoPacMan])
            if self.comidas_especiais[IndiceEspeciais] != "JA PASSEI":
                self.comidas_especiais[IndiceEspeciais].undraw()
                self.comidas_especiais[IndiceEspeciais] = "JA PASSEI"

                self.total_comidas -= 1
                self.pontos += 50

                self.especialPacMan()

                self.atualizaPontuacao()

                if self.total_comidas == 0:
                    self.resetarGame(False, "")

    def especialPacMan(self):
        self.timerEspecial = Timer()

        self.pac_especial = True

        #Deixamos os fantasmas azuis (modo assustado):
        self.blinky.scaredMode(True)
        self.pinky.scaredMode(True)
        self.clyde.scaredMode(True)
        self.inky.scaredMode(True)

    def perdeVida(self):
        self.line.undraw()
        self.line2.undraw()
        self.line3.undraw()
        self.line4.undraw()
        if len(self.vidas) >= 1:
            self.atualizaVidas()
            del(self.vidas[-1])
            self.setVidas()

        else:
            self.encerraGame()

    def checkTimer(self):
        if int(self.timer.getTime()) >= 4 and self.stardedPinky == False:
            self.pinky.getMovesPinky()
            self.stardedPinky = True
        if int(self.timer.getTime()) >= 6 and self.stardedClyde == False:
            self.clyde.getMovesClyde()
            self.stardedClyde = True
        if int(self.timer.getTime()) >= 8 and self.stardedBlinky == False:
            self.blinky.getMovesBlinky()
            self.stardedBlinky = True
        if int(self.timer.getTime()) >= 10 and self.stardedInky == False:
            self.inky.getMovesInky()
            self.stardedInky = True

        #Checagem do Timer() do Especial do PacMan:
        if self.pac_especial ==  True:
            if int(self.timerEspecial.getTime()) >= 5:
                self.pinky.scaredMode(None)
                self.inky.scaredMode(None)
                self.blinky.scaredMode(None)
                self.clyde.scaredMode(None)

            if int(self.timerEspecial.getTime()) >= 8:
                self.pinky.scaredMode(False)
                self.inky.scaredMode(False)
                self.blinky.scaredMode(False)
                self.clyde.scaredMode(False)

                self.pac_especial = False


    #CHAMADO QUANDO AS VIDAS ACABAM:
    def GameOver(self):
        self.atualizaHighscore()

        time.sleep(0.05)

        encerrarGame = telaGameOver(self.win)

        if encerrarGame == False:
            self.pontos = 0
            self.total_comidas = 244

            self.resetarGame(False, "")

        if encerrarGame == True:
            self.pontos = 0
            self.total_comidas = 244
            
            telaInicial = TelaInicial(self.win, True)
            
            usuario = telaInicial #-> a função "TelaInicial()"" retorna o nome do usuário
            self.resetarGame(True, usuario)

    #CHAMADA SEMPRE QUE UM FANTASMA PEGA O PACMAN E QUANDO O JOGO PRECISA SER REINICIADO:
    def restartGame(self): 
        self.done = True

        #Coloco todos na posição inicial:
        self.pacman.restartPacMan()

        self.pinky.scaredMode(False)
        self.inky.scaredMode(False)
        self.blinky.scaredMode(False)
        self.clyde.scaredMode(False)

        self.blinky.restartBlinky()
        self.clyde.restartClyde()
        self.inky.restartInky()
        self.pinky.restartPinky()


        self.pac_especial = False

        time.sleep(0.05)

        self.done = False
        self.gameLoop()

    #É CHAMADA DENTRO DO GAME OVER (DEIXA O JOGO NA CONFIGURAÇÃO INICIAL):
    def resetarGame(self, resetUsuario, user):
        self.timer = Timer()
        
        self.stardedBlinky = False
        self.stardedPinky = False
        self.stardedInky = False
        self.stardedClyde = False

        if resetUsuario:
            self.username = user

            self.usuario.undraw()
            self.usuario = Text(Point(510, 637), f"{self.username}")
            self.setUsuario()

        self.encerraGame()

        self.comidas = com.comidas()
        self.posiComidas = getPosComidas()
        for item in self.comidas:
            item.draw(self.win)

        self.comidas_especiais = com.comidas_especiais()
        self.posiEspeciais = getPosEspeciais()
        for item in self.comidas_especiais:
            item.draw(self.win)

        if len(self.vidas) == 0:
            self.vidas = [Image(Point(20, 637), "Sprites/lifePacMan.png"),
                        Image(Point(35, 637), "Sprites/lifePacMan.png"),
                        Image(Point(50, 637), "Sprites/lifePacMan.png")]
        for item in self.vidas:
            item.draw(self.win)

        self.atualizaPontuacao()

        self.restartGame()

    #CHAMADO QUANDO O JOGO PRECISA SER RESETADO (TUDO É APAGADO):
    def encerraGame(self):
        self.pacman.undrawPac()
        self.blinky.undrawBlinky()
        self.pinky.undrawPinky()
        self.clyde.undrawClyde()
        self.inky.undrawInky()
        
        for item in self.vidas:
            item.undraw()

        for item in self.comidas:
            if type(item) != str:
                item.undraw()

        for item in self.comidas_especiais:
            if type(item) != str:
                item.undraw()

        self.pontuacao.undraw()

        self.total_comidas == 244


    def atualizaHighscore(self):        
        new_Score = f'{self.username};{self.pontos}\n'

        novo_Arquivo = open("Highscores\highscores.csv", "a", encoding="utf-8")
        novo_Arquivo.write(new_Score)
        novo_Arquivo.close()

    def gameLoop(self):
        MOVIMENTO = ""
        tryMove = ""

        self.line = Line(Point(0,0), Point(0,0))
        self.line.draw(self.win)
        self.line2 = Line(Point(0,0), Point(0,0))
        self.line2.draw(self.win)
        self.line3 = Line(Point(0,0), Point(0,0))
        self.line3.draw(self.win)
        self.line4 = Line(Point(0,0), Point(0,0))
        self.line4.draw(self.win)
        
        #Lógica do movimento inicial do Pac-Man:
        iniciar = False
        while not iniciar:
            key = self.win.getKey()
            if key == "Right" or key == "D" or key == "d":
                MOVIMENTO = "Right"
                iniciar = True
            elif key == "Left" or key == "A" or key == "a":
                MOVIMENTO = "Left"
                iniciar = True
        #

        #Laço principal do jogo:
        while not self.done:
            #Lógica do próximo movimento do Pac-Man:    
            if MOVIMENTO != "":
                key = self.win.checkKey()

                if key == "Up" or key == "W" or key == "w":
                    tryMove = "Up"
                elif key == "Down" or key == "S" or key == "s":
                    tryMove = "Down"
                elif key == "Right" or key == "D" or key == "d":
                    tryMove = "Right"
                elif key == "Left" or key == "A" or key == "a":
                    tryMove = "Left"

            if MOVIMENTO != "":
                self.pacman.movePac(MOVIMENTO)
                
            if tryMove != "":
                if self.pacman.proxMovimento(tryMove):
                    MOVIMENTO = tryMove

            self.checkTimer()

            #Checagem da colisão com as comidas:
            self.checkComidas()

            #Checagem da colisão com as comidas especiais:
            self.checkEspeciais()

            self.moveFantasmas()

            self.checkColisao()

            update(10)