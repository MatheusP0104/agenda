from classe_agenda import *

class Menu:
    def __init__(self):
        agenda = Agenda()

        #  Iniciar Menu
        while True:
            entrada = input('Informe a opção desejada\n1 - Novo Contato\n2 - Listar Contatos\n3 - Alterar Telefone\n4 - Sair\nR:')
            if entrada == '1':
                agenda.salvar_contatos()
            elif entrada == '2':
                agenda.listar_todos_contatos()
            elif entrada == '3':
                agenda.alterar_telefone()
            elif entrada == '4': 
                print('Saindo...')
                break
            else:
                print('Opção não existente')

