t = int(input("Digite o tamanho da Lista: "))
L = []
for i in range(t):
 
    v = int(input(f"Digite o valor da lista na posição[{i+1}]: "))
    L.append(v)
m = []
n = int(input("Digite o numero que multiplicará a lista: "))
for i in range(t):
  m[(L[i])]+= L[i]*n
print(f"A lista atual é {L}")
print(f"A soma dos números da lista é: {m}")