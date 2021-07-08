print("Locaçâo de Espaço de Eventos")
print()
print("Tecle 1, para LISTAR LOCAÇÔES")
print("Tecle 2, para LOCAR")
print("Tecle 3, para EXCLUIR LOCAÇÂO")
print("Tecle 0, para SAIR")
r = int(input())
d = 0
l = ("LIVRE")
o = ("OCUPADO")
while 3 >= r >= 0:
    if r == 1:
        print("1-Domingo:",l)
        print("2-Segunda:",l)
        print("3-Terça:",l)
        print("4-Quarta:",l)
        print("5-Quinta:",l)
        print("6-Sexta:",l)
        print("7-Sábado:",l)
    elif r == 2:
        print("Qual dia o sr(a), deseja locar? ")
        print("1-Domingo:",l)
        print("2-Segunda:",l)
        print("3-Terça:",l)
        print("4-Quarta:",l)
        print("5-Quinta:",l)
        print("6-Sexta:",l)
        print("7-Sábado:",l)
        print("0-Sair")
        d = int(input("tecle um número q corresponda ao dia! "))
        if d == 1:
            print("1-Domingo:",o)
        elif d == 2:
            print("2-Segunda:",o)
        elif d == 3:
            print("3-Terça:",o)
        elif d == 4:
            print("4-Quarta:",o)
        elif d == 5:
            print("5-Quinta:",o)
        elif d == 6:
            print("6-Sexta:",o)
        elif d == 7:
            print("7-Sábado:",o)
        elif d == 0:
            print("Saiu")
    elif r == 3:
        print("Qual LOCAÇÂO o sr(a), deseja excluir? ")
        d= int(input())
        print("1-Domingo:")
        print("2-Segunda:")
        print("3-Terça:")
        print("4-Quarta:")
        print("5-Quinta:")
        print("6-Sexta:")
        print("7-Sábado:")
        print("0-Sair")
        if d == 1:
            print()
            print("1-Domingo:",l)
        elif d == 2:
            print()
            print("2-Segunda:",l)
        elif d == 3:
            print()
            print("3-Terça:",l)
        elif d == 4:
            print()
            print("4-Quarta:",l)
        elif d == 5:
            print()
            print("5-Quinta:",l)
        elif d == 6:
            print()
            print("6-Sexta:",l)
        else:
            print("7-Sábado:",l)
    elif r == 0:
        print("Obrigado, e volte sempre!")
        break

    print()
    print("Locaçâo de Espaço de Eventos")
    print()
    print("Tecle 1, para LISTAR LOCAÇÔES")
    print("Tecle 2, para LOCAR")
    print("Tecle 3, para EXCLUIR LOCAÇÂO")
    print("Tecle 0, para SAIR")
    r = int(input())
    d = 0
    l = ("LIVRE")
    o = ("OCUPADO")
         
