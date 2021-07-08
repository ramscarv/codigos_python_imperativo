def b_d(n):
    decimal = 0
    n = str(n)
    n = n[::-1]
    tam = len(n)
    o=int(input("digite 0 para parar ou qualquer outro número para prosseguir:"))
    while o!=0:
        for i in range(tam):
            if n[i]!="1" and n[i]!="0":
                exit()
            if n[i] == "1":
                decimal = decimal + 2**i
        print(decimal)
        m=int(input("digite um número binário: "))
        o=int(input("digite 0 para parar ou qualquer outro número para prosseguir"))
    print("Thanks for use my algorithm")

    
    
'''
def b_d2(x):
    decimal=0
    x=str(x)
    x=x[::-1]
    tam=len(x)
    i=0
    while i<tam:
        if x[i]!="1" and x[i]!="0":
            exit()
        if x[i]=="1":
            decimal = decimal + 2**i
        i += 1
    return decimal
'''
