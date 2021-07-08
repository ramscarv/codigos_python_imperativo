
n=int(input("digite um número inteiro > que 0: "))
a=[]
b=1
while b<=n:
    a.append(b)
    b+=1

i=len(a)-1
while i>=0:
    print(a[i],end=" ")
    i-=1
'''
#mesmo algoritmo mas com range
n=int(input("digite um número inteiro > que 0: "))
a=[]
for b in range(1,n+1):
    if b<=n:
        a.append(b)
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")
'''    
