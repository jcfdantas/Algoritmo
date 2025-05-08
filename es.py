t = int(input("Digite o tamanho da Lista: "))
L = []
for i in range(t):
 
    v = int(input(f"Digite o valor da lista na posição[{i+1}]: "))
    L.append(v)
s = 0
for i in range(t):

    s += L[i]
print(f"A lista atual é {L}")
print(f"A soma dos números da lista é: {s}")