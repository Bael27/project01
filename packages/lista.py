names = []

class List():

    def __init__(self):

        pass

    def add(self, name):
        names.append(name)
        n = len(names)
        print(f"Usuario criado com sucesso! Seu id é: {n - 1}")

    def search(name):
        if name in names:
            print(f"Estes são seus dados: {name}.")
        else:
            print(f"O usuário {name}, não existe.")