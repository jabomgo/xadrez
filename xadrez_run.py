tabuleiro = [[0 for _ in range(8)] for _ in range(8)]

def mostra_tabuleiro():
    for linha in range(tabuleiro.__len__()):
        formater = []
        for coluna in range(tabuleiro.__len__()):
            formater.append(tabuleiro[linha][coluna].__str__())
        print(f'{linha} {formater}')

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
    
class Dama(Peca):
    def movimento_valido(self, linha_destino, coluna_destino):
        return super().movimento_valido(linha_destino, coluna_destino)
    
    def __str__(self) -> str:
        return 'Dama '+ self.cor
    
class Bispo(Peca):
    def movimento_valido(self, linha_destino, coluna_destino):
        return super().movimento_valido(linha_destino, coluna_destino)
    
    def __str__(self) -> str:
        return 'Bispo '+ self.cor
    
def preparar_tabuleiro():
    #preparar a logica para colocar todas as peças nos lugares corretos
    #logica para os peoes
    for linha in range(tabuleiro.__len__()):
        #tabuleiro acima
        if linha == 1:
            for coluna in range(tabuleiro.__len__()):
                tabuleiro[linha][coluna] = Peao('branco', linha, coluna)
        #tabuleiro baixo
        if linha == 6:
            for coluna in range(tabuleiro.__len__()):
                tabuleiro[linha][coluna] = Peao('preto', linha, coluna)
    
    #demais peças colocar aqui com a posição correta manualmente

    tabuleiro[0][0] = Torre('branco', 0, 0)
    tabuleiro[0][7] = Torre('branco', 0, 7)

    tabuleiro[0][1] = Cavalo('branco', 0, 1)
    tabuleiro[0][6] = Cavalo('branco', 0, 6)

    tabuleiro[0][2] = Bispo('branco', 0, 2)
    tabuleiro[0][5] = Bispo('branco', 0, 5)

    tabuleiro[0][3] = Rei('branco', 0,3)
    tabuleiro[0][4] = Dama('branco', 0,4)

    #outro lado

    tabuleiro[7][0] = Torre('preto', 7, 0)
    tabuleiro[7][7] = Torre('preto', 7, 7)

    tabuleiro[7][1] = Cavalo('preto', 7, 1)
    tabuleiro[7][6] = Cavalo('preto', 7, 6)

    tabuleiro[7][2] = Bispo('preto', 7,2)
    tabuleiro[7][5] = Bispo('preto', 7,5)

    tabuleiro[7][3] = Rei('preto', 7,3)
    tabuleiro[7][4] = Dama('preto', 7, 4)

# main game

preparar_tabuleiro()
mostra_tabuleiro()
