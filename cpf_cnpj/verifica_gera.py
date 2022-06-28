import funcoes


print(('='*12) + " DOCUMENTOS " + ('='*12))

while True:
    funcoes.menu()

    usuario = input("Opção: ")

    try:
        usuario = int(usuario)
    except Exception:
        print("Opção inválida!")
    else:
        if usuario == 1:
            active = True
            while active:
                cpf = funcoes.inserir_documento('cpf')
                if len(cpf) != 11:
                    print("CPF inexistente!")
                    continue
                else:
                    active = False

            funcoes.verificar_cpf(cpf)
            print("=" * 36)

        if usuario == 2:
            active = True
            while active:
                cnpj = funcoes.inserir_documento('cnpj')
                if len(cnpj) != 14:
                    print("CNPJ inexistente!")
                    continue
                else:
                    active = False

            funcoes.verificar_cnpj(cnpj)
            print("=" * 36)

        if usuario == 3:
            funcoes.gerar_cpf()
            print("=" * 36)

        if usuario == 4:
            funcoes.gerar_cnpj()
            print("=" * 36)

        if usuario == 5:
            print("\n" + ('=' * 7) + ' PROGRAMA ENCERRADO! ' + ('=' * 8))
            break
