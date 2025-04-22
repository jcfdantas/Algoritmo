A = [
    [1, 2], [5, 6]
]
B = [
    [7, 8], [9,5]
]

soma = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range (len(A))]
# jeito para imprimir mais bonitinho print(f"A[{i}][{j}] + B[{i}][{j}] = {A[i][j]} + {B[i][j]}")
#for j in range(len=(A[0])) percorre a A[0] e j percorre a quantidade de numeros em A[0]

#for i in range (len(A)) quantidade de "vetores" na matriz A 

#tudo em matriz[], range(), len()

print("Resultado da soma de matrizes é: ")
print(soma)

