def findletra(x,y):
    cont = 0
    for i in x:
        if i == y:
            cont = cont + 1
    return cont        
       
print("Digite uma palavra ou frase.\nObs:somente letras minúsculas")
x = input()
print("Qual letra deseja sabe a quantidade")
y = input()

z = findletra(x,y)
print(z)
