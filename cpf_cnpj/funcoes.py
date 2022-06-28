from random import randint
import re


def menu():
    """Imprime na tela o menu de opções do usuário"""

    print("""\n1- Verificar CPF
2- Verificar CNPJ
3- Gerar CPF
4- Gerar CNPJ
5- Encerrar\n""")


def inserir_documento(nome_documento):
    """Retorna o documento solicitado ao usuário"""

    documento = input(f"\nDigite o {nome_documento.upper()}: ")
    documento = re.sub(r'\D', '', documento)  # re.sub(r'[^0-9]', ...)
    return documento


def gerar_lista(documento, n1, n2):
    """Gera uma lista resultante da multiplicação entre outras duas"""

    return [int(documento[d]) * i for d, i in enumerate(range(n1, n2, -1))]


def gerar_lista_especial(documento, s, n1, n2):
    """Gera uma lista diferente da comum resultante da multiplicação entre outras duas"""

    return [int(documento[d + s]) * i for d, i in enumerate(range(n1, n2, -1))]


def gerar_digito(lista):
    """Retorna um dígito que pertence ao final do documento"""

    d = 11 - ((sum(lista)) % 11)
    if d > 9:
        d = 0

    return d


def verificar_documento(documento, d1, d2, digitos, nome_documento):
    """Verifica se um documento é ou não válido"""

    if d1 == int(documento[digitos-2]) and d2 == int(documento[digitos-1]):
        print(f"\n{nome_documento.upper()} VÁLIDO!\n")
    else:
        print(f"\n{nome_documento.upper()} INVÁLIDO!\n")


def verificar_cpf(cpf):
    """Verifica se um CPF é válido"""

    lista1_cpf = gerar_lista(cpf, 10, 1)
    lista2_cpf = gerar_lista(cpf, 11, 2)
    lista2_cpf.append(int(cpf[9]) * 2)

    d1 = gerar_digito(lista1_cpf)
    d2 = gerar_digito(lista2_cpf)

    verificar_documento(cpf, d1, d2, 11, 'cpf')


def verificar_cnpj(cnpj):
    """Verifica se um CNPJ é válido"""

    lista1_cnpj = gerar_lista(cnpj, 5, 1)
    lista_1b = gerar_lista_especial(cnpj, 4, 9, 1)
    lista1_cnpj.extend(lista_1b)

    lista2_cnpj = gerar_lista(cnpj, 6, 1)
    lista_2b = gerar_lista_especial(cnpj, 5, 9, 1)
    lista2_cnpj.extend(lista_2b)

    d1 = gerar_digito(lista1_cnpj)
    d2 = gerar_digito(lista2_cnpj)

    verificar_documento(cnpj, d1, d2, 14, 'cnpj')


def gerar_cpf():
    """Gera um CPF válido"""

    cpf = str(randint(100000000, 999999999))

    lista1_cpf = gerar_lista(cpf, 10, 1)
    d1 = gerar_digito(lista1_cpf)
    cpf += str(d1)

    lista2_cpf = gerar_lista(cpf, 11, 2)
    lista2_cpf.append(int(cpf[9]) * 2)
    d2 = gerar_digito(lista2_cpf)
    cpf += str(d2)

    print(f"\nCPF: {cpf}")
    print(f"Formatado: {formatar_cpf(cpf)}\n")


def gerar_cnpj():
    """Gera um CNPJ válido"""

    cnpj = str(randint(100000000000, 999999999999))

    lista1_cnpj = gerar_lista(cnpj, 5, 1)
    lista_1b = gerar_lista_especial(cnpj, 4, 9, 1)
    lista1_cnpj.extend(lista_1b)
    d1 = gerar_digito(lista1_cnpj)
    cnpj += str(d1)

    lista2_cnpj = gerar_lista(cnpj, 6, 1)
    lista_2b = gerar_lista_especial(cnpj, 5, 9, 1)
    lista2_cnpj.extend(lista_2b)
    d2 = gerar_digito(lista2_cnpj)
    cnpj += str(d2)

    print(f"\nCNPJ: {cnpj}")
    print(f"Formatado: {formatar_cnpj(cnpj)}\n")


def formatar_cnpj(cnpj):
    """Retorna o CNPJ formatado com pontuação"""

    cnpj_formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return cnpj_formatado


def formatar_cpf(cpf):
    """Retorna o CPF formatado com pontuação"""

    cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
    return cpf_formatado
