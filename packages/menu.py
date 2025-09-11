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
        try:
            i = int(input("Qual o seu ID? "))
            if isinstance(i, int):
                proc = search.Search(i)
                proc.proc()
        except:
            print("Digite um valor de ID válido. (Ex: 0, 1, 2...)")    