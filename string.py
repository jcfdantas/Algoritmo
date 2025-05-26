n = str(input("Digite uma palavra: "))
n1=str(input("Digite outra palavra: "))
n2=str(input("Digite a ultima palavra: "))
a = int(input("Você deseja ordenalas por ordem alfábética(1) ou por número de letras(2): "))
if a == 1:
    print(sorted[n,n1,n2])
elif a==2:
    palavras = [n, n1, n2]
    tamanhos = [len(n), len(n1), len(n2)]
    # Cria tuplas para facilitar a ordenação
    combinadas = list(zip(palavras, tamanhos))
    # Ordena pela quantidade de letras
    combinadas.sort(key=lambda x: x[1])

    # Desempacota as palavras já ordenadas
    n, n1, n2 = combinadas[0][0], combinadas[1][0], combinadas[2][0]

    # Usando match/case apenas como exemplo ilustrativo
    match True:
        case _ if len(n) == len(n1) == len(n2):
            print("Todas têm o mesmo tamanho.")
        case _ if len(n) == len(n1) or len(n1) == len(n2) or len(n) == len(n2):
            print("Algumas têm o mesmo tamanho.")
        case _:
            print("Todas têm tamanhos diferentes.")
else:
    print("Digite a opçao 1 ou 2, escolha inválida.")
