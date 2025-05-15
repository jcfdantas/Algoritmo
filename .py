m = []
t = int(input("Digite o tamanho da matriz: "))
for i in range(t):
    l =[]
    for j in range(t):
        n = int(input(f"Digite o numero para o valor para a posição [{i+1}][{j+1}]: "))
        l.append(n)
    m.append(l)

for i in range(t):
        print("|", m[i], "|")
