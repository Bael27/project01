from packages import register
from packages import search

tam = 30

opcoes = {
    "1": "Criar conta",
    "2": "Detalhes da conta",
    "0": "sair",
}

while True:

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
        reg = register.Register()
        reg.reg()

    #Começa a procura por um usuário existente.
    if op == "2":
        proc = search.Search()
        proc.proc()