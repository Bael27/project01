from packages import register
from packages import search

tam = 30

opcoes = {
    "1": "Criar conta",
    "2": "Detalhes da conta",
    "0": "sair",
}

while True:
    print(f"+{'-' * tam}+")
    print(f"|{'MENU':^{tam}}|")
    print(f"+{'-' * tam}+")
    for k, v in opcoes.items():
        print(f"|{f' {k} - {v}' :{tam}}|")
    print(f"+{'-' * tam}+")

    op = input()

    if op not in opcoes:
        print("Opção inválida")
        continue

    if op == "0":
        break

    if op == "1":
            reg = register.Register()
            reg.reg()

    if op == "2":
            i = input("Qual o seu ID? ")
            proc = search.Search()
            proc.proc(i)