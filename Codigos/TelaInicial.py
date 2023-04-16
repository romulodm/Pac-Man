from graphics import *

#

def TelaInicial(win, apagar):

    TELA_ITENS = []

    apagarTudo = Rectangle(Point(0,0), Point(560, 660))
    apagarTudo.setFill("black")
    apagarTudo.setOutline("black")
    apagarTudo.draw(win)

    LOGO = Image(Point(280, 150), "Sprites/pacman-logo-1.png")
    TELA_ITENS.append(LOGO)

    JOGARSOMBRA = Text(Point(282, 352), "JOGAR")
    JOGARSOMBRA.setTextColor("blue")
    JOGARSOMBRA.setFace("terminal")
    JOGARSOMBRA.setStyle("bold italic")
    JOGARSOMBRA.setSize(20)
    TELA_ITENS.append(JOGARSOMBRA)
    JOGAR = Text(Point(280, 350), "JOGAR")
    JOGAR.setTextColor("white")
    JOGAR.setFace("terminal")
    JOGAR.setStyle("bold italic")
    JOGAR.setSize(20)
    TELA_ITENS.append(JOGAR)

    HIGHSCORESOMBRA = Text(Point(282, 432), "HIGHSCORES")
    HIGHSCORESOMBRA.setTextColor("blue")
    HIGHSCORESOMBRA.setFace("terminal")
    HIGHSCORESOMBRA.setStyle("bold italic")
    HIGHSCORESOMBRA.setSize(20)
    TELA_ITENS.append(HIGHSCORESOMBRA)
    HIGHSCORE = Text(Point(280, 430), "HIGHSCORES")
    HIGHSCORE.setTextColor("yellow")
    HIGHSCORE.setFace("terminal")
    HIGHSCORE.setStyle("bold italic")
    HIGHSCORE.setSize(20)
    TELA_ITENS.append(HIGHSCORE)

    SAIRSOMBRA = Text(Point(282, 512), "SAIR")
    SAIRSOMBRA.setTextColor("blue")
    SAIRSOMBRA.setFace("terminal")
    SAIRSOMBRA.setStyle("bold italic")
    SAIRSOMBRA.setSize(20)
    TELA_ITENS.append(SAIRSOMBRA)
    SAIR = Text(Point(280, 510), "SAIR")
    SAIR.setTextColor("yellow")
    SAIR.setFace("terminal")
    SAIR.setStyle("bold italic")
    SAIR.setSize(20)
    TELA_ITENS.append(SAIR)

    COPYRIGHT = Text(Point(280, 649), "© Romulo")
    COPYRIGHT.setTextColor("yellow")
    COPYRIGHT.setFace("helvetica")
    COPYRIGHT.setStyle("bold italic")
    COPYRIGHT.setSize(7)
    TELA_ITENS.append(COPYRIGHT)

    SETA = Image(Point(217, 350), "Sprites/Pac - Menu/Pacman-Ajar-R.png")
    TELA_ITENS.append(SETA)

    for item in TELA_ITENS:
        item.draw(win)

    POSICAO = 1

    done = False
    while not done:
        key = win.getKey()

        if key == "Down" and POSICAO == 2:
            TELA_ITENS[-1].undraw()
            TELA_ITENS[-1] = Image(Point(227, 510), "Sprites/Pac - Menu/Pacman-Ajar-R.png")
            TELA_ITENS[-1].draw(win) # SETA
 
            TELA_ITENS[4].undraw()
            TELA_ITENS[4].setTextColor("yellow")
            TELA_ITENS[4].draw(win) # HIGHSCORE
            TELA_ITENS[6].undraw()
            TELA_ITENS[6].setTextColor("white")
            TELA_ITENS[6].draw(win) # SAIR

            POSICAO = 3

        if key == "Down" and POSICAO == 1:
            TELA_ITENS[-1].undraw()
            TELA_ITENS[-1] = Image(Point(172, 430), "Sprites/Pac - Menu/Pacman-Open-R.png")
            TELA_ITENS[-1].draw(win) # SETA

            TELA_ITENS[2].undraw()
            TELA_ITENS[2].setTextColor("yellow")
            TELA_ITENS[2].draw(win) # JOGAR
            TELA_ITENS[4].undraw()
            TELA_ITENS[4].setTextColor("white")
            TELA_ITENS[4].draw(win) # HIGHSCORE

            POSICAO = 2

        if key == "Up" and POSICAO == 2:
            TELA_ITENS[-1].undraw()
            TELA_ITENS[-1] = Image(Point(217, 350), "Sprites/Pac - Menu/Pacman-Ajar-R.png")
            TELA_ITENS[-1].draw(win) # SETA

            TELA_ITENS[4].undraw()
            TELA_ITENS[4].setTextColor("yellow")
            TELA_ITENS[4].draw(win) # HIGHSCORE
            TELA_ITENS[2].undraw()
            TELA_ITENS[2].setTextColor("white")
            TELA_ITENS[2].draw(win) # JOGAR

            POSICAO = 1

        if key == "Up" and POSICAO == 3:
            TELA_ITENS[-1].undraw()
            TELA_ITENS[-1] = Image(Point(172, 430), "Sprites/Pac - Menu/Pacman-Open-R.png")
            TELA_ITENS[-1].draw(win) # SETA

            TELA_ITENS[6].undraw()
            TELA_ITENS[6].setTextColor("yellow")
            TELA_ITENS[6].draw(win) # SAIR  
            TELA_ITENS[4].undraw()
            TELA_ITENS[4].setTextColor("white")
            TELA_ITENS[4].draw(win) # HIGHSCORE    

            POSICAO = 2

        if key == "Return" and POSICAO == 1:
            usuario = InsiraNome(win)
            if usuario != "VOLTANDO!":
                for item in TELA_ITENS:
                    item.undraw()
                apagarTudo.undraw()

                return usuario
                
        if key == "Return" and POSICAO == 2:
            HighScore(win)

        if key == "Return" and POSICAO == 3:
            win.close()

        update(60)

