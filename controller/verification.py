def verify_numbers(n):
    n = n.upper()
    if n.isdigit():
        print('error')
    else:
        return False


def verify_pairs(lista,columms):
    conj_caracteres = set()
    for item in lista:
        if lista.count(item) == 2:
            conj_caracteres.add(item)

    qtd_caracteres = len(conj_caracteres)
    limit = pow(columms, 2) / 2
    if qtd_caracteres == limit:
        return True
    else:
        return ValueError('O número de caracteres para pares é insuficiente.')

