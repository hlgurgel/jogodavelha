import tabuleiro

if __name__ == "__main__":
    while not tabuleiro.finalizado():
        tabuleiro.imprimir()
        comando = input('> ')
        tabuleiro.interpretar_comando(comando)
    else:
        tabuleiro.imprimir()
        print('jogo finalizado :)')
