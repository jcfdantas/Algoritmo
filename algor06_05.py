m =[]
for i in range(4):
    linha=[]
    for j in range(4):
       vlr=int(input(f"Digite o valor para a posição[{i+1}][{j+1}]: "))
       linha.append(vlr)
    m.append(linha)
print(f"Essa é sua matriz inicial:{m}")
diagonal_principal=[]
soma_principal=0
for i in range(len(m)):
    diagonal_principal.append(m[i][i])
    soma_principal += m[i][i]
print(f"Diagonal principal: {diagonal_principal}")
print(f"soma principal: {soma_principal}")

d_s= []
s_s=0
for i in range(len(m)):
    d_s.append(m[i][(len(m[1])) - 1 - i])
    s_s += m[i][(len(m[1])) - 1 - i]
print(f"Diagonal secundária: {d_s}")
print(f"soma principalsecunsária = {s_s}")