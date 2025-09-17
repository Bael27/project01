from packages import lista

class Search():

    def __init__(self, id):
    
        self.id = id

    def show(self):

        #Começa a verificação do id desejado.
        sh = lista.List()
        sh = sh.search(self.id)

        #Verificação dos casos de retorno da lista.
        match sh:

            #Mostra que a verificação resultou em falha por não existência do id procurado.
            case 1:
                print("\nEste ID de usuário não existe.")

            #Mostra as informações do usuário procurado após a verificação.
            case 2:
                item = int(self.id)
                item -= 1
                print(f"\nEstes são seus dados:\n {lista.names[item]}.")

            #Mostra que houve um erro de digitação do id.
            case 3:
                print("\nDigite um valor de ID válido. (Ex: 1, 2, 3...)")