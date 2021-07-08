n=int(input("Digite um valor inteiro: "))
m=int(input("Digite um valor inteiro diferente: "))
par=0
impar=0
if n < m:
    c=n+1
    while c <= m+1:
        c=c+1
        if c%2==0:
            par=par+1
        elif c%2!=0:
            impar=impar+1
    print("pares:",par)
    print("impares:",impar)

elif n>m:
    c=n-1
    while c >= m-1:
        c=c-1
        if c%2==0:
            par=par+1
        elif c%2!=0:
            impar=impar+1
    print("pares: ",par)
    print("impares: ",impar)
        
        
