from packages import lista

class Register():

    def __init__(self):
        
        self.n = 0

    def reg(self):
        
        tam = 100
        print(f"+{'-' * tam}+")
        print(f"|{'REGISTRAR':^{tam}}|")
        print(f"+{'-' * tam}+")
        nome_cpf = input("Nome e CPF (siga este exemplo: João Ismael, 000-000-000.00): ")

        ad = lista.List()
        ad.add(nome_cpf) 
    
