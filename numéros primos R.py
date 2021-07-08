def primo(a):
    c = 1
    div = 0
    while c <= a:
        if a % c == 0:
            div = div + 1
        c = c + 1
    
    if div <= 2:
       return True
    else:
        return False


b = int (input())
if b <= 0:
    print ("errow")
    exit()
    
print("números primos")
cont = 1
while cont <= b:
    if primo(cont):
        print (cont, end=", ")
    cont = cont + 1
         
        
    
