from random import randint


def multiplica_1(cnpj):
    lista1_cnpj = [int(cnpj[d]) * i for d, i in enumerate(range(5, 1, -1))]
    lista_1b = [int(cnpj[d+4]) * i for d, i in enumerate(range(9, 1, -1))]
    lista1_cnpj.extend(lista_1b)
    return lista1_cnpj


def multiplica_2(cnpj):
    lista2_cnpj = [int(cnpj[d]) * i for d, i in enumerate(range(6, 1, -1))]
    lista_2b = [int(cnpj[d+5]) * i for d, i in enumerate(range(9, 1, -1))]
    lista2_cnpj.extend(lista_2b)
    return lista2_cnpj


def obter_digito_1(lista1_cnpj):
    d1 = 11 - ((sum(lista1_cnpj)) % 11)
    if d1 > 9:
        d1 = 0
    return d1


def obter_digito_2(lista2_cnpj):
    d2 = 11 - ((sum(lista2_cnpj)) % 11)
    if d2 > 9:
        d2 = 0
    return d2


def gerar_cnpj(cnpj):
    print(f'CNPJ: {cnpj}')


def formatar_cnpj(cnpj):
    cnpj_formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return cnpj_formatado


print(('='*10) + ' GERADOR DE CNPJ ' + ('='*10) + "\n")
while True:
    usuario = input("Gerar CNPJ? [s]im / [n]ao: ")
    if usuario not in 'NnSs':
        print("Resposta inválida!\n")
        continue
    if usuario in 'Nn':
        print("\n" + ('=' * 8) + ' Gerador encerrado! ' + ('=' * 9))
        break
    else:
        cnpj = randint(100000000000, 999999999999)
        cnpj = str(cnpj)

    lista1_cnpj = multiplica_1(cnpj)
    d1 = obter_digito_1(lista1_cnpj)
    cnpj += str(d1)

    lista2_cnpj = multiplica_2(cnpj)
    d2 = obter_digito_2(lista2_cnpj)
    cnpj += str(d2)

    gerar_cnpj(cnpj)
    print(f'Formatado: {formatar_cnpj(cnpj)}\n')
