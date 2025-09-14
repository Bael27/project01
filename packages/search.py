from packages import lista

class Search():

    def __init__(self, id):
    
        self.id = id

    def proc(self):

        pr = lista.List()
        pr = pr.search(self.id)

        #Mostra que a verificação resultou em falha por não existência do id procurado.
        if pr == 1:
            print("\nEste ID de usuário não existe.")

        #Mostra as informações do usuário procurado após a verificação.
        elif pr == 2:
            item = int(self.id)
            item -= 1
            print(f"\nEstes são seus dados:\n {lista.names[item]}.")

        #Mostra que houve um erro de digitação do id.
        elif pr == 3:
            print("\nDigite um valor de ID válido. (Ex: 1, 2, 3...)")