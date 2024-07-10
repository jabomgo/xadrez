tabuleiro = [[0 for _ in range(8)] for _ in range(8)]

def mostra_tabuleiro():
    for linha in tabuleiro:
        print(linha)

class Peca:
    def __init__(self, cor, linha_atual, coluna_atual):
        self.cor = cor
        self.linha_atual = linha_atual
        self. coluna_atual = coluna_atual

    def movimento_valido(self, linha_destino, coluna_destino):
        raise NotImplementedError("Metodo deve ser implementado nas subclasses")
    

class Peao(Peca):
    def movimento_valido(self, linha_destino, coluna_destino):
        return super().movimento_valido(linha_destino, coluna_destino)
    
    def __str__(self) -> str:
        return 'Peão '+ self.cor
    
class Rei(Peca):
    def movimento_valido(self, linha_destino, coluna_destino):
        return super().movimento_valido(linha_destino, coluna_destino)

    def __str__(self) -> str:
        return 'Rei '+ self.cor

class Torre(Peca):
    def movimento_valido(self, linha_destino, coluna_destino):
        return super().movimento_valido(linha_destino, coluna_destino)
    
    def __str__(self) -> str:
        return 'Torre '+ self.cor
    
class Cavalo(Peca):
    def movimento_valido(self, linha_destino, coluna_destino):
        return super().movimento_valido(linha_destino, coluna_destino)
    
    def __str__(self) -> str:
        return 'Cavalo '+ self.cor
    
class Rainha(Peca):
    def movimento_valido(self, linha_destino, coluna_destino):
        return super().movimento_valido(linha_destino, coluna_destino)
    
    def __str__(self) -> str:
        return 'Rainha '+ self.cor
    
def preparar_tabuleiro():
    #preparar a logica para colocar todas as peças nos lugares corretos
    #logica para os peoes
    for linha in range(tabuleiro.__len__()):
        #tabuleiro acima
        if linha == 1:
            for coluna in range(tabuleiro.__len__()):
                tabuleiro[linha][coluna] = 'peao'
        #tabuleiro baixo
        if linha == 6:
            for coluna in range(tabuleiro.__len__()):
                tabuleiro[linha][coluna] = 'peao'
    
    #demais peças colocar aqui com a posição correta manualmente

    tabuleiro[0][0] = 'torre'
    tabuleiro[0][7] = 'torre'

    tabuleiro[0][1] = 'cavalo'
    tabuleiro[0][6] = 'cavalo'

    tabuleiro[0][2] = 'bispo'
    tabuleiro[0][5] = 'bispo'

    tabuleiro[0][3] = 'rei'
    tabuleiro[0][4] = 'dama'

    #outro lado

    tabuleiro[7][0] = 'torre'
    tabuleiro[7][7] = 'torre'

    tabuleiro[7][1] = 'cavalo'
    tabuleiro[7][6] = 'cavalo'

    tabuleiro[7][2] = 'bispo'
    tabuleiro[7][5] = 'bispo'

    tabuleiro[7][3] = 'rei'
    tabuleiro[7][4] = 'dama'

# main game

preparar_tabuleiro()
mostra_tabuleiro()

peao = Peao('branco', 1,2)

rainha = Rainha('preto', 1, 1)
print(peao)
print(rainha)
