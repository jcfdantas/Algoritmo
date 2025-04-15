# Inicializa uma matriz vazia
matriz = []

print("Digite os valores para a matriz 3x3:")

# Loop pelas linhas
for i in range(3):
    linha = []
    # Loop pelas colunas
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Mostra a matriz formatada
print("\nMatriz 3x3:")
for linha in matriz:
    print(linha)
