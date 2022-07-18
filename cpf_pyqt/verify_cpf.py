import re


def verify_cpf(cpf):
    """Verifica se o CPF inserido é válido"""
    cpf = str(cpf)

    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return 'INVÁLIDO'

    list1_cpf = [int(cpf[d]) * i for d, i in enumerate(range(10, 1, -1))]
    list2_cpf = [int(cpf[d]) * i for d, i in enumerate(range(11, 2, -1))]
    list2_cpf.append(int(cpf[9]) * 2)

    d1 = 11 - ((sum(list1_cpf)) % 11)
    d2 = 11 - ((sum(list2_cpf)) % 11)

    if d1 > 9:
        d1 = 0
    if d2 > 9:
        d2 = 0

    cpf_validator = cpf[:9] + str(d1) + str(d2)

    sequence = cpf_validator == str(cpf_validator[0]) * len(cpf)

    if cpf == cpf_validator and not sequence:
        return 'VÁLIDO'
    else:
        return 'INVÁLIDO'
