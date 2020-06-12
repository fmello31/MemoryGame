numero = 65
print(numero)
numero = chr(65)
print(numero)
numero = chr(67)
print(numero)
numero = ord(numero) + 2
print(numero)
numero = chr(numero)
print(numero)

#char - transforma um número em caractere
#ord - transforma um caracter em um número

#tabela ascii - tabela de mapeamento de número inteiros (0 à 127) para caracteres.
#128 carcateres -
#menor unidade de memória é o bit - 2 valores (0 e 1)
# 2 bits = 4 valores
# 3 bits = 2³ = 8
# 2^n
#2 ^ n = 128

letra = 'A'
print(ord(letra))

letra2 = 'C'

dif = ord(letra) - ord(letra2)

print(dif)


palavra1 = 'teste' # [t - 116, e - 101, s- 115, t - 116, e - 101] = 549
palavra2 = 'testa' #  [t - 116, e - 101, s- 115, t - 116, a - 97] = 545

tamp1 = 0
tamp2 = 0

for l in palavra1:
    tamp1 += ord(l)

for l in palavra2:
    tamp2 += ord(l)

print(tamp1)
print(tamp2)

if tamp1 > tamp2:
    print(f'{palavra2}\n{palavra1}')
else:
    print(f'{palavra1}\n{palavra2}')

    


