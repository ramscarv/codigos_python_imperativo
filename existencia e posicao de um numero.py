import random
a = []
b = 1
cont = 0

while b<=100:
    a.append(b)
    b+=1
p=random.choice(a)
e=random.sample(range(1,100),(p))
print(e)
d = int(input("Digite um número para verificar se o mesmo existe na lista: "))
cont = 0
while cont < p-1:
    if e[cont]==d:
        print("o número",d,"está na posicao",cont," da lista")
        exit()
    cont += 1
print("não número ",d," nao está na lista")
    
    
