from operator import le
from classe_contato import *

class Agenda:
    def __init__(self):
        self.listaContato = []

    def salvar_contatos(self):
        entrada_cod = input('Informe o código: ')
        entrada_nome = input('Informe o nome: ')
        entrada_telefone = input('Informe o telefone: ')
        self.listaContato.append(Contato(entrada_cod, entrada_nome, entrada_telefone))
        print('Contato salvo com sucesso!')
        print('===================================')

    def listar_todos_contatos(self):
        for i in range(len(self.listaContato)):
            print('Cod:',self.listaContato[i].cod,'nome:',self.listaContato[i].nome, 'telefone:',self.listaContato[i].telefone)
            print('===================================')

    def alterar_telefone(self):
        entrada = input('Digite o código do contato: ')
        for i in range(len(self.listaContato)):
            if entrada == self.listaContato[i].cod:
                self.listaContato[i].telefone = input('Digite o novo telefone: ')
                print('Telefone alterado com sucesso!')
                print('===================================')



