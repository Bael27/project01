import re

cpfs = []

class valid():

    def __init__(self, cpf):

        self.cpf = cpf

    def validator(self):

        #Verifica se o cpf ja foi cadastrado anteriormente.
        if self.cpf not in cpfs:

            #Retira apenas os dígitos do CPF, ignorando os caracteres especiais.
            numeros = [int(digito) for digito in self.cpf if digito.isdigit()]

            formatacao = False
            quant_digitos = False
            validacao1 = False
            validacao2 = False

            #Verifica a estrutura do CPF (000.000.000-00).
            if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', self.cpf):
                formatacao = True

                #Verifica se a quantidade de numeros do cpf fornecido esta correta e retorna se houver erro.
                if len(numeros) == 11:
                    quant_digitos = True
                else:
                    return 3

                #Faz as contas e confirma se o numero obtido bate com o do primeiro digito verificador.
                soma_produtos = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
                digito_esperado = (soma_produtos * 10 % 11) % 10
                if numeros[9] == digito_esperado:
                    validacao1 = True

                #Faz as contas e verifica se o numero obtido bate com o segundo numero verificador.
                soma_produtos1 = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
                digito_esperado1 = (soma_produtos1 *10 % 11) % 10
                if numeros[10] == digito_esperado1:
                    validacao2 = True

                #Verifica se o cpf fornecido possui todas as condições para ser válidado, o adiciona a lista de cpf's e retorna.
                if quant_digitos == True and formatacao == True and validacao1 == True and validacao2 == True:
                    cpfs.append(self.cpf)
                    return 1
            
                #Verifica se o cpf não possui uma ou mais das conições para ser válidado e retorna.
                else:
                    return 2

            #Verifica que o cpf não está escrito no modelo correto e retorna.
            else:
                return 3
            
        else:
            return 4