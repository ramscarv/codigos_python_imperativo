p = list()
pp = dict()
n = True
m = 0
mm = 0
while(n == True):
    pp['nome'] = input("digite o nome: ")
    pp["sexo"] = input("digite o sexo: [F/M] ")
    m = int(input("digite a idade: "))
    mm = m+mm
    pp['idade'] = m
    p.append(pp.copy())
    d = input("pretende continuar? [S/N] ")
    if d in 'nN':
        n = False
mt = mm/len(p)
print(f'o grupo tem {len(p)} pessoas')
print('\n')
print(f'media de idade igual a {mt}')
print('\n')
print(f'as mulheres cadastradas foram:')
print('\n')
for k,v in enumerate(p):
    if (p[k]['sexo'] == 'f'):
        print(f"{p[k]['nome']}", end="")
print('\n')
print("lista de pessoas acima da media de idade: ")
print('\n')
for k,v in enumerate(p):
    if(p[k]['idade'] > mt):
        print(f"{p[k]['nome']}", end="")