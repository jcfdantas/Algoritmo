#n1 = float(input("Digite o primeiro número: "))
#n2 = float(input("Digite o segundo número: "))
#def soma(n1,n2):
#    print (n1 + n2)

#soma(n1,n2)     

#graus = float(input("Digite graus a serem convertidos para Fahrenheit: "))
#def transformar(graus):
#    F = graus * 9/5 + 32
#    print(F)

#transformar(graus)
t=int(input("Digite o tamanho da lista: "))
l = []
for x in range(t):
    v = int(input("Digite o próximo numero para a lista: "))
    l.append(v)

def achar(l):
    nl=[]
    for w in range(len(l)):     
        if l[w] % 2 == 0:
            nl.append(l[w])
    print(nl)

achar(l)