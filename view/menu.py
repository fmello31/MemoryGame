

def mostraLinhas():
    print('\033[30m-\033[m' * 80)


def gerarMenu(lista_opcoes, titulo, mensagem_selecao):  # GERAR MENU DE OPÇÕES
    mostraLinhas()
    print('               \033[0;34m',titulo,'\033[m')
    mostraLinhas()
    indice = 1
    for item in lista_opcoes:
        print(f'\033[0;34m{indice}\033[m - {item}')
        indice += 1
    mostraLinhas()
    opcao = lerInt( mensagem_selecao )
    return opcao


def lerInt(mensagem):  # CRIAR INPUT COM NÚMERO INTEIRO
    while True:
        try:
            opcao = int( input( mensagem ) )
        except (ValueError, TypeError):
            print('\033[31mERRO OPÇÃO INVÁLIDA, DiGITE UM NÚMERO INTEIRO VÁLIDO DENTRE AS OPÇÕES DO MENU !!!!!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO USUÁRIO NÃO DIGITOU NENHUM NÚMERO')
            return 0
        else:
            return opcao


def size():   #ADAPTA O MENU PARA EXIBIR AS OPÇÕES DE ESCOLHA DO TAMANHO DA TABELA
 opcoes = ['4x4','6x6','8x8','10x10','TO RETURN FOR MENU']
 titulo = 'BOARD SIZE'
 escolha = 'Digite sua opção :'
 menu_tamanho = gerarMenu(opcoes, titulo, escolha)
 return menu_tamanho


def menu_confirmation():
    opcoes = ['SIM', 'NÃO']
    escolha = 'Deseja Confirmar o tabuleiro ? :'
    titulo = 'CONFIRMAÇÃO DE TABULEIRO'
    confirmacao = gerarMenu( opcoes, titulo, escolha )
    return confirmacao