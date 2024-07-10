tabuleiro = [[0 for _ in range(8)] for _ in range(8)]

def mostra_tabuleiro():
    for linha in tabuleiro:
        print(linha)

def preparar_tabuleiro():
    #preparar a logica para colocar todas as peças nos lugares corretos
    #logica para os peoes
    for linha in range(tabuleiro.__len__()):
        if linha == 1:
            for coluna in range(tabuleiro.__len__()):
                tabuleiro[linha][coluna] = 1

        if linha == 6:
            for coluna in range(tabuleiro.__len__()):
                tabuleiro[linha][coluna] = 1
    
    #demais peças colocar aqui com a posição correta manualmente


# main game

preparar_tabuleiro()
mostra_tabuleiro()