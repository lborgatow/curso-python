"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segundo digito
"""


def multiplica_1(cnpj):
    lista1_cnpj = [int(cnpj[d]) * i for d, i in enumerate(range(5, 1, -1))]
    lista_1b = [int(cnpj[d + 4]) * i for d, i in enumerate(range(9, 1, -1))]
    lista1_cnpj.extend(lista_1b)
    return lista1_cnpj


def multiplica_2(cnpj):
    lista2_cnpj = [int(cnpj[d]) * i for d, i in enumerate(range(6, 1, -1))]
    lista_2b = [int(cnpj[d + 5]) * i for d, i in enumerate(range(9, 1, -1))]
    lista2_cnpj.extend(lista_2b)
    return lista2_cnpj


def obter_digitos(lista1_cnpj, lista2_cnpj):
    d1 = 11 - ((sum(lista1_cnpj)) % 11)
    d2 = 11 - ((sum(lista2_cnpj)) % 11)

    if d1 > 9:
        d1 = 0
    if d2 > 9:
        d2 = 0

    return d1, d2


def verificar_cnpj(d1, d2):
    if d1 == int(cnpj[12]) and d2 == int(cnpj[13]):
        print("CNPJ VÁLIDO!")
    else:
        print("CNPJ INVÁLIDO!")


print(('=' * 12) + " CONSULTA DE CNPJ " + ('=' * 12))
print(('=' * 8) + " (digite 'q' para parar) " + ('=' * 9))
while True:
    cnpj = input('\nDigite o CNPJ (sem pontuação): ')
    if cnpj == 'q':
        print("\n" + ('=' * 10) + ' Consulta encerrada! ' + ('=' * 11))
        break
    if len(cnpj) != 14 or not cnpj.isdigit():
        print("CNPJ inexistente!")
        continue

    lista1_cnpj = multiplica_1(cnpj)
    lista2_cnpj = multiplica_2(cnpj)

    d1, d2 = obter_digitos(lista1_cnpj, lista2_cnpj)

    verificar_cnpj(d1, d2)
