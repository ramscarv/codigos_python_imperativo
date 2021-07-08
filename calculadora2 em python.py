def soma(x,y):
    print(x,"+",y,"=",x+y)
def subtração(x,y):
    print(x,"-",y,"=",x-y)
def multiplicação(x,y):
    print(x,"*",y,"=",x*y)
def divisão(x,y):
    print(x,"/",y,"=",x/y)

n=float(input(" digite o primeiro número: "))
n1=float(input(" digite o segundo número: "))
print("digite 1 para somar,2 para subtrair, 3 para multiplicar, 4 para dividir e 0 para sair")
o=int(input())
while o!=0:
    if o==1:
        soma(n,n1)
    elif o==2:
        subtração(n,n1)
    elif o==3:
        multiplicação(n,n1)
    elif o==4:
        divisão(n,n1)
    else:
        print("valor invalido")
    n=float(input(" digite o primeiro número: "))
    n1=float(input(" digite o segundo número: "))
    print("digite 1 para somar,2 para subtrair, 3 para multiplicar, 4 para dividir e 0 para sair")
    o=int(input())
print("até a próxima")
        
        
