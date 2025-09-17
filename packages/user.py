from packages import lista
from packages.vef_mixin import ValidatorMixin

class User(ValidatorMixin):

    def __init__(self, nome, cpf):
        self.cpf = cpf
        self.nome = nome

    #Método para a criação de um usuário.
    def creation(self):
        
        #Utilização da verficação de nome do ValidatorMixin.
        vef_nome = ValidatorMixin.val_name(self.nome)
        
        #Verificação dos casos de rotorno da verificação do nome.
        match vef_nome:
            case 1:
                return print("\nPor favor, digite seu primeiro e último nome (Ex: João Monasterio).")
            case 2:
                return print("\nPor favor, Digite somente seu primeiro e ultimo nome (Ex: João Monasterio).")

        #Utilização da verificação de cpf do ValidatorMixin.
        vef_cpf = ValidatorMixin.val_cpf(self.cpf)

        #Verificação de casos do retorno da verificação do cpf.
        match vef_cpf:

            #Caso em que está tudo validado.
            case 1:

                #Junta as informações de nome e cpf de um usuário em uma mesma variavel.
                nome_cpf ="\nNome: " + self.nome.title() + "\nCPF: " + self.cpf

                #Leva o nome e cpf de um usuário para adiciona-lo à lista.
                ad = lista.List()
                ad.add(nome_cpf)
            
            #Casos de erro.
            case 2:
                return print("\nCPF inválido!")
            
            case 3:
                return print("\nCPF inválido! Siga este exemplo quando digitar seu CPF: '000.000.000-00'.")
            
            case 4:
                return print("\nEste CPF ja está cadastrado e não pode ser usado novamente.") 
