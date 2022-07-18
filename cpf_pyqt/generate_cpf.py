from random import randint


def generate_cpf():
    """Gera um CPF aleatório válido"""
    cpf = randint(100000000, 999999999)
    cpf = str(cpf)

    list1_cpf = [int(cpf[d]) * i for d, i in enumerate(range(10, 1, -1))]

    d1 = 11 - ((sum(list1_cpf)) % 11)
    if d1 > 9:
        d1 = 0
    cpf = str(cpf) + str(d1)

    list2_cpf = [int(cpf[d]) * i for d, i in enumerate(range(11, 2, -1))]
    list2_cpf.append(int(cpf[9]) * 2)

    d2 = 11 - ((sum(list2_cpf)) % 11)
    if d2 > 9:
        d2 = 0
    cpf = str(cpf) + str(d2)

    return cpf
