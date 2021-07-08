def opcoes():
    print('\nDigite 1 para LISTAR AGENDAMENTO.\nDigite 2 para AGENDAR.')
    print('Digite 3 para EXCLUIR AGENDAMENTO.\nDigite 4 para EDITAR AGENDAMENTO.')
    print('Digite 0 para SAIR.')
    n = int(input())
    return n

print('{:=^50}'.format('Locação de espaço de eventos'))
print('Digite 1 para LISTAR AGENDAMENTO.\nDigite 2 para AGENDAR.')
print('Digite 3 para EXCLUIR AGENDAMENTO.\nDigite 4 para EDITAR AGENDAMENTO.')
print('Digite 0 para SAIR.')
n = int(input())
agendamento ='1 - Domingo: Livre\n2 - Segunda: Livre\n3 - Terça: Livre\n4 - Quarta: Livre\n5 - Quinta: Livre\n6 - Sexta: Livre\n7 - Sábado: Livre'

while n > 0 and n <=4:
        if n == 1:
            print(agendamento)
            n = opcoes()

        elif n == 2:
            print('Digite o número do dia da semana que deseja agendar :')
            x = int(input())

            if x == 1:
                print('\nAGENDAMENTO EFETUADO COM SUCESSO')
                agendamento = '1 - Domingo: OCUPADO\n2 - Segunda: Livre\n3 - Terça: Livre\n4 - Quarta: Livre\n5 - Quinta: Livre\n6 - Sexta: Livre\n7 - Sábado: Livre'
                n = opcoes()
            if x == 2:
                print('\nAGENDAMENTO EFETUADO COM SUCESSO')
                agendamento = '1 - Domingo: Livre\n2 - Segunda: OCUPADO\n3 - Terça: Livre\n4 - Quarta: Livre\n5 - Quinta: Livre\n6 - Sexta: Livre\n7 - Sábado: Livre'
                n = opcoes()
            if x == 3:
                print('\nAGENDAMENTO EFETUADO COM SUCESSO')
                agendamento = '1 - Domingo: Livre\n2 - Segunda: Livre\n3 - Terça: OCUPADO\n4 - Quarta: Livre\n5 - Quinta: Livre\n6 - Sexta: Livre\n7 - Sábado: Livre'
                n = opcoes()

            if x == 4:
                print('\nAGENDAMENTO EFETUADO COM SUCESSO')
                agendamento = '1 - Domingo: Livre\n2 - Segunda: Livre\n3 - Terça: Livre\n4 - Quarta: OCUPADO\n5 - Quinta: Livre\n6 - Sexta: Livre\n7 - Sábado: Livre'
                n = opcoes()
            if x == 5:
                print('\nAGENDAMENTO EFETUADO COM SUCESSO')
                agendamento = '1 - Domingo: Livre\n2 - Segunda: Livre\n3 - Terça: Livre\n4 - Quarta: Livre\n5 - Quinta: OCUPADO\n6 - Sexta: Livre\n7 - Sábado: Livre'
                n = opcoes()

            if x == 6:
                print('\nAGENDAMENTO EFETUADO COM SUCESSO')
                agendamento = '1 - Domingo: Livre\n2 - Segunda: Livre\n3 - Terça: Livre\n4 - Quarta: Livre\n5 - Quinta: Livre\n6 - Sexta: OCUPADO\n7 - Sábado: Livre'
                n = opcoes()

            if x == 7:
                print('\nAGENDAMENTO EFETUADO COM SUCESSO')
                agendamento = '1 - Domingo: Livre\n2 - Segunda: Livre\n3 - Terça: Livre\n4 - Quarta: Livre\n5 - Quinta: Livre\n6 - Sexta: Livre\n7 - Sábado: OCUPADO'
                n = opcoes()

        elif n == 3:
            print('Digite o número do dia que deseja excluir :')
            x = int(input())
            agendamento = agendamento.replace('OCUPADO','Livre')
            n = opcoes()

        elif n == 4:
            print('Digite o dia da semana que deseja editar')
            y = int(input())
            n = 2
        
print('{:=^50}'.format('Programa Finalizado'))
