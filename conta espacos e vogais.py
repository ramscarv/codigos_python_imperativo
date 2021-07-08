nome = str(input("Digite um baguio ae, irmao: "))
cont = 0
c = 0
letra = str
for letra in nome:
    if letra == "a":
        cont += 1
    if letra == "e":
        cont += 1
    elif letra == "i":
        cont += 1
    elif letra == "o":
        cont += 1
    elif letra == "u":
        cont += 1
print("Vogais:",cont)
for letra in nome:
    if letra ==" ":
        c+=1
print("Espaco(s) em branco:", c)
