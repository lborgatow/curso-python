"""
CPF (exemplo) = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 (9º dígito) *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""


print(('='*12) + " CONSULTA DE CPF " + ('='*12))
print(('='*8) + " (digite 'q' para parar) " + ('='*8))
while True:
    cpf = input("\nDigite o CPF (sem pontuação): ")
    if cpf == 'q':
        print("\n" + ('=' * 10) + ' Consulta encerrada! ' + ('=' * 10))
        break
    if not cpf.isdigit():
        print("CPF inexistente!")
        continue

    lista1_cpf = [int(cpf[d]) * i for d, i in enumerate(range(10, 1, -1))]
    lista2_cpf = [int(cpf[d]) * i for d, i in enumerate(range(11, 2, -1))]
    lista2_cpf.append(int(cpf[9]) * 2)

    d1 = 11 - ((sum(lista1_cpf)) % 11)
    d2 = 11 - ((sum(lista2_cpf)) % 11)

    if d1 > 9:
        d1 = 0
    if d2 > 9:
        d2 = 0

    if d1 == int(cpf[9]) and d2 == int(cpf[10]):
        print("CPF VÁLIDO!")
    else:
        print("CPF INVÁLIDO!")
