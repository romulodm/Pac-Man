from graphics import *

def telaGameOver(win):

    TELA_ITENS = []

    imagemGameOver = Image(Point(280, 330), "Sprites/game-over.png")
    TELA_ITENS.append(imagemGameOver) 

    JOGARSOMBRA = Text(Point(282, 392), "DESEJA JOGAR NOVAMENTE?")
    JOGARSOMBRA.setTextColor("blue")
    JOGARSOMBRA.setFace("terminal")
    JOGARSOMBRA.setStyle("bold italic")
    JOGARSOMBRA.setSize(20)
    TELA_ITENS.append(JOGARSOMBRA)
    JOGAR = Text(Point(280, 390), "DESEJA JOGAR NOVAMENTE?")
    JOGAR.setTextColor("white")
    JOGAR.setFace("terminal")
    JOGAR.setStyle("bold italic")
    JOGAR.setSize(20)
    TELA_ITENS.append(JOGAR)

    SIMSOMBRA = Text(Point(182, 512), "SIM")
    SIMSOMBRA.setTextColor("blue")
    SIMSOMBRA.setFace("terminal")
    SIMSOMBRA.setStyle("bold italic")
    SIMSOMBRA.setSize(20)
    TELA_ITENS.append(SIMSOMBRA)
    SIM = Text(Point(180, 510), "SIM")
    SIM.setTextColor("yellow")
    SIM.setFace("terminal")
    SIM.setStyle("bold italic")
    SIM.setSize(20)
    TELA_ITENS.append(SIM)

    NAOSOMBRA = Text(Point(367, 512), "NÃO")
    NAOSOMBRA.setTextColor("blue")
    NAOSOMBRA.setFace("terminal")
    NAOSOMBRA.setStyle("bold italic")
    NAOSOMBRA.setSize(20)
    TELA_ITENS.append(NAOSOMBRA)
    NAO = Text(Point(365, 510), "NÃO")
    NAO.setTextColor("white")
    NAO.setFace("terminal")
    NAO.setStyle("bold italic")
    NAO.setSize(20)
    TELA_ITENS.append(NAO)

    setaGameOver = Polygon(Point(173, 550), Point(183, 550), Point(178, 540))
    setaGameOver.setFill("yellow")
    setaGameOver.setOutline("yellow")
    setaGameOver.setWidth(5)
    TELA_ITENS.append(setaGameOver)

    miniPacMan =  Image(Point(280, 650), "Sprites/Pac - Menu/Pacman-Ajar-R.png")
    TELA_ITENS.append(miniPacMan)

    for item in TELA_ITENS:
        item.draw(win)

    POSICAO = 0

    done = False
    while not done:
        key = win.getKey()

        if key == "Right" and POSICAO == 0:
            POSICAO = 1
            TELA_ITENS[-2].move(188,0)
 
            TELA_ITENS[4].undraw()
            TELA_ITENS[4].setTextColor("white")
            TELA_ITENS[4].draw(win) # SIM
            TELA_ITENS[6].undraw()
            TELA_ITENS[6].setTextColor("yellow")
            TELA_ITENS[6].draw(win) # NÃO

            TELA_ITENS[-1].undraw()
            TELA_ITENS[-1] = Image(Point(280, 650), "Sprites/Pac - Menu/Pacman-Open-R.png")
            TELA_ITENS[-1].draw(win) # mini Pac-Man

        elif key == "Left" and POSICAO == 1:
            POSICAO = 0
            TELA_ITENS[-2].move(-188,0)

            TELA_ITENS[4].undraw()
            TELA_ITENS[4].setTextColor("yellow")
            TELA_ITENS[4].draw(win) # SIM
            TELA_ITENS[6].undraw()
            TELA_ITENS[6].setTextColor("white")
            TELA_ITENS[6].draw(win) # NÃO

            TELA_ITENS[-1].undraw()
            TELA_ITENS[-1] = Image(Point(280, 650), "Sprites/Pac - Menu/Pacman-Ajar-R.png")
            TELA_ITENS[-1].draw(win) # mini Pac-Man

        #Se apertar enter:
        elif key == "Return" and POSICAO == 0:

            for item in TELA_ITENS:
                item.undraw()

            return False

        elif key == "Return" and POSICAO == 1:

            for item in TELA_ITENS:
                item.undraw()

            return True    
        