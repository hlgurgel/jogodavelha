import re


tabuleiro = ['_' for i in range(9)]


def imprimir():
    for posicao_tabuleiro in range(1,10):
        print(tabuleiro[posicao_tabuleiro-1], end=' ')
        if not posicao_tabuleiro % 3:
            print('')


def finalizado():
    if tabuleiro[0] != '_' and tabuleiro[0]==tabuleiro[1]==tabuleiro[2] or \
       tabuleiro[3] != '_' and tabuleiro[3]==tabuleiro[4]==tabuleiro[5] or \
       tabuleiro[6] != '_' and tabuleiro[6]==tabuleiro[7]==tabuleiro[8]:
           return True
    elif tabuleiro[0] != '_' and tabuleiro[0]==tabuleiro[3]==tabuleiro[6] or \
         tabuleiro[1] != '_' and tabuleiro[1]==tabuleiro[4]==tabuleiro[7] or \
         tabuleiro[2] != '_' and tabuleiro[2]==tabuleiro[5]==tabuleiro[8]:
           return True
    elif tabuleiro[0] != '_' and tabuleiro[0]==tabuleiro[4]==tabuleiro[8] or \
         tabuleiro[2] != '_' and tabuleiro[2]==tabuleiro[4]==tabuleiro[6]:
           return True
    return False


def interpretar_comando(comando):
    if comando=='q':
        print('jogo finalizado')
        exit(0)
    elif re.compile(r'[1-3],[1-3] [xo]').match(comando):
        linha = int(comando[0])
        coluna = int(comando[2])
        posicao = ((linha-1)*3) + coluna - 1
        if tabuleiro[posicao] != '_':
            print('casa já preenchida')
        else:
            valor = comando[4]
            tabuleiro[posicao] = valor
    else:
        print('comando não reconhecido')
