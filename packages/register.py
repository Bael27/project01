from packages import verify_cpf
import re

cpfs = []
class Register():

    def __init__(self, cpf, nome):
        
        self.cpf = cpf
        self.nome = nome

    def reg(self):
        
        #Verifica se um nome escrito por um usuário está vazio.
        if not self.nome.strip():
            return 1
        
        #Verifica o tamanho do nome do usuário.
        if len(self.nome) > 25:
            return 1
        
        if re.fullmatch(r"^[a-zA-ZÀ-ÖØ-öø-ÿ\s]*$", self.nome):
            pass
        else:
            return 1

        #Chama o verificador de CPF, para verificar se o CPF digitado pelo usuário é valido, se ja foi usado e se está escrito corretamente.
        verify = verify_cpf.valid(self.cpf)
        vef = verify.validator()

        #Retorno com o cpf válido.
        if vef == 1:
            return 2

        #Retorno com o cpf inválido.
        elif vef == 2:
            return 3
        
            #Retorno com o cpf escrito de uma forma errada.
        elif vef == 3:
            return 4
        
        elif vef == 4:
            return 5
