def primos(n):
    n2 = n
    cont = 0

    while n2 >=1 :
        if n % n2 == 0:
            cont = cont + 1
        n2 = n2 - 1

    return cont <= 2
      


print("digite um número:")
n1 = float(input())
n = 1

while n<=n1:
    if primos(n):
       print(n)
    n = n + 1
    
print("fim")    
