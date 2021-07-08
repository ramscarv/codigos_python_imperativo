import random
d = dict()
f = list()
l = list()
for i  in range(0,4):
    d['nome'] = str(input("digite seu nome: "))
    d['dado'] = random.randint(1, 6)
    f.append(d.copy())
    print(d)
    l.append(d['dado'])
    d.clear()
l = sorted(l, reverse = True)
while(len(l)!= 0):
    i = 0
    for j in range(0, 4):
        if(l[i] == f[j]["dado"]):
            print(f"jogador {f[j]['nome']} tirou {l[i]} no dado")
            l.pop(0)