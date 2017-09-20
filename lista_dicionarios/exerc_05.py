contatos = {}
i=0
sair=0

while i<=100:
    resposta = int(input("1 - Inserir\n2 - Remover\n3 - Pesquisar\n4 - Sair\nO que deseja fazer?\n"))
    if resposta == 1:
        nome = input('Nome: ')
        email = input('Email: ')
        tel = input('Telefone: ')
        end = input('Endereço: ')
        contatos[nome] = [email, tel, end]
        if nome in contatos[nome]:
            email =input('Atualize o email: ')
            tel = input('Atualize seu contato: ')
            end = input('Atualize seu endereço: ')
    elif resposta == 2:
        nome=input('Informe o nome que deseja apagar: ')
        del contatos[nome]
    elif resposta == 3:
        nome=input('Informe o nome que deseja pesquisar:')
        if nome in contatos:
            print('Email: ',email)
            print('Telefone: ',tel)
            print('Endereço: ',end)
        else:
            print('Não foi encontrado nenhum contato com o nome digitado.')

    elif resposta == 4:
        sair=0
    else:
        print("Opcao invalida.")

i += 1
