def dias():
    print(" 1-Domingo\n 2-Segunda-feira\n 3-Terça-feira\n 4-Quarta-feira")
    print(" 5-Quinta-feira\n 6-Sexta-feira\n 7-Sábado")
def mudar():
     print("Deseja mudar o agendamento para qual dia")
    
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
        dias()
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
        print("AGENDAMENTO FEITO COM SUCESSO")
        
    if esc == 3:
        print("EXCLUIR AGENDAMENTO")
        print("Qual dia deseja cancelar o agendamento?")
        dias()
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
        print("AGENDAMENTO EXCLUIDO COM SUCESSO")
    if esc == 4:
        print("EDITAR AGENDAMENTO")
        print("Deseja editar qual agendamento?")
        dias()
        c = int(input())

        if c == 1:
            mudar()
            print(" 2-Segunda-feira\n 3-Terça-feira\n 4-Quarta-feira")
            print(" 5-Quinta-feira\n 6-Sexta-feira\n 7-Sábado")
            j = int(input())
            if j == 2:
                if seg == l:
                    seg = o
                    dom = l
                elif seg == o:
                    print("Esse dia ja está ocupado!")
            if j == 3:
                if ter == l:
                    ter = o
                    dom = l
                elif ter == o:
                    print("Esse dia ja está ocupado!")
            if j == 4:
                if qua == l:
                    qua = o
                    dom = l
                elif qua == o:
                    print("Esse dia ja está ocupado!")
            if j == 5:
                if qui == l:
                    qui = o
                    dom = l
                elif qui == o:
                    print("Esse dia ja está ocupado!")
            if j == 6:
                if sex == l:
                    sex = o
                    dom = l
                elif sex == o:
                    print("Esse dia ja está ocupado!")
            if j == 7:
                if sab == l:
                    sab = o
                    dom = l
                elif sab == o:
                    print("Esse dia ja está ocupado!")
             
        if c == 2:
            mudar()
            print(" 1-Domingo\n 3-Terça-feira\n 4-Quarta-feira")
            print(" 5-Quinta-feira\n 6-Sexta-feira\n 7-Sábado")
            j = int(input())
            if j == 1:
                if dom == l:
                    dom = o
                    seg = l
                elif dom == o:
                    print("Esse dia ja está ocupado!")
            if j == 3:
                if ter== l:
                    ter = o
                    seg = l
                elif ter == o:
                    print("Esse dia ja está ocupado!")
            if j == 4:
                if qua == l:
                    qua = o
                    seg = l
                elif qua == o:
                    print("Esse dia ja está ocupado!")
            if j == 5:
                if qui == l:
                    qui = o
                    seg = l
                elif qui == o:
                    print("Esse dia ja está ocupado!")
            if j == 6:
                if sex == l:
                    sex = o
                    seg = l
                elif sex == o:
                    print("Esse dia ja está ocupado!")
            if j == 7:
                if sab == l:
                    sab = o
                    seg = l
                elif sab == o:
                    print("Esse dia ja está ocupado!")
             
        if c == 3:
            mudar()
            print(" 1-Domingo\n 2-Segunda-feira\n 4-Quarta-feira")
            print(" 5-Quinta-feira\n 6-Sexta-feira\n 7-Sábado")
            j = int(input())
            if j == 1:
                if dom == l:
                    dom = o
                    ter = l
                elif dom == o:
                    print("Esse dia ja está ocupado!")
            if j == 2:
                if seg == l:
                    seg = o
                    ter = l
                elif seg == o:
                    print("Esse dia ja está ocupado!")
            if j == 4:
                if qua == l:
                    qua = o
                    ter = l
                elif qua == o:
                    print("Esse dia ja está ocupado!")
            if j == 5:
                if qui == l:
                    qui = o
                    ter = l
                elif qui == o:
                    print("Esse dia ja está ocupado!")
            if j == 6:
                if sex == l:
                    sex = o
                    ter = l
                elif sex == o:
                    print("Esse dia ja está ocupado!")
            if j == 7:
                if sab == l:
                    sab = o
                    ter = l
                elif sab == o:
                    print("Esse dia ja está ocupado!")
        if c == 4:
            mudar()
            print(" 1-Domingo\n 2-Segunda-feira\n 3-Terça-feira")
            print(" 5-Quinta-feira\n 6-Sexta-feira\n 7-Sábado")
            j = int(input())
            if j == 1:
                if dom == l:
                    dom = o
                    qua = l
                elif dom == o:
                    print("Esse dia ja está ocupado!")
            if j == 2:
                if seg == l:
                    seg = o
                    qua= l
                elif seg == o:
                    print("Esse dia ja está ocupado!")
            if j == 3:
                if qui == l:
                    qui = o
                    qua = l
                elif qui == o:
                    print("Esse dia ja está ocupado!")
            if j == 5:
                if qui == l:
                    qui = o
                    qua = l
                elif qui == o:
                    print("Esse dia ja está ocupado!")
            if j == 6:
                if sex == l:
                    sex = o
                    qua = l
                elif sex == o:
                    print("Esse dia ja está ocupado!")
            if j == 7:
                if sab == l:
                    sab = o
                    qua = l
                elif sab == o:
                    print("Esse dia ja está ocupado!")
        if c == 5:
            mudar()
            print(" 1-Domingo\n 2-Segunda-feira\n 3-Terça-feira")
            print(" 4-Quarta-feira\n 6-Sexta-feira\n 7-Sábado")
            j = int(input())
            if j == 1:
                if dom == l:
                    dom = o
                    qui = l
                elif dom == o:
                    print("Esse dia ja está ocupado!")
            if j == 2:
                if seg == l:
                    seg = o
                    qui = l
                elif seg == o:
                    print("Esse dia ja está ocupado!")
            if j == 3:
                if ter == l:
                    ter = o
                    qui = l
                elif ter == o:
                    print("Esse dia ja está ocupado!")
            if j == 4:
                if qua == l:
                    qua = o
                    qui = l
                elif qua == o:
                    print("Esse dia ja está ocupado!")
            if j == 6:
                if sex == l:
                    sex = o
                    qui = l
                elif sex == o:
                    print("Esse dia ja está ocupado!")
            if j == 7:
                if sab == l:
                    sab = o
                    qui = l
                elif sab == o:
                    print("Esse dia ja está ocupado!")
        if c == 6:
            mudar()
            print(" 1-Domingo\n 2-Segunda-feira\n 3-Terça-feira")
            print(" 4-Quarta-feira\n 5-Quinta-feira\n 7-Sábado")
            j = int(input())
            if j == 1:
                if dom == l:
                    dom = o
                    sex = l
                elif dom == o:
                    print("Esse dia ja está ocupado!")
            if j == 2:
                if seg == l:
                    seg = o
                    sex = l
                elif seg == o:
                    print("Esse dia ja está ocupado!")
            if j == 3:
                if ter == l:
                    ter = o
                    sex = l
                elif ter == o:
                    print("Esse dia ja está ocupado!")
            if j == 4:
                if qua == l:
                    qua = o
                    sex = l
                elif qua == o:
                    print("Esse dia ja está ocupado!")
            if j == 5:
                if qui == l:
                    qui = o
                    sex = l
                elif qui == o:
                    print("Esse dia ja está ocupado!")
            if j == 7:
                if sab == l:
                    sab = o
                    sex = l
                elif sab == o:
                    print("Esse dia ja está ocupado!")
        if c == 7:
            mudar()
            print(" 1-Domingo\n 2-Segunda-feira\n 3-Terça-feira")
            print(" 4-Quarta-feira\n 5-Quinta-feira\n 6-Sexta-feira")
            j = int(input())
            if j == 1:
                if dom == l:
                    dom = o
                    sab = l
                elif dom== o:
                    print("Esse dia ja está ocupado!")
            if j == 2:
                if seg == l:
                    seg = o
                    sab = l
                elif seg == o:
                    print("Esse dia ja está ocupado!")
            if j == 3:
                if ter == l:
                    ter = o
                    sab = l
                elif ter == o:
                    print("Esse dia ja está ocupado!")
            if j == 4:
                if qua == l:
                    qua = o
                    sab = l
                elif qua == o:
                    print("Esse dia ja está ocupado!")
            if j == 5:
                if qui == l:
                    qui = o
                    sab = l
                elif qui == o:
                    print("Esse dia ja está ocupado!")
            if j == 6:
                if sex == l:
                    sex = o
                    sab = l
                elif sex == o:
                    print("Esse dia ja está ocupado!")
                   
        print("MUDANÇA FEITA COM SUCESSO")       




    
