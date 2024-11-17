n = [0]*50
def Dados():
    i = 1
    a = 0
    while(i<=50):
        print("Digite o:", a+1, "/50 elemento")
        n[a] = input()
        
        print("")
        
        a = a + 1
        i = i + 1
        
        print("")
        print("")
        
        
    k = 0
    j = 1
    while(k<a):
        print("Dados imprimidos ",j, "/50: ",n[k])
        k = k + 1
        j = j + 1

Dados()
input()