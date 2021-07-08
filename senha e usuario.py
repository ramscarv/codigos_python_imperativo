print("Nome do usuário:")
nome=input()
print("senha:")
key=input()

while nome==key:
    print("senha inválida, digite o usuário e a senha novamente")
    nome=str(input("Nome do usuário:"))
    key=str(input("senha:"))

print("fim")

