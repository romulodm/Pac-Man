from graphics import *

#
from Codigos.comidas import *
from Codigos.mapa import *
from Codigos.a_star import *
from Codigos.TelaInicial import *

#
from Classes.classpacman import *
from Classes.classfantasmas import *
from Classes.classgame import *

def main():

    win = GraphWin("Pac-Man",560,660,autoflush=False)
    win.setBackground("black")

    vidas = [Image(Point(20, 637), "Sprites/lifePacMan.png"),
            Image(Point(35, 637), "Sprites/lifePacMan.png"),
            Image(Point(50, 637), "Sprites/lifePacMan.png")]

    pontos = 0
                             #"False" porque não quero que ele crie um retângulo para "apagar tudo da tela".
    usuario = TelaInicial(win, False) # "TelaInicial" é uma função que retorna um nome de usuário.
        
    comidas = com.comidas() # lista de objetos da Graphics (as bolinhas)
    comidas_especiais = com.comidas_especiais() # lista de "pastilhas especiais" (que dão poderes ao pac-man)

    MAP = Image(Point(280,310), "Sprites/map.png")
    MAP.draw(win)

    #Crio as instâncias dos objetos:

    PACMAN = PacMan(win) #

    #Fantasma rosa:
    PINKY = Pinky(win)

    #Fantasma laranja:
    CLYDE = Clyde(win, PACMAN)

    #Fantasma vermelho:
    BLINKY = Blinky(win, PACMAN)

    #Fantasma azul:
    INKY = Inky(win, PACMAN)

    GAME = Game(win,usuario,pontos,vidas,comidas,comidas_especiais, 
                        PACMAN,BLINKY,PINKY,CLYDE,INKY)
    
    GAME.startGame()
    
if __name__ == "__main__":
    main()