####################

def InsiraNome(win):
    ITENS_NOME = []

    APAGAR = Rectangle(Point(0, 0), Point(560, 660))
    APAGAR.setFill("black")
    ITENS_NOME.append(APAGAR)

    MENSAGEMSOMBRA = Text(Point(282, 202), "Insira seu nome:")
    MENSAGEMSOMBRA.setTextColor("blue")
    MENSAGEMSOMBRA.setFace("terminal")
    MENSAGEMSOMBRA.setStyle("bold italic")
    MENSAGEMSOMBRA.setSize(20)
    ITENS_NOME.append(MENSAGEMSOMBRA)
    MENSAGEM = Text(Point(280, 200), "Insira seu nome:")
    MENSAGEM.setFace("terminal")
    MENSAGEM.setTextColor("white")
    MENSAGEM.setStyle("bold italic")
    MENSAGEM.setSize(20)
    ITENS_NOME.append(MENSAGEM)

    CAIXA_NOME = Rectangle(Point(70, 250), Point(490, 310))
    CAIXA_NOME.setFill("white") #EEE8AA
    CAIXA_NOME.setOutline("blue")
    CAIXA_NOME.setWidth(3)
    ITENS_NOME.append(CAIXA_NOME)

    VOLTAR = Rectangle(Point(270, 330), Point(490, 370))
    VOLTAR.setFill("ORANGE") #EEE8AA
    VOLTAR.setOutline("white")
    VOLTAR.setWidth(1)
    ITENS_NOME.append(VOLTAR)
    VOLTAR_PALAVRA = Text(Point(380, 350), "VOLTAR")
    VOLTAR_PALAVRA.setTextColor("WHITE")
    VOLTAR_PALAVRA.setFace("terminal")
    VOLTAR_PALAVRA.setStyle("bold italic")
    VOLTAR_PALAVRA.setSize(20)
    ITENS_NOME.append(VOLTAR_PALAVRA)

    CONFIRMAR = Rectangle(Point(70, 330), Point(260, 370))
    CONFIRMAR.setFill("GRAY") #EEE8AA
    CONFIRMAR.setOutline("white")
    CONFIRMAR.setWidth(1)
    ITENS_NOME.append(CONFIRMAR)
    CONFIRMAR_PALAVRA = Text(Point(165, 350), "CONFIRMAR")
    CONFIRMAR_PALAVRA.setTextColor("WHITE")
    CONFIRMAR_PALAVRA.setFace("terminal")
    CONFIRMAR_PALAVRA.setStyle("bold italic")
    CONFIRMAR_PALAVRA.setSize(20)
    ITENS_NOME.append(CONFIRMAR_PALAVRA)

    LETRAS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
              "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    usuario = ""

    NOME_TELA = Text(Point(280, 280), f"")
    ITENS_NOME.append(NOME_TELA)

    for item in ITENS_NOME:
        item.draw(win)

    done = False
    while not done:
        key = win.checkKey()

        click = win.checkMouse()
        if click != None:
            mouse_x = click.getX()
            mouse_y = click.getY()

            if mouse_x >= 70 and mouse_x <= 260 and mouse_y >= 330 and mouse_y <= 370:
                if len(usuario) >= 3:
                    for item in ITENS_NOME:
                        item.undraw()
                    return usuario

            if mouse_x >= 270 and mouse_x <= 490 and mouse_y >= 330 and mouse_y <= 370:
                for item in ITENS_NOME:
                    item.undraw()
                return "VOLTANDO!"


        if key in LETRAS and len(usuario) < 8:
            usuario += key

            ITENS_NOME[-1].undraw()
            ITENS_NOME[-1] = Text(Point(280, 280), f"{usuario}")
            ITENS_NOME[-1].setTextColor("black")
            ITENS_NOME[-1].setFace("terminal")
            ITENS_NOME[-1].setStyle("bold italic")
            ITENS_NOME[-1].setSize(19)
            ITENS_NOME[-1].draw(win)
            update(60)

        if key == "BackSpace" and len(usuario) >= 1:
            usuario = usuario[:-1]

            ITENS_NOME[3].undraw()
            ITENS_NOME[3] = Rectangle(Point(70, 250), Point(490, 310))
            ITENS_NOME[3].setFill("white")
            ITENS_NOME[3].setOutline("blue")
            ITENS_NOME[3].setWidth(3) 
            ITENS_NOME[3].draw(win) # CAIXA DO NOME

            ITENS_NOME[-1].undraw()
            ITENS_NOME[-1] = Text(Point(280, 280), f"{usuario}")
            ITENS_NOME[-1].setTextColor("black")
            ITENS_NOME[-1].setFace("terminal")
            ITENS_NOME[-1].setStyle("bold italic")
            ITENS_NOME[-1].setSize(21)
            ITENS_NOME[-1].draw(win)
            update(60)

        if len(usuario) >= 3:
            ITENS_NOME[-3].undraw()
            ITENS_NOME[-3] = Rectangle(Point(70, 330), Point(260, 370))
            ITENS_NOME[-3].setFill("GREEN") #EEE8AA
            ITENS_NOME[-3].setOutline("white")
            ITENS_NOME[-3].setWidth(1)
            ITENS_NOME[-3].draw(win) # CAIXA "CONFIRMAR"

            ITENS_NOME[-2].undraw()
            ITENS_NOME[-2] = Text(Point(165, 350), "CONFIRMAR")
            ITENS_NOME[-2].setTextColor("WHITE")
            ITENS_NOME[-2].setFace("terminal")
            ITENS_NOME[-2].setStyle("bold italic")
            ITENS_NOME[-2].setSize(20) # PALAVRA "CONFIRMAR"
            ITENS_NOME[-2].draw(win)
            update(60)

        if len(usuario) < 3:
            ITENS_NOME[-3].undraw()
            ITENS_NOME[-3] = Rectangle(Point(70, 330), Point(260, 370))
            ITENS_NOME[-3].setFill("gray") #EEE8AA
            ITENS_NOME[-3].setOutline("white")
            ITENS_NOME[-3].setWidth(1)
            ITENS_NOME[-3].draw(win) # CAIXA "CONFIRMAR"

            ITENS_NOME[-2].undraw()
            ITENS_NOME[-2] = Text(Point(165, 350), "CONFIRMAR")
            ITENS_NOME[-2].setTextColor("WHITE")
            ITENS_NOME[-2].setFace("terminal")
            ITENS_NOME[-2].setStyle("bold italic")
            ITENS_NOME[-2].setSize(20) # PALAVRA "CONFIRMAR"
            ITENS_NOME[-2].draw(win)
            update(60)


        if key == "Return" and len(usuario) >= 3:
            for item in ITENS_NOME:
                item.undraw()
            return usuario

        if key == "Escape":
            for item in ITENS_NOME:
                item.undraw()
            return "VOLTANDO!"


def HighScore(win):

    lista_Highscores = organizaScores()

    ITENS_HIGHSCORE = []

    APAGAR = Rectangle(Point(0, 0), Point(560, 660))
    APAGAR.setFill("black")
    ITENS_HIGHSCORE.append(APAGAR)

    HIGHSCORESOMBRA = Text(Point(282, 102), "MELHORES JOGADORES:")
    HIGHSCORESOMBRA.setTextColor("blue")
    HIGHSCORESOMBRA.setFace("terminal")
    HIGHSCORESOMBRA.setStyle("bold italic")
    HIGHSCORESOMBRA.setSize(20)
    ITENS_HIGHSCORE.append(HIGHSCORESOMBRA)
    HIGHSCORE = Text(Point(280, 100), "MELHORES JOGADORES:")
    HIGHSCORE.setFace("terminal")
    HIGHSCORE.setTextColor("white")
    HIGHSCORE.setStyle("bold italic")
    HIGHSCORE.setSize(20)
    ITENS_HIGHSCORE.append(HIGHSCORE)

    CAIXASOMBRA= Rectangle(Point(42,182), Point(512, 552))
    CAIXASOMBRA.setOutline("blue")
    CAIXASOMBRA.setWidth(4)
    ITENS_HIGHSCORE.append(CAIXASOMBRA)
    CAIXANOMES = Rectangle(Point(40,180), Point(510, 550))
    CAIXANOMES.setFill("#25262C")
    CAIXANOMES.setOutline("white")
    CAIXANOMES.setWidth(4)
    ITENS_HIGHSCORE.append(CAIXANOMES)

    if lista_Highscores != "None":
        y_pos = 220
        for item in lista_Highscores:

            NOMESOMBRA = Text(Point(152, y_pos+2), f"{item[0]}")
            NOMESOMBRA.setTextColor("blue")
            NOMESOMBRA.setFace("terminal")
            NOMESOMBRA.setStyle("bold italic")
            NOMESOMBRA.setSize(20)
            ITENS_HIGHSCORE.append(NOMESOMBRA)
            NOME = Text(Point(150, y_pos), f"{item[0]}")
            NOME.setFace("terminal")
            NOME.setTextColor("yellow")
            NOME.setStyle("bold italic")
            NOME.setSize(20)
            ITENS_HIGHSCORE.append(NOME)

            SETASOMBRA = Text(Point(282, y_pos-3), f"→")
            SETASOMBRA.setTextColor("blue")
            SETASOMBRA.setFace("poppins")
            SETASOMBRA.setStyle("bold italic")
            SETASOMBRA.setSize(20)
            ITENS_HIGHSCORE.append(SETASOMBRA)
            SETA = Text(Point(280, y_pos-5), f"→")
            SETA.setFace("poppins")
            SETA.setTextColor("white")
            SETA.setStyle("bold italic")
            SETA.setSize(20)
            ITENS_HIGHSCORE.append(SETA)

            SCORESOMBRA = Text(Point(412, y_pos+2), f"{item[1]}")
            SCORESOMBRA.setTextColor("blue")
            SCORESOMBRA.setFace("terminal")
            SCORESOMBRA.setStyle("bold italic")
            SCORESOMBRA.setSize(20)
            ITENS_HIGHSCORE.append(SCORESOMBRA)
            SCORE = Text(Point(410, y_pos), f"{item[1]}")
            SCORE.setFace("terminal")
            SCORE.setTextColor("white")
            SCORE.setStyle("bold italic")
            SCORE.setSize(20)
            ITENS_HIGHSCORE.append(SCORE)

            y_pos += 70
        
    else:

        y_pos = 220
        while y_pos < 520:

            NOMESOMBRA = Text(Point(152, y_pos+2), f"--")
            NOMESOMBRA.setTextColor("blue")
            NOMESOMBRA.setFace("terminal")
            NOMESOMBRA.setStyle("bold italic")
            NOMESOMBRA.setSize(20)
            ITENS_HIGHSCORE.append(NOMESOMBRA)
            NOME = Text(Point(150, y_pos), f"--")
            NOME.setFace("terminal")
            NOME.setTextColor("yellow")
            NOME.setStyle("bold italic")
            NOME.setSize(20)
            ITENS_HIGHSCORE.append(NOME)

            SETASOMBRA = Text(Point(282, y_pos+2), f"->")
            SETASOMBRA.setTextColor("blue")
            SETASOMBRA.setFace("terminal")
            SETASOMBRA.setStyle("bold italic")
            SETASOMBRA.setSize(20)
            ITENS_HIGHSCORE.append(SETASOMBRA)
            SETA = Text(Point(280, y_pos), f"->")
            SETA.setFace("terminal")
            SETA.setTextColor("white")
            SETA.setStyle("bold italic")
            SETA.setSize(20)
            ITENS_HIGHSCORE.append(SETA)

            SCORESOMBRA = Text(Point(412, y_pos+2), f"--")
            SCORESOMBRA.setTextColor("blue")
            SCORESOMBRA.setFace("terminal")
            SCORESOMBRA.setStyle("bold italic")
            SCORESOMBRA.setSize(20)
            ITENS_HIGHSCORE.append(SCORESOMBRA)
            SCORE = Text(Point(410, y_pos), f"--")
            SCORE.setFace("terminal")
            SCORE.setTextColor("YELLOW")
            SCORE.setStyle("bold italic")
            SCORE.setSize(20)
            ITENS_HIGHSCORE.append(SCORE)

            y_pos += 70

    VOLTAR = Rectangle(Point(160, 600), Point(400, 640))
    VOLTAR.setFill("blue") #EEE8AA
    VOLTAR.setOutline("white")
    VOLTAR.setWidth(1)
    ITENS_HIGHSCORE.append(VOLTAR)
    VOLTAR_PALAVRA = Text(Point(280, 620), "VOLTAR")
    VOLTAR_PALAVRA.setTextColor("white")
    VOLTAR_PALAVRA.setFace("terminal")
    VOLTAR_PALAVRA.setStyle("bold italic")
    VOLTAR_PALAVRA.setSize(20)
    ITENS_HIGHSCORE.append(VOLTAR_PALAVRA)



    for item in ITENS_HIGHSCORE:
        item.draw(win)

    done = False
    while not done:

        key = win.checkKey()
        if key == "Escape":
            for item in ITENS_HIGHSCORE:
                        item.undraw()

            return "VOLTAR"
    
        click = win.checkMouse()
        if click != None:
            mouse_x = click.getX()
            mouse_y = click.getY()


            if mouse_x >= 160 and mouse_x <= 400 and mouse_y >= 600 and mouse_y <= 640:
                    
                    for item in ITENS_HIGHSCORE:
                        item.undraw()

                    return "VOLTAR"
            




def organizaScores():
    #RETIRAMOS OS HIGHSCORES
    highscore_Arquivo = open("Highscores\highscores.csv", "r", encoding="utf-8")
    lista_ArquivoHighscores = highscore_Arquivo.readlines()
    highscore_Arquivo.close()

    if len(lista_ArquivoHighscores) > 0:

        lista_Highscores = []

        for item in lista_ArquivoHighscores:
            linha = item[0:-1]
            uma_lista = linha.split(";") 
            lista_Highscores.append(uma_lista)

        #del(lista_Highscores[-1])
        #

        dicionarioUsuarios = {}

        apenasPontuacoes = []
        for item in lista_Highscores:
            apenasPontuacoes.append(int(item[1]))

            #Adicionamos no dicionário o "score" como chave para o "nome":
            key, value = item[1], item[0]
            dicionarioUsuarios[key] = value

        #Ordenamos a lista, dos maiores para os menores:
        apenasPontuacoes = sorted(apenasPontuacoes, reverse=True)

        #Com o dicionário, achamos os nomes dos 5 maiores scores:
        lista_Final = []

        cont = 0

        #Se a lista de pontuações for maior do que 5, limitamos o while em 5:
        if len(apenasPontuacoes) >= 5:
            while cont < 5:
                uma_lista = [f'{dicionarioUsuarios[str(apenasPontuacoes[cont])]}',f'{str(apenasPontuacoes[cont])}']

                lista_Final.append(uma_lista)

                cont += 1

            return(lista_Final)
        
        #Se a lista de pontuações for menor do que 5, pegamos todos:
        else:
            while cont < len(apenasPontuacoes):
                uma_lista = [f'{dicionarioUsuarios[str(apenasPontuacoes[cont])]}',f'{str(apenasPontuacoes[cont])}']

                lista_Final.append(uma_lista)

                cont += 1
            
            cont = len(lista_Final)
            while cont < 5:
                lista_Final.append(["--","--"])
                cont += 1

            return(lista_Final)
    
    else:
        return("None")

    

    

            
                    


    