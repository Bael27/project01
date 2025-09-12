#lista de nomes e cpfs.
names = []

#Variavel que faz os ids começarem a ser colocados no index 1 da lista.
identifier = 1

class List():

    def __init__(self):

        pass

    def add(self, name):
        
        #Adiciona um usuário criado e validado pelo register.
        names.insert(identifier, name)

        #Proporciona o id o usuário, que é usado nas pesquisas.
        n = len(names)
        print(f"Usuario criado com sucesso! Seu id é: {n}")

    def search(self, item):

        #verifica se o id que o usuário pesquisou existe ou se está escrito corretamente, se sim, ele mostra as informações do usuário correspondente.
        try:
            item = int(item)

            #Verifica se o id requisitado é 0, se for, devolve um erro.
            if item == 0:
                return 3

            #Verifica se o id existe e retorna.
            if item > len(names):
                return  1
            
            #Verifica se o id fornecido é um inteiro e retorna.
            if isinstance(item, int):
                return 2
        
        #Verifica que há um erro de digitação no id e retorna.
        except:
                return 3

#Aumenta o valor da variavel para que o próximo usuario criado seja posto no próximo inex da lista.
identifier += 1