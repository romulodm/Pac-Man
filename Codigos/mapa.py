MAPA =  [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
        [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
        [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
        [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],
        [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],
        [1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1],
        [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
        [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
        [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
        [1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1],
        [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
        [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
        [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
        [1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
        [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
        [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
        [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]


from graphics import *

def getPositions():
    POSICOES = {

    #LINHA 1    
    "30.0,30.0": "MAPA[1][1]",
    "50.0,30.0": "MAPA[1][2]", 
    "70.0,30.0": "MAPA[1][3]", 
    "90.0,30.0": "MAPA[1][4]",
    "110.0,30.0": "MAPA[1][5]",
    "130.0,30.0": "MAPA[1][6]",
    "150.0,30.0": "MAPA[1][7]",
    "170.0,30.0": "MAPA[1][8]",
    "190.0,30.0": "MAPA[1][9]",
    "210.0,30.0": "MAPA[1][10]",
    "230.0,30.0": "MAPA[1][11]",
    "250.0,30.0": "MAPA[1][12]",
    "310.0,30.0": "MAPA[1][15]",
    "330.0,30.0": "MAPA[1][16]",
    "350.0,30.0": "MAPA[1][17]",
    "370.0,30.0": "MAPA[1][18]",
    "390.0,30.0": "MAPA[1][19]",
    "410.0,30.0": "MAPA[1][20]",
    "430.0,30.0": "MAPA[1][21]",
    "450.0,30.0": "MAPA[1][22]",
    "470.0,30.0": "MAPA[1][23]",
    "490.0,30.0": "MAPA[1][24]",
    "510.0,30.0": "MAPA[1][25]",
    "530.0,30.0": "MAPA[1][26]",

    #LINHA 2
    "30.0,50.0": "MAPA[2][1]",
    "130.0,50.0": "MAPA[2][6]",
    "250.0,50.0": "MAPA[2][12]",
    "310.0,50.0": "MAPA[2][15]",
    "430.0,50.0": "MAPA[2][21]",
    "530.0,50.0": "MAPA[2][26]",

    #LINHA 3
    "30.0,70.0": "MAPA[3][1]",
    "130.0,70.0": "MAPA[3][6]",
    "250.0,70.0": "MAPA[3][12]",
    "310.0,70.0": "MAPA[3][15]",
    "430.0,70.0": "MAPA[3][21]",
    "530.0,70.0": "MAPA[3][26]",

    #LINHA 4
    "30.0,90.0": "MAPA[4][1]",
    "130.0,90.0": "MAPA[4][6]",
    "250.0,90.0": "MAPA[4][12]",
    "310.0,90.0": "MAPA[4][15]",
    "430.0,90.0": "MAPA[4][21]",
    "530.0,90.0": "MAPA[4][26]",

    #LINHA 5
    "30.0,110.0": "MAPA[5][1]",
    "50.0,110.0": "MAPA[5][2]",
    "70.0,110.0": "MAPA[5][3]",
    "90.0,110.0": "MAPA[5][4]",
    "110.0,110.0": "MAPA[5][5]",
    "130.0,110.0": "MAPA[5][6]",
    "150.0,110.0": "MAPA[5][7]",
    "170.0,110.0": "MAPA[5][8]",
    "190.0,110.0": "MAPA[5][9]",
    "210.0,110.0": "MAPA[5][10]",
    "230.0,110.0": "MAPA[5][11]",
    "250.0,110.0": "MAPA[5][12]",
    "270.0,110.0": "MAPA[5][13]",
    "290.0,110.0": "MAPA[5][14]",
    "310.0,110.0": "MAPA[5][15]",
    "330.0,110.0": "MAPA[5][16]",
    "350.0,110.0": "MAPA[5][17]",
    "370.0,110.0": "MAPA[5][18]",
    "390.0,110.0": "MAPA[5][19]",
    "410.0,110.0": "MAPA[5][20]",
    "430.0,110.0": "MAPA[5][21]",
    "450.0,110.0": "MAPA[5][22]",
    "470.0,110.0": "MAPA[5][23]",
    "490.0,110.0": "MAPA[5][24]",
    "510.0,110.0": "MAPA[5][25]",
    "530.0,110.0": "MAPA[5][26]",

    #LINHA 6
    "30.0,130.0": "MAPA[6][1]",
    "130.0,130.0": "MAPA[6][6]",
    "190.0,130.0": "MAPA[6][9]",
    "370.0,130.0": "MAPA[6][18]",
    "430.0,130.0": "MAPA[6][21]",
    "530.0,130.0": "MAPA[6][26]",

    #LINHA 7
    "30.0,150.0": "MAPA[7][1]",
    "130.0,150.0": "MAPA[7][6]",
    "190.0,150.0": "MAPA[7][9]",
    "370.0,150.0": "MAPA[7][18]",
    "430.0,150.0": "MAPA[7][21]",
    "530.0,150.0": "MAPA[7][26]",

    #LINHA 8
    "30.0,170.0": "MAPA[8][1]",
    "50.0,170.0": "MAPA[8][2]",
    "70.0,170.0": "MAPA[8][3]",
    "90.0,170.0": "MAPA[8][4]",
    "110.0,170.0": "MAPA[8][5]",
    "130.0,170.0": "MAPA[8][6]",
    "190.0,170.0": "MAPA[8][9]",
    "210.0,170.0": "MAPA[8][10]",
    "230.0,170.0": "MAPA[8][11]",
    "250.0,170.0": "MAPA[8][12]",
    "310.0,170.0": "MAPA[8][15]",
    "330.0,170.0": "MAPA[8][16]",
    "350.0,170.0": "MAPA[8][17]",
    "370.0,170.0": "MAPA[8][18]",
    "430.0,170.0": "MAPA[8][21]",
    "450.0,170.0": "MAPA[8][22]",
    "470.0,170.0": "MAPA[8][23]",
    "490.0,170.0": "MAPA[8][24]",
    "510.0,170.0": "MAPA[8][25]",
    "530.0,170.0": "MAPA[8][26]",

    #LINHA 9
    "130.0,190.0": "MAPA[9][6]",
    "250.0,190.0": "MAPA[9][12]",
    "310.0,190.0": "MAPA[9][15]",
    "430.0,190.0": "MAPA[9][21]",

    #LINHA 10
    "130.0,210.0": "MAPA[10][6]",
    "250.0,210.0": "MAPA[10][12]",
    "310.0,210.0": "MAPA[10][15]",
    "430.0,210.0": "MAPA[10][21]",

    #LINHA 11
    "130.0,230.0": "MAPA[11][6]",
    "190.0,230.0": "MAPA[11][9]",
    "210.0,230.0": "MAPA[11][10]",
    "230.0,230.0": "MAPA[11][11]",
    "250.0,230.0": "MAPA[11][12]",
    "270.0,230.0": "MAPA[11][13]",
    "290.0,230.0": "MAPA[11][14]",
    "310.0,230.0": "MAPA[11][15]",
    "330.0,230.0": "MAPA[11][16]",
    "350.0,230.0": "MAPA[11][17]",
    "370.0,230.0": "MAPA[11][18]",
    "390.0,230.0": "MAPA[11][17]",
    "410.0,230.0": "MAPA[11][20]",
    "430.0,230.0": "MAPA[11][21]",

    #LINHA 12
    "130.0,250.0": "MAPA[12][6]",
    "190.0,250.0": "MAPA[12][9]",
    "410.0,250.0": "MAPA[12][20]",
    "430.0,250.0": "MAPA[12][21]",

    #LINHA 13
    "130.0,270.0": "MAPA[13][6]",
    "190.0,270.0": "MAPA[13][9]",
    "410.0,270.0": "MAPA[13][20]",
    "430.0,270.0": "MAPA[13][21]",

    #LINHA 14
    "10.0,290.0": "MAPA[14][0]",
    "30.0,290.0": "MAPA[14][1]",
    "50.0,290.0": "MAPA[14][2]",
    "70.0,290.0": "MAPA[14][3]",
    "90.0,290.0": "MAPA[14][4]",
    "110.0,290.0": "MAPA[14][5]",
    "130.0,290.0": "MAPA[14][6]",
    "150.0,290.0": "MAPA[14][7]",
    "170.0,290.0": "MAPA[14][8]",
    "190.0,290.0": "MAPA[14][9]",
    "370.0,290.0": "MAPA[14][18]",
    "390.0,290.0": "MAPA[14][19]",
    "410.0,290.0": "MAPA[14][20]",
    "430.0,290.0": "MAPA[14][21]",
    "450.0,290.0": "MAPA[14][22]",
    "470.0,290.0": "MAPA[14][23]",
    "490.0,290.0": "MAPA[14][24]",
    "510.0,290.0": "MAPA[14][25]",
    "530.0,290.0": "MAPA[14][26]",
    "550.0,290.0": "MAPA[14][27]",

    #LINHA 15
    "130.0,310.0": "MAPA[15][6]",
    "190.0,310.0": "MAPA[15][9]",
    "410.0,310.0": "MAPA[15][20]",
    "430.0,310.0": "MAPA[15][21]",

    #LINHA 16
    "130.0,330.0": "MAPA[16][6]",
    "190.0,330.0": "MAPA[16][9]",
    "410.0,330.0": "MAPA[16][20]",
    "430.0,330.0": "MAPA[16][21]",

    #LINHA 17
    "130.0,350.0": "MAPA[17][6]",
    "190.0,350.0": "MAPA[17][9]",
    "210.0,350.0": "MAPA[17][10]",
    "230.0,350.0": "MAPA[17][11]",
    "250.0,350.0": "MAPA[17][12]",
    "270.0,350.0": "MAPA[17][13]",
    "290.0,350.0": "MAPA[17][14]",
    "310.0,350.0": "MAPA[17][15]",
    "330.0,350.0": "MAPA[17][16]",
    "350.0,350.0": "MAPA[17][17]",
    "370.0,350.0": "MAPA[17][18]",
    "390.0,350.0": "MAPA[17][19]",
    "430.0,350.0": "MAPA[17][21]",

    #LINHA 18
    "130.0,370.0": "MAPA[18][6]",
    "190.0,370.0": "MAPA[18][9]",
    "410.0,370.0": "MAPA[18][20]",
    "430.0,370.0": "MAPA[18][21]",

    #LINHA 19
    "130.0,390.0": "MAPA[19][6]",
    "190.0,390.0": "MAPA[19][9]",
    "410.0,390.0": "MAPA[19][20]",
    "430.0,390.0": "MAPA[19][21]",

    #LINHA 20
    "30.0,410.0": "MAPA[20][1]",
    "50.0,410.0": "MAPA[20][2]",
    "70.0,410.0": "MAPA[20][3]",
    "90.0,410.0": "MAPA[20][4]",
    "110.0,410.0": "MAPA[20][5]",
    "130.0,410.0": "MAPA[20][6]",
    "150.0,410.0": "MAPA[20][7]",
    "170.0,410.0": "MAPA[20][8]",
    "190.0,410.0": "MAPA[20][9]",
    "210.0,410.0": "MAPA[20][10]",
    "230.0,410.0": "MAPA[20][11]",
    "250.0,410.0": "MAPA[20][12]",
    "310.0,410.0": "MAPA[20][15]",
    "330.0,410.0": "MAPA[20][16]",
    "350.0,410.0": "MAPA[20][17]",
    "370.0,410.0": "MAPA[20][18]",
    "390.0,410.0": "MAPA[20][19]",
    "410.0,410.0": "MAPA[20][20]",
    "430.0,410.0": "MAPA[20][21]",
    "450.0,410.0": "MAPA[20][22]",
    "470.0,410.0": "MAPA[20][23]",
    "490.0,410.0": "MAPA[20][24]",
    "510.0,410.0": "MAPA[20][25]",
    "530.0,410.0": "MAPA[20][26]",

    #LINHA 21
    "30.0,430.0": "MAPA[21][1]",
    "130.0,430.0": "MAPA[21][6]",
    "250.0,430.0": "MAPA[21][12]",
    "310.0,430.0": "MAPA[21][15]",
    "430.0,430.0": "MAPA[21][21]",
    "530.0,430.0": "MAPA[21][26]",

    #LINHA 22
    "30.0,450.0": "MAPA[22][1]",
    "130.0,450.0": "MAPA[22][6]",
    "250.0,450.0": "MAPA[22][12]",
    "310.0,450.0": "MAPA[22][15]",
    "430.0,450.0": "MAPA[22][21]",
    "530.0,450.0": "MAPA[22][26]",

    #LINHA 23
    "30.0,470.0": "MAPA[23][1]",
    "50.0,470.0": "MAPA[23][2]",
    "70.0,470.0": "MAPA[23][3]",
    "130.0,470.0": "MAPA[23][6]",
    "150.0,470.0": "MAPA[23][7]",
    "170.0,470.0": "MAPA[23][8]",
    "190.0,470.0": "MAPA[23][9]",
    "210.0,470.0": "MAPA[23][10]",
    "230.0,470.0": "MAPA[23][11]",
    "250.0,470.0": "MAPA[23][12]",
    "270.0,470.0": "MAPA[23][13]",
    "290.0,470.0": "MAPA[23][14]",
    "310.0,470.0": "MAPA[23][15]",
    "330.0,470.0": "MAPA[23][16]",
    "350.0,470.0": "MAPA[23][17]",
    "370.0,470.0": "MAPA[23][18]",
    "390.0,470.0": "MAPA[23][19]",
    "410.0,470.0": "MAPA[23][20]",
    "430.0,470.0": "MAPA[23][21]",
    "490.0,470.0": "MAPA[23][24]",
    "510.0,470.0": "MAPA[23][25]",
    "530.0,470.0": "MAPA[23][26]",

    #LINHA 24
    "70.0,490.0": "MAPA[24][3]",
    "130.0,490.0": "MAPA[24][6]",
    "190.0,490.0": "MAPA[24][9]",
    "370.0,490.0": "MAPA[24][18]",
    "430.0,490.0": "MAPA[24][21]",
    "490.0,490.0": "MAPA[24][24]",

    #LINHA 25
    "70.0,510.0": "MAPA[25][3]",
    "130.0,510.0": "MAPA[25][6]",
    "190.0,510.0": "MAPA[25][9]",
    "370.0,510.0": "MAPA[25][18]",
    "430.0,510.0": "MAPA[25][21]",
    "490.0,510.0": "MAPA[25][24]",

    #LINHA 26
    "30.0,530.0": "MAPA[26][1]",
    "50.0,530.0": "MAPA[26][2]",
    "70.0,530.0": "MAPA[26][3]",
    "90.0,530.0": "MAPA[26][4]",
    "110.0,530.0": "MAPA[26][5]",
    "130.0,530.0": "MAPA[26][6]",
    "190.0,530.0": "MAPA[26][9]",
    "210.0,530.0": "MAPA[26][10]",
    "230.0,530.0": "MAPA[26][11]",
    "250.0,530.0": "MAPA[26][12]",
    "310.0,530.0": "MAPA[26][15]",
    "330.0,530.0": "MAPA[26][16]",
    "350.0,530.0": "MAPA[26][17]",
    "370.0,530.0": "MAPA[26][18]",
    "430.0,530.0": "MAPA[26][21]",
    "450.0,530.0": "MAPA[26][22]",
    "470.0,530.0": "MAPA[26][23]",
    "490.0,530.0": "MAPA[26][24]",
    "510.0,530.0": "MAPA[26][25]",
    "530.0,530.0": "MAPA[26][26]",

    #LINHA 27
    "30.0,550.0": "MAPA[27][1]",
    "250.0,550.0": "MAPA[27][12]",
    "310.0,550.0": "MAPA[27][15]",
    "530.0,550.0": "MAPA[27][26]",

    #LINHA 28
    "30.0,570.0": "MAPA[28][1]",
    "250.0,570.0": "MAPA[28][12]",
    "310.0,570.0": "MAPA[28][15]",
    "530.0,570.0": "MAPA[28][26]",

    #LINHA 29
    "30.0,590.0": "MAPA[29][1]",
    "50.0,590.0": "MAPA[29][2]",
    "70.0,590.0": "MAPA[29][3]",
    "90.0,590.0": "MAPA[29][4]",
    "110.0,590.0": "MAPA[29][5]",
    "130.0,590.0": "MAPA[29][6]",
    "150.0,590.0": "MAPA[29][7]",
    "170.0,590.0": "MAPA[29][8]",
    "190.0,590.0": "MAPA[29][9]",
    "210.0,590.0": "MAPA[29][10]",
    "230.0,590.0": "MAPA[29][11]",
    "250.0,590.0": "MAPA[29][12]",
    "270.0,590.0": "MAPA[29][13]",
    "290.0,590.0": "MAPA[29][14]",
    "310.0,590.0": "MAPA[29][15]",
    "330.0,590.0": "MAPA[29][16]",
    "350.0,590.0": "MAPA[29][17]",
    "370.0,590.0": "MAPA[29][18]",
    "390.0,590.0": "MAPA[29][19]",
    "410.0,590.0": "MAPA[29][20]",
    "430.0,590.0": "MAPA[29][21]",
    "450.0,590.0": "MAPA[29][22]", 
    "470.0,590.0": "MAPA[29][23]",
    "490.0,590.0": "MAPA[29][24]",
    "510.0,590.0": "MAPA[29][25]",
    "530.0,590.0": "MAPA[29][26]"}

    return(POSICOES)

def getPosComidas():
    POSICOES_COMIDAS = {
        "30.0,30.0": 1,
        "50.0,30.0": 2,
        "70.0,30.0": 3,
        "90.0,30.0": 4,
        "110.0,30.0": 5,
        "130.0,30.0": 6,
        "150.0,30.0": 7,
        "170.0,30.0": 8,
        "190.0,30.0": 9,
        "210.0,30.0": 10,
        "230.0,30.0": 11,
        "250.0,30.0": 12,
        "310.0,30.0": 13,
        "330.0,30.0": 14,
        "350.0,30.0": 15,
        "370.0,30.0": 16,
        "390.0,30.0": 17,
        "410.0,30.0": 18,
        "430.0,30.0": 19,
        "450.0,30.0": 20,
        "470.0,30.0": 21,
        "490.0,30.0": 22,
        "510.0,30.0": 23,
        "530.0,30.0": 24,
        "30.0,50.0": 25,
        "130.0,50.0": 26,
        "250.0,50.0": 27,
        "310.0,50.0": 28,
        "430.0,50.0": 29,
        "530.0,50.0": 30,
        "130.0,70.0": 31,
        "250.0,70.0": 32,
        "310.0,70.0": 33,
        "430.0,70.0": 34,
        "30.0,90.0": 35,
        "130.0,90.0": 36,
        "250.0,90.0": 37,
        "310.0,90.0": 38,
        "430.0,90.0": 39,
        "530.0,90.0": 40,
        "30.0,110.0": 41,
        "50.0,110.0": 42,
        "70.0,110.0": 43,
        "90.0,110.0": 44,
        "110.0,110.0": 45,
        "130.0,110.0": 46,
        "150.0,110.0": 47,
        "170.0,110.0": 48,
        "190.0,110.0": 49,
        "210.0,110.0": 50,
        "230.0,110.0": 51,
        "250.0,110.0": 52,
        "270.0,110.0": 53,
        "290.0,110.0": 54,
        "310.0,110.0": 55,
        "330.0,110.0": 56,
        "350.0,110.0": 57,
        "370.0,110.0": 58,
        "390.0,110.0": 59,
        "410.0,110.0": 60,
        "430.0,110.0": 61,
        "450.0,110.0": 62,
        "470.0,110.0": 63,
        "490.0,110.0": 64,
        "510.0,110.0": 65,
        "530.0,110.0": 66,
        "30.0,130.0": 67,
        "130.0,130.0": 68,
        "190.0,130.0": 69,
        "370.0,130.0": 70,
        "430.0,130.0": 71,
        "530.0,130.0": 72,
        "30.0,150.0": 73,
        "130.0,150.0": 74,
        "190.0,150.0": 75,
        "370.0,150.0": 76,
        "430.0,150.0": 77,
        "530.0,150.0": 78,
        "30.0,170.0": 79,
        "50.0,170.0": 80,
        "70.0,170.0": 81,
        "90.0,170.0": 82,
        "110.0,170.0": 83,
        "130.0,170.0": 84,
        "190.0,170.0": 85,
        "210.0,170.0": 86,
        "230.0,170.0": 87,
        "250.0,170.0": 88,
        "310.0,170.0": 89,
        "330.0,170.0": 90,
        "350.0,170.0": 91,
        "370.0,170.0": 92,
        "430.0,170.0": 93,
        "450.0,170.0": 94,
        "470.0,170.0": 95,
        "490.0,170.0": 96,
        "510.0,170.0": 97,
        "530.0,170.0": 98,
        "130.0,190.0": 99,
        "430.0,190.0": 100,
        "130.0,210.0": 101,
        "430.0,210.0": 102,
        "130.0,230.0": 103,
        "430.0,230.0": 104,
        "130.0,250.0": 105,
        "430.0,250.0": 106,
        "130.0,270.0": 107,
        "430.0,270.0": 108,
        "0.0,0.0": 0,
        "0.0,0.0": 0,
        "130.0,290.0": 111,
        "430.0,290.0": 112,
        "130.0,310.0": 113,
        "430.0,310.0": 114,
        "130.0,330.0": 115,
        "430.0,330.0": 116,
        "130.0,350.0": 117,
        "430.0,350.0": 118,
        "130.0,370.0": 119,
        "430.0,370.0": 120,
        "130.0,390.0": 121,
        "430.0,390.0": 122,
        "30.0,410.0": 123,
        "50.0,410.0": 124,
        "70.0,410.0": 125,
        "90.0,410.0": 126,
        "110.0,410.0": 127,
        "130.0,410.0": 128,
        "150.0,410.0": 129,
        "170.0,410.0": 130,
        "190.0,410.0": 131,
        "210.0,410.0": 132,
        "230.0,410.0": 133,
        "250.0,410.0": 134,
        "310.0,410.0": 135,
        "330.0,410.0": 136,
        "350.0,410.0": 137,
        "370.0,410.0": 138,
        "390.0,410.0": 139,
        "410.0,410.0": 140,
        "430.0,410.0": 141,
        "450.0,410.0": 142,
        "470.0,410.0": 143,
        "490.0,410.0": 144,
        "510.0,410.0": 145,
        "530.0,410.0": 146,
        "30.0,430.0": 147,
        "130.0,430.0": 148,
        "250.0,430.0": 149,
        "310.0,430.0": 150,
        "430.0,430.0": 151,
        "530.0,430.0": 152,
        "30.0,450.0": 153,
        "130.0,450.0": 154,
        "250.0,450.0": 155,
        "310.0,450.0": 156,
        "430.0,450.0": 157,
        "530.0,450.0": 158,
        "50.0,470.0": 159,
        "70.0,470.0": 160,
        "130.0,470.0": 161,
        "150.0,470.0": 162,
        "170.0,470.0": 163,
        "190.0,470.0": 164,
        "210.0,470.0": 165,
        "230.0,470.0": 166,
        "250.0,470.0": 167,
        "270.0,470.0": 168,
        "290.0,470.0": 169,
        "310.0,470.0": 170,
        "330.0,470.0": 171,
        "350.0,470.0": 172,
        "370.0,470.0": 173,
        "390.0,470.0": 174,
        "410.0,470.0": 175,
        "430.0,470.0": 176,
        "490.0,470.0": 177,
        "510.0,470.0": 178,
        "70.0,490.0": 179,
        "130.0,490.0": 180,
        "190.0,490.0": 181,
        "370.0,490.0": 182,
        "430.0,490.0": 183,
        "490.0,490.0": 184,
        "70.0,510.0": 185,
        "130.0,510.0": 186,
        "190.0,510.0": 187,
        "370.0,510.0": 188,
        "430.0,510.0": 189,
        "490.0,510.0": 190,
        "30.0,530.0": 191,
        "50.0,530.0": 192,
        "70.0,530.0": 193,
        "90.0,530.0": 194,
        "110.0,530.0": 195,
        "130.0,530.0": 196,
        "190.0,530.0": 197,
        "210.0,530.0": 198,
        "230.0,530.0": 199,
        "250.0,530.0": 200,
        "310.0,530.0": 201,
        "330.0,530.0": 202,
        "350.0,530.0": 203,
        "370.0,530.0": 204,
        "430.0,530.0": 205,
        "450.0,530.0": 206,
        "470.0,530.0": 207,
        "490.0,530.0": 208,
        "510.0,530.0": 209,
        "530.0,530.0": 210,
        "30.0,550.0": 211,
        "250.0,550.0": 212,
        "310.0,550.0": 213,
        "530.0,550.0": 214,
        "30.0,570.0": 215,
        "250.0,570.0": 216,
        "310.0,570.0": 217,
        "530.0,570.0": 218,
        "30.0,590.0": 219,
        "50.0,590.0": 220,
        "70.0,590.0": 221,
        "90.0,590.0": 222,
        "110.0,590.0": 223,
        "130.0,590.0": 224,
        "150.0,590.0": 225,
        "170.0,590.0": 226,
        "190.0,590.0": 227,
        "210.0,590.0": 228,
        "230.0,590.0": 229,
        "250.0,590.0": 230,
        "310.0,590.0": 231,
        "330.0,590.0": 232,
        "350.0,590.0": 233,
        "370.0,590.0": 234,
        "390.0,590.0": 235,
        "410.0,590.0": 236,
        "430.0,590.0": 237,
        "450.0,590.0": 238,
        "470.0,590.0": 239,
        "490.0,590.0": 240,
        "510.0,590.0": 241,
        "530.0,590.0": 242,}

    return(POSICOES_COMIDAS)


def getPosEspeciais():

    POSICOES_ESPECIAIS = {
    "30.0,70.0": 0,
    "530.0,70.0": 1,
    "30.0,470.0": 2,
    "530.0,470.0": 3    
    }
    
    return(POSICOES_ESPECIAIS)