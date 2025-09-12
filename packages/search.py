from packages import lista
from operator import neg

class Search():

    def __init__(self):
    
        pass

    def proc(self):

        #Criação do menu de pesquisa.
        tam = 100
        print(f"+{'-' * tam}+")
        print(f"|{'PESQUISAR':^{tam}}|")
        print(f"+{'-' * tam}+")

        #Recebe a informação do id desejado para pesquisa e envia para o responsável por procurar esse id.
        item = input("Qual o seu ID? ")
        pro = lista.List()
        pr = pro.search(item)

        #Mostra que a verificação resultou em falha por não existência do id procurado.
        if pr == 1:
            print("Este ID de usuário não existe.")

        #Mostra as informações do usuário procurado após a verificação.
        elif pr == 2:
            item = int(item)
            item -= 1
            print(f"Estes são seus dados: {lista.names[item]}.")

        #Mostra que houve um erro de digitação do id.
        elif pr == 3:
            print("Digite um valor de ID válido. (Ex: 1, 2, 3...)")