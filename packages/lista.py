names = []

class List():

    def __init__(self):

        pass

    def add(self, name):
        names.append(name)
        n = len(names)
        print(f"Usuario criado com sucesso! Seu id é: {n - 1}")

    def search(self, item):
        try:
            item = int(item)
            if item > len(names):
                return  print("Este ID de usuário não existe")
            if isinstance(item, int):
                print(f"Estes são seus dados: {names[item]}")
        except:
                print("Digite um valor de ID válido. (Ex: 0, 1, 2...)")