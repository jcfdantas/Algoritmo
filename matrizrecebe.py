matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
print()
print("Primeira Matriz:")
print()
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[0])):
        receber = int(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
        linha.append(receber)
    matriz.append(linha)
print()
print("Segunda Matriz")
print()
for i in range(len(B)):
    linha = []
    for j in range(len(B[0])):
        receber = int(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
        linha.append(receber)
    B.append(linha)

soma = [[matriz[p][l] + B[p][l] for l in range(len(matriz[0]))] for p in range(len(matriz))]

print(soma)
#tudo em matriz[], range(), len()