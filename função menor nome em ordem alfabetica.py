def nomes(nomealfa):
    min=nomealfa[0]
    i=1
    while i < len(nomealfa):
        if nomealfa[i] < min:
            min=nomealfa[i]
        i=i+1
    return min.strip().capitalize()

def teste_pontual(nomea,nome_esperado):
    nome_calculado=nomes(nomea)
    if nome_calculado != nome_esperado:
        print("nome errado para array",nomea)
        print("nome esperado: ", nome_esperado,"nome calculado", nome_calculado)

def testa_nomes():
    print("Iniciando os testes")
    teste_pontual(["A"], "A")
    teste_pontual(["A","A","A","A"], "A")
    teste_pontual(["luis","carll","kratos"], "Carll")
    teste_pontual(["henrique","escobar","kate"], "Escobar")
    print("Testes Finalizados")
    
    
    
