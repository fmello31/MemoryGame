from controller import verification


def size(columms,lines):
    list = []
    for c in range( 0, lines ):
        for j in range( 0, columms ):
            n = input( f'Linha[{c + 1}] Coluna[{j + 1}]: ' )
            if not verification.verify_numbers(n):
                list.append(n)
    return list