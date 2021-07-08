print("AGENDAMENTOS PARA EVENTOS")
o = "OCUPADO"
l = "LIVRE"
dom = l   
seg = l
ter = l
qua = l
qui = l
sex = l
sab = l
while True:
    print("O que deseja fazer?")
    print("1 para LISTAR AGENDAMENTOS\n2 para AGENDAR")
    print("3 para EXCLUIR AGENDAMENTO\n4 para EDITAR AGENDAMENTO")
    print("0 se deseja SAIR")
    esc = int(input())
    print("\n")
    if esc < 0 or esc > 4:
        print("ERROR: opção inválida")
    if esc == 0:
        print("Obrigado pela preferência!")
        break

    if esc == 1:
        print("LISTA DE AGENDAMENTOS")
        print("1 - Domingo:",dom)
        print("2 - Segunda-feira:",seg)
        print("3 - Terça-feira:",ter)
        print("4 - Quarta-feira:",qua)
        print("5 - Quinta-feira:",qui)
        print("6 - Sexta-feira:",sex)
        print("7 - Sábado:",sab,"\n")

    if esc == 2:
        print("FAZER AGENDAMENTO")
        print("Para qual dia deseja agendar?")
        print(" 1-Domingo\n 2-Segunda-feira\n 3-Terça-feira\n 4-Quarta-feira")
        print(" 5-Quinta-feira\n 6-Sexta-feira\n 7-Sábado")
        a = int(input())

        if a == 1:
            dom = o
        if a == 2:
            seg = o
        if a == 3:
            ter = o
        if a == 4:
            qua = o
        if a == 5:
            qui = o
        if a == 6:
            sex = o
        if a == 7:
            sab = o
        print("Agendamento feito com sucesso")
        
    if esc == 3:
        print("EXCLUIR AGENDAMENTO")
        print("Qual dia deseja cancelar o agendamento?")
        print(" 1-Domingo\n 2-Segunda-feira\n 3-Terça-feira\n 4-Quarta-feira")
        print(" 5-Quinta-feira\n 6-Sexta-feira\n 7-Sábado")
        b = int(input())
        if b == 1:
            dom = l
        if b == 2:
            seg = l
        if b == 3:
            ter = l
        if b == 4:
            qua = l
        if b == 5:
            qui = l
        if b == 6:
            sex = l
        if b == 7:
            sab = l    

    if esc == 4:
        print("EDITAR AGENDAMENTO")
        print("Deseja editar qual agendamento")
        print(" 1-Domingo\n 2-Segunda-feira\n 3-Terça-feira\n 4-Quarta-feira")
        print(" 5-Quinta-feira\n 6-Sexta-feira\n 7-Sábado")
        c = int(input())

        if c == 1:
            if dom == l:
                print("Esse dia ja está livre, deseja agenda-lo? Digite 1 para SIM e 2 para NÃO")
                s = int(input())
                if s == 1:
                    dom = o
            elif dom == o:
                dom = l        
        if c == 2:
            if dom == o:
                dom = l
            if dom == l:
                print("Esse dia ja está livre, deseja agenda-lo? Digite 1 para SIM e 2 para NÃO")
                s = int(input())
                if s == 1:
                    dom = o
        if c == 3:
            if dom == o:
                dom = l
            if dom == l:
                print("Esse dia ja está livre, deseja agenda-lo? Digite 1 para SIM e 2 para NÃO")
                s = int(input())
                if s == 1:
                    dom = o
        if c == 4:
            if dom == o:
                dom = l
            if dom == l:
                print("Esse dia ja está livre, deseja agenda-lo? Digite 1 para SIM e 2 para NÃO")
                s = int(input())
                if s == 1:
                    dom = o
        if c == 5:
            if dom == o:
                dom = l
            if dom == l:
                print("Esse dia ja está livre, deseja agenda-lo? Digite 1 para SIM e 2 para NÃO")
                s = int(input())
                if s == 1:
                    dom = o
        if c == 6:
            if dom == o:
                dom = l
            if dom == l:
                print("Esse dia ja está livre, deseja agenda-lo? Digite 1 para SIM e 2 para NÃO")
                s = int(input())
                if s == 1:
                    dom = o
        if c == 7:
            if sab == o:
                sab = l
            if sab == l:
                print("Esse dia ja está livre, deseja agenda-lo? Digite 1 para SIM e 2 para NÃO")
                s = int(input())
                if s == 1:
                    sab = o
                   
               




    
