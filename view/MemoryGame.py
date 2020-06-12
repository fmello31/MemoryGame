from view import menu
from view import sizeGame
from controller import verification


opcoes = ['MANUAL','AUTOMATIC','QUIT']
titulo = 'WELCOME TO THE MEMORY GAME'
escolha = 'Escolha a funcionalidade do menu que quer acessar:'


resposta = menu.gerarMenu(opcoes,titulo,escolha)
sysout = True

while sysout:
    if resposta == 1:
        if menu.size() == 1:
            lista = sizeGame.size(columms=4,lines=4)
            if menu.menu_confirmation() == 1:
                if verification.verify_pairs(lista, columms=4) == True:
                    print('Tabuleiro Confirmado, VaMOS COMEÇAR  PARTIDA')

                else:
                    print('Tabuleiro incorreto')
    elif menu.size() == 2:
        lista = sizeGame.size(columms=6,lines=6)
        if menu.menu_confirmation() == 1:
            if verification.verify_pairs( lista, columms=6 ) == True:
                print( 'Tabuleiro Confirmado, VaMOS COMEÇAR  PARTIDA' )
            else:
                print( 'Tabuleiro incorreto' )
    elif menu.size() == 3:
        lista = sizeGame.size(columms=8,lines=8)
        if menu.menu_confirmation() == 1:
            if verification.verify_pairs( lista, columms=8 ) == True:
                print( 'Tabuleiro Confirmado, VaMOS COMEÇAR  PARTIDA' )
            else:
                print( 'Tabuleiro incorreto' )
    elif menu.size() == 4:
        lista = sizeGame.size(columms=10,lines=10)
        if menu.menu_confirmation() == 1:
            if verification.verify_pairs( lista, columms=10 ) == True:
                print( 'Tabuleiro Confirmado, VaMOS COMEÇAR  PARTIDA' )
            else:
                print( 'Tabuleiro incorreto' )
    elif resposta == 3:
        sysout = False
