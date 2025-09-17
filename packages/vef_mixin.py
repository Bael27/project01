import re

#Lista que guarda os CPF'S já utilizados.
cpfs = []

#Classe Mixin de verificação.
class ValidatorMixin:

    #Método de verificação de nome.
    def val_name(nome):

        #Verifica se um nome escrito por um usuário está vazio.
        if not nome.strip():
            return 1
        
        #Verifica o tamanho do nome do usuário.
        if len(nome) > 25:
            return 2
        
        #Verifica se o nome está escrito corretamente.
        if re.fullmatch(r"^[a-zA-ZÀ-ÖØ-öø-ÿ\s]*$", nome):
            pass

        #Verifica que o nome recebido não passou nas verificações de validação e retorna um erro.
        else:
            return 2
    
    #Método de verificação de CPF.
    def val_cpf(cpf):

        #Verifica se o CPF já não foi utilizado anteriormente por outro usuário.
        if cpf not in cpfs:

            #Retira apenas os dígitos do CPF, ignorando os caracteres especiais.
            numeros = [int(digito) for digito in cpf if digito.isdigit()]

            #Define as verificações necessárias para validação como falsas para começar.
            formatting = False
            amount_digits = False
            validation1 = False
            validation2 = False

            #Verifica a estrutura do CPF (000.000.000-00).
            if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
                formatting = True

                #Verifica se a quantidade de numeros do cpf fornecido esta correta e retorna se houver erro.
                if len(numeros) == 11:
                    amount_digits = True
                else:
                    return 3

                #Faz as contas e confirma se o numero obtido bate com o do primeiro digito verificador.
                soma_produtos = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
                digito_esperado = (soma_produtos * 10 % 11) % 10
                if numeros[9] == digito_esperado:
                    validation1 = True

                #Faz as contas e verifica se o numero obtido bate com o segundo numero verificador.
                soma_produtos1 = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
                digito_esperado1 = (soma_produtos1 *10 % 11) % 10
                if numeros[10] == digito_esperado1:
                    validation2 = True

                #Verifica se o cpf fornecido possui todas as condições para ser válidado, o adiciona a lista de cpf's e retorna.
                if amount_digits == True and formatting == True and validation1 == True and validation2 == True:
                    cpfs.append(cpf)
                    return 1
            
                #Verifica se o cpf não possui uma ou mais das conições para ser válidado e retorna.
                else:
                    return 2

            #Verifica que o cpf não está escrito no modelo correto e retorna.
            else:
                return 3
            
        else:
            return 4