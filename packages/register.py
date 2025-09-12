from packages import lista
from packages import verify_cpf

cpfs = []
class Register():

    def __init__(self):
        
        pass

    def reg(self):
        
        #Criação do menu de registro.
        tam = 100
        print(f"+{'-' * tam}+")
        print(f"|{'REGISTRAR':^{tam}}|")
        print(f"+{'-' * tam}+")

        #Coleta de dados do usuário.
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF (Siga este exemplo: '000.000.000-00'): ")

        #Chama o verificador de CPF, para verificar se o CPF digitado pelo usuário é valido, se ja foi usado e se está escrito corretamente.
        verify = verify_cpf.valid(cpf)
        vef = verify.validator()

        #Retorno com o cpf válido.
        if vef == 1:
            print("CPF válido!")
            cpfs.append(cpf)

        #Retorno com o cpf inválido.
        elif vef == 2:
            return print("CPF inválido!")
        
        #Retorno com o cpf escrito de uma forma errada.
        elif vef == 3:
            return print("CPF inválido! Siga este exemplo quando digitar seu CPF: '000.000.000-00'.")
        
        #Retorno com um cpf que já havia sido adicionado
        elif vef == 4:
            return print("Este CPF ja está cadastrado e não pode ser usado novamente.")
        
        #Junta as informações de nome e cpf de um usuário em uma mesma variavel.
        nome_cpf ="\nNome: " + nome + "\nCPF: " + cpf

        #Leva o nome e cpf de um usuário para adiciona-lo à lista.
        ad = lista.List()
        ad.add(nome_cpf) 
    
