m = []
t = int(input("Digiteo tamanho da matriz: "))
for i in range(t):
    linha = []
    for j in range(t):
        v = int(input(f"Digite o valor da matriz para a posição [{i+1}][{j+1}]: "))
        linha.append(v)
    m.append(linha)
print("="*50)
print(f"Essa é sua matriz inicial:")
#para imprimir configurado é necessario usar for l in m: for v in l: print...
for linha in m:
        print("|", end=" ")
        for v in linha:
            print(f"{v:5}", end=" ")
        print("|")
s_p = 0
d_p = []
s_s = 0
d_s = []
for i in range(t):
    d_p.append(m[i][i])
    s_p += m[i][i]

print(f"A diagonal principal é:\n{d_p}")
print(f"A soma da diagonal principal é:\n{s_p}")
print("="*50)
