from packages.user import User
from packages.search import Search

class Menus:

    def menu_register():

        #Criação do menu de registro.
        tam = 100
        print(f"+{'-' * tam}+")
        print(f"|{'REGISTRAR':^{tam}}|")
        print(f"+{'-' * tam}+")

        #Recebe as informações para a criação de um usuário.
        nome = input("Digite seu primeiro e último nome: ")
        cpf = input("digite seu cpf (siga este exemplo 000.000.000-00): ")
        reg = User(nome, cpf)
        reg.creation()

    def menu_search():
    
        #Criação do menu de pesquisa.
        tam = 100
        print(f"+{'-' * tam}+")
        print(f"|{'PESQUISAR':^{tam}}|")
        print(f"+{'-' * tam}+")

        #Recebe a informação do id desejado para pesquisa e envia para o responsável por procurar esse id.
        item = input("Qual o seu ID? ")
        sh = Search(item)
        sh.show()

opcoes = {
    "1": "Criar conta",
    "2": "Detalhes da conta",
    "0": "sair",
}

while True:

    tam = 30
    #Cria o menu no terminal.
    print(f"+{'-' * tam}+")
    print(f"|{'MENU':^{tam}}|")
    print(f"+{'-' * tam}+")
    for k, v in opcoes.items():
        print(f"|{f' {k} - {v}' :{tam}}|")
    print(f"+{'-' * tam}+")

    #Recebe a opção escolhida pelo usuário.
    op = input()

    #Verifica se a opção escolhia realmente é uma opção.
    if op not in opcoes:
        print("Opção inválida")
        continue

    #Finaliza o programa.
    if op == "0":
        print("Programa finalizado!")
        break

    #Começa o registro de um novo usuário na lista.
    if op == "1":
        Menus.menu_register()
            
    #Começa a procura por um usuário existente.
    if op == "2":
        Menus.menu_search()