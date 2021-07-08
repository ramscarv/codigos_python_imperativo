print("CALCULADORA\nQUE OPERAÇÃO DESEJA FAZER:")
print("Tecle 1 para SOMA\nTecle 2 para SUBTRAÇÃO")
print("Tecle 3 para MULTIPLICAÇÃO\ntecle 4 para DIVISÃO")
print("tecle 0 se deseja SAIR")
top = int(input())

while top != 0 :
    if  top<0 or top>4:
        print("Não existe essa opção \n")
    else:
        print("Digite dois número:")
        n1 = float(input())
        n2 = float(input())
        if top == 1:
            print(n1," + ",n2," = ",n1+n2)

        elif top == 2:
            print(n1," - ",n2," = ",n1-n2)

        elif top == 3:
            print(n1," X ",n2," = ",n1*n2)

        else:
           print(n1," / ",n2," = ",n1/n2)
           
    print("DESEJA FAZER OUTRA OPERAÇÃO?")
    print("Tecle 1 para SOMA\nTecle 2 para SUBTRAÇÃO")
    print("Tecle 3 para MULTIPLICAÇÃO\ntecle 4 para DIVISÃO")
    print("tecle 0 se deseja SAIR")
    top = int(input())
      
print("Tchau '-'")


