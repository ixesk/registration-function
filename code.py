

def cadastro():
    """
    Esta função recebe os dados do usuário em forma de cadastro e o retorna.
    Os dados podem ser salvoss em um conjunto.
    :return: Retorna os dados do usuário.
    """
    message_list = ['Para que o cadastro seja feito sem erros, siga a seguinte ordem:',
                    'Nome -> Sobrenome -> Idade -> Cidade',
                    'Para pular para a proxima etapa, pressione ENTER depois de preencher os parâmetros.',
                    '-----------------------------------------']

    for index in message_list:
        print(index)

    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    idade = input('Idade: ')
    cidade = input('Cidade: ')

    receive = {'Nome': nome, 'Sobrenome': sobrenome, 'Idade': idade, 'Cidade': cidade}

    print('-----------------------------------------')
    for chave, valor in receive.items():
        print(f'{chave}: {valor}')
    print('-----------------------------------------')

    quest = input('Confirmar informações? (Sim/Não): ')

    if quest == 'Sim':
        print('-----------------------------------------')
        print('Cadastro realizado com sucesso.')

    if quest == 'Não':
        print('-----------------------------------------')
        print('Por favor, insira seus dados novamente.')
        print('-----------------------------------------')
        cadastro()


cadastro()
