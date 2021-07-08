nome = (input("Digite seu nome completo: "))
y = nome[::-1]
z = " "
for c in y:
    z = c + z
    if c == " ":
        break
z = z[1:len(z)]
print("Bom dia, SR(a)",z)
