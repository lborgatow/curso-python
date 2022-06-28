"""
Faça uma lista de 'tarefas' com as seguintes opções:
    # adicionar tarefa
    # listar tarefas
    # opção de desfazer tarefa (a cada vez que chamarmos, desfaz a última ação) - undo
    # opção de refazer tarefa (a cada vez que chamarmos, refaz a útima ação) - redo
"""


def menu():
    """Exibe o menu de opções"""

    print("""1 - Adicionar tarefa
2 - Listar tarefas
3 - Desfazer última ação
4 - Refazer última ação\n""")


def adicionar(tarefa, tarefas):
    """Adiciona uma tarefa na lista de tarefas"""

    tarefas.append(tarefa)


def listar(tarefas):
    """Lista todas as tarefas da lista de tarefas"""

    if not tarefas:
        print()
        print('Lista vazia')
        return

    for indice, tarefa in enumerate(tarefas):
        print(f'Tarefa {indice+1} --> {tarefa}')


def desfazer(tarefas, lista_desfazer):
    """Remove a última tarefa na lista de tarefas"""

    if not tarefas:
        print()
        print('Nada a desfazer')
        return

    lista_desfazer.append(tarefas.pop())


def refazer(tarefas, lista_desfazer):
    """Adiciona novamente a última tarefa removida na lista de tarefas"""

    if not lista_desfazer:
        print()
        print('Nada a refazer')
        return

    tarefas.append(lista_desfazer.pop())


print('Digite 0 para encerrar o programa\n\n')

tarefas, lista_desfazer = [], []
while True:
    menu()

    opcao = input('Opção: ')

    try:
        opcao = int(opcao)
    except Exception:
        print('\nOpção inválida!\n')
        continue
    else:
        if opcao == 0:
            print('\n\nPrograma encerrado!')
            break

        if opcao == 1:
            print()
            tarefa = input()
            adicionar(tarefa, tarefas)
            print(f'\n{"="*25}\n')
            continue

        if opcao == 2:
            listar(tarefas)
            print(f'\n{"="*25}\n')
            continue

        if opcao == 3:
            desfazer(tarefas, lista_desfazer)
            print(f'\n{"="*25}\n')
            continue

        if opcao == 4:
            refazer(tarefas, lista_desfazer)
            print(f'\n{"="*25}\n')
            continue
