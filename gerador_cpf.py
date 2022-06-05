from random import randint


print(('='*10) + ' GERADOR DE CPF ' + ('='*10) + "\n")
while True:
    usuario = input("Gerar CPF? [s]im / [n]ao: ")
    if usuario not in 'NnSs':
        print("Resposta inválida!\n")
        continue
    if usuario in 'Nn':
        print("\n" + ('=' * 8) + ' Gerador encerrado! ' + ('=' * 8))
        break
    else:
        cpf = randint(100000000, 999999999)
        cpf = str(cpf)

        lista1_cpf = [int(cpf[d]) * i for d, i in enumerate(range(10, 1, -1))]
        lista2_cpf = []

        d1 = 11 - ((sum(lista1_cpf)) % 11)
        if d1 > 9:
            d1 = 0
        cpf = str(cpf) + str(d1)

        lista2_cpf = [int(cpf[d]) * i for d, i in enumerate(range(11, 2, -1))]
        lista2_cpf.append(int(cpf[9]) * 2)

        d2 = 11 - ((sum(lista2_cpf)) % 11)
        if d2 > 9:
            d2 = 0
        cpf = str(cpf) + str(d2)
        cpf = int(cpf)

        print(f'CPF: {cpf}\n')
