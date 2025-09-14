from packages import user
from packages import search


opcoes = {
    "1": "Criar conta",
    "2": "Detalhes da conta",
    "0": "sair",
}

while True:

    tam = 30
    #cria o menu no terminal.
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

        #Criação do menu de registro.
        tam = 100
        print(f"+{'-' * tam}+")
        print(f"|{'REGISTRAR':^{tam}}|")
        print(f"+{'-' * tam}+")

        nome = input("Digite seu primeiro e último nome: ")
        cpf = input("digite seu cpf (siga este exemplo 000.000.000-00): ")
        reg = user.User(nome, cpf)
        reg.creation()

    #Começa a procura por um usuário existente.
    if op == "2":

        #Criação do menu de pesquisa.
        tam = 100
        print(f"+{'-' * tam}+")
        print(f"|{'PESQUISAR':^{tam}}|")
        print(f"+{'-' * tam}+")

        #Recebe a informação do id desejado para pesquisa e envia para o responsável por procurar esse id.
        item = input("Qual o seu ID? ")
        proc = search.Search(item)
        proc.proc()