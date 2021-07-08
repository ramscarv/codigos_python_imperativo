m=input("digite uma frase ou palavra: ")
f=input("digite uma letra para ver a quantidade repete:")
f=m.count(f)
print(f)
'''
na função não irá aparecer nenhuma mensagem pedindo
para você inserir algo basta escrever a frase ou palavra
na variavel (p) e a palavra para checar a quantidade na variavel (l)
não esqueça de por "" ou '' quando for usar a função 
'''
def quant_carac(p,l):
    l=p.count(l)
    return(l)
