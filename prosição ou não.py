print("v é ou, V é símbolo proposisional")
x=input("digite uma proposição com símbolos : ")
a=0
i=0
b=len(x)
while(i<len(x)):
    if x[i]=="(" or x[i]=="¬" or x[i]==")":
        i+=1
        # colocar de A a Z usando tabela asc basta só colocar o número sem aspas
    else:

        if x[i]=="P" or x[i]=="Q":
            i+=1
            if i<b:
                if x[i]=="P" or x[i]=="Q":
                    a=1
                    break
        elif x[i]=="^" or x[i]=="v":
                if (x[i-1]=="P" or x[i-1]=="Q" or x[i-1]==")") and (x[i+1]=="P" or x[i+1]=="Q" or x[i+1]=="(" or x[i+1]=="¬"):
                    i+=1
                else:
                    a=1
                    break
        elif x[i]=="-":
            if (x[i-1]=="P" or x[i-1]=="Q"  or x[i-1]==")") and (x[i+2]=="P" or x[i+2]=="Q" or x[i+2]=="(" or x[i+2]=="¬"):
                    i+=2
            else:
                 a=1
                 break
        elif x[i]=="<":
            if (x[i-1]=="P" or x[i-1]=="Q" or x[i-1]==")") and (x[i+3]=="P" or x[i+3]=="Q" or x[i+3]=="(" or x[i+3]=="¬"):
                    i+=3
            else:
                a=1
                break
        else:
            a=1
            break
if a==0:
    print("É proposição")
else:
    print("não é proposoção")

            
