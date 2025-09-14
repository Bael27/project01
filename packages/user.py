from packages import lista
from packages import register

class User():

    def __init__(self, nome, cpf):
        self.cpf = cpf
        self.nome = nome

    def creation(self):
        
        vef = register.Register(self.cpf, self.nome)
        vef = vef.reg()
        
        if vef == 1:
            return print("\nDigite somente seu primeiro e último nome(Ex: João Monasterio).")

        elif vef == 2:
            #Junta as informações de nome e cpf de um usuário em uma mesma variavel.
            nome_cpf ="\nNome: " + self.nome.title() + "\nCPF: " + self.cpf

            #Leva o nome e cpf de um usuário para adiciona-lo à lista.
            ad = lista.List()
            ad.add(nome_cpf)

        elif vef == 3:
            return print("\nCPF inválido!")
        
        elif vef == 4:
            return print("\nCPF inválido! Siga este exemplo quando digitar seu CPF: '000.000.000-00'.")
        
        elif vef == 5:
            return print("\nEste CPF ja está cadastrado e não pode ser usado novamente.") 