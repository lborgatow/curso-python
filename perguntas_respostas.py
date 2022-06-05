print(('='*10) + " QUIZ - HISTÓRIA DA LINGUAGEM PYTHON! " + ('='*10) + '\n')

perguntas = {
    "Pergunta 1":
        {
            "pergunta": 'Quem criou a linguagem Python?',
            "alternativas":
                {
                    "a": 'Brendan Eich',
                    "b": 'Bjarne Stroustrup',
                    "c": 'Guido van Rossum',
                    "d": 'Anders Hejlsberg'
                },
            "resposta_certa": 'Cc'
        },

        "Pergunta 2":
        {
            "pergunta": 'Em que ano Python foi criada?',
            "alternativas":
                {
                    "a": '1978',
                    "b": '1989',
                    "c": '1998',
                    "d": '2002'
                },
            "resposta_certa": 'Bb'
        },

        "Pergunta 3":
        {
            "pergunta": 'Em qual país Python foi criada?',
            "alternativas":
                {
                    "a": 'Estados Unidos',
                    "b": 'Países Baixos',
                    "c": 'Inglaterra',
                    "d": 'Noruega'
                },
            "resposta_certa": 'Bb'
        },

        "Pergunta 4":
        {
            "pergunta": 'Em que ano Python foi lançada?',
            "alternativas":
                {
                    "a": '1991',
                    "b": '1987',
                    "c": '2004',
                    "d": '1982'
                },
            "resposta_certa": 'Aa'
        },

        "Pergunta 5":
        {
            "pergunta": 'Qual a versão mais atual de Python?',
            "alternativas":
                {
                    "a": '2.7',
                    "b": '3.9.8',
                    "c": '3.10.1',
                    "d": '3.10.4'
                },
            "resposta_certa": 'Dd'
        },
}

quantidade_acertos = 0
for pergunta, dados_pergunta in perguntas.items():
    print(f"{pergunta}: {dados_pergunta['pergunta']}\n")

    for alternativa, dados_alternativa in dados_pergunta['alternativas'].items():
        print(f"[{alternativa}] {dados_alternativa}")

    resposta_usuario = input("\nSua resposta: ")

    if resposta_usuario in dados_pergunta['resposta_certa']:
        print("\nRESPOSTA CORRETA!!!\n")
        quantidade_acertos += 1
    else:
        print("\nRESPOSTA INCORRETA!!!\n")

quantidade_perguntas = len(perguntas)
porcentagem_acertos = (quantidade_acertos / quantidade_perguntas) * 100

print(f"\nVocê acertou {quantidade_acertos} de {quantidade_perguntas} perguntas!")
print(f"Porcentagem de acertos: {porcentagem_acertos}%")
