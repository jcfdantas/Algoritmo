m =[]
t = int(input("Digite o tamanho da matriz: "))
for i in range(t):
    l =[]
    for j in range(t):
        v = int(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
        l.append(v)
    m.append(l)
for l in m:
    print("|", end= " ")
    for v in l:
        print(f"[{v}", end=" ")
    print("]|")