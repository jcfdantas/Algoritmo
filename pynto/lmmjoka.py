"""
=============================
LISTA DE EXERCÍCIOS – MATRIZES E MANIPULAÇÃO DE DADOS
=============================
Exercícios de revisão baseados nos conceitos do primeiro semestre
Aluno: 
"""
notasex21 = []
banco_dadosex22 = {
  "aluno_001": {"nome": "Ana", "nota": 8.5},
    "aluno_002": {"nome": "Bruno", "nota": 7.0},
    "aluno_003": {"nome": "Carla", "nota": 9.2},
    "aluno_004": {"nome": "Daniel", "nota": 6.8},
    "aluno_005": {"nome": "Eduarda", "nota": 7.5},
    "aluno_006": {"nome": "Felipe", "nota": 8.0},
    "aluno_007": {"nome": "Gabriela", "nota": 9.0},
    "aluno_008": {"nome": "Henrique", "nota": 5.5},
    "aluno_009": {"nome": "Isabela", "nota": 6.0},
    "aluno_010": {"nome": "João", "nota": 7.8},
    "aluno_011": {"nome": "Larissa", "nota": 8.3},
    "aluno_012": {"nome": "Marcos", "nota": 6.7}}
a = [[1, 2, 3],
     [4, 5, 6]]

b = [[7, 8, 9],
     [1, 2, 3]]
matriz = [[1, 2, 3],                                  # matriz utilizada
          [4, 5, 6],
          [7, 8, 9]]
escalar = 100   

# =============================
# 1. OPERAÇÕES BÁSICAS COM MATRIZES
# =============================


def ex1():
    
    matriz = [[0,0,0], [0,0,0]]
    print(matriz)



def ex2(a, b):        
  resultado = []                                   # Cria uma lista vazia para armazenar o resultado

  for i in range(len(a)):                          # Percorre as linhas da matriz     
        linha = []                                   # Cria uma nova linha para a matriz resultado

        for j in range(len(a[0])):                   # Percorre as colunas da matriz
             linha.append(a[i][j] + b[i][j])         # Soma os elementos correspondentes de 'a' e 'b'
        
        resultado.append(linha)                      # Adiciona a linha somada à matriz resultado
    
  print( resultado)                            # Retorna a matriz resultante



def ex3(matriz, escalar):
  # define a função 
    resultado = []                                    # Cria uma lista vazia para armazenar o resultado
    for linha in matriz:                              # serve para percorrer cada linha da matriz, uma por uma.
        nova_linha = []                               # Cria uma nova linha para a matriz resultado
        for elemento in linha:                        # serve para percorrer cada item de linha, um por um
            nova_linha.append(elemento * escalar)     # multiplica os elementos por um valor escalar e coloca o resultado à lista nova_linha.
        resultado.append(nova_linha)                  # serve para adicionar a lista nova_linha dentro da lista resultado.
    print(resultado)                                  # exibição do resultado

def ex4(matriz):
  transposta = [list(linha) for linha in zip(*matriz)]                # Essa linha desempacota a matriz, usa zip para trocar linhas por colunas, 
  for linha in transposta:                                     # Esse código vai linha por linha da matriz transposta e imprime cada uma, 
      print(linha)          
ex4(matriz)

def ex5(matriz):
    matriz_espelhada = ( [linha[::-1] for linha in matriz]   )                # Para cada linha da matriz, inverta os elementos e 
    for linha in matriz_espelhada:
        print(linha) 


# =============================
# 2. ANÁLISE DE MATRIZES
# =============================

def ex6(matriz):
    if not matriz or not matriz[0]:               # esse if é usado para garantir que a matriz não esteja vazia e 
                                                  # que sua primeira linha também tenha elementos, evitando erros ao acessar índices.
        return None, None                         # Essa linha faz a função parar e retornar uma tupla com dois valores nulos: `(None, None)`.

    
    maior = menor = matriz[0][0]                  # define que tanto maior quanto menor começam com o valor do primeiro elemento da matriz.
    for linha in matriz:                          # para cada linha dentro da matriz, execute o bloco de código seguinte.
        for elemento in linha:
            if elemento > maior:                  # para cada elemento dentro da linha atual, execute o bloco de código seguinte.
                maior = elemento                  # atribui o valor do elemento atual à variável maior, geralmente quando se encontrou um valor maior que o anterior.
            if elemento < menor:                  # verifica se o elemento atual é menor que a variável menor; se for, o bloco do if será executado.
                menor = elemento                  # atribui o valor do elemento atual à variável menor, geralmente quando se encontrou um valor menor que o anterior.
    print("O maior elemento é: ", maior, "\n","O menor elemento é: ", menor)  


def ex7(matriz):
  soma = 0                                                            # cria a variável soma e a inicializa com 0, geralmente para acumular valores depois.
  for i in range(len(matriz)):                                        # percorrer os índices de 0 até o tamanho da matriz menos 1, permitindo acessar cada linha pelo índice i.
        soma += matriz[i][i]                                            # adiciona o elemento da diagonal principal da matriz à variável soma, acumulando os valores ao longo do loop. 
  print("Soma da diagonal principal: ", soma )                                                        # faz a função parar e devolver o valor atual da variável soma como resultado.


def ex8(matriz):
  n = len(matriz)                                                             # cria a variável n e armazena o número de linhas da matriz, obtido com len(matriz).
  soma = 0                                                                    # inicializa a variável soma com 0, geralmente para acumular valores em um loop.
  for i in range(n):                                                          # percorrer os índices de 0 até n‑1, permitindo acessar elementos da matriz usando i.
        soma += matriz[i][n - 1 - i]                                            # adiciona à variável soma o elemento da diagonal secundária da matriz, ou seja, o que está na posição [i][n - 1 - i].
  print("soma da diagonal secundaria:", soma )


def ex9(matriz):
  maiores = []                                   # cria uma lista vazia chamada maiores, geralmente para armazenar os maiores elementos de cada linha depois
  for linha in matriz:                           # para cada linha na matriz, execute o bloco de código seguinte.
        maiores.append(max(linha))                 # adiciona à lista maiores o maior valor da linha atual, usando a função max().
  print("maiores de cada linha: ", maiores)     


def ex10(matriz):
  contador = 0                                     # cria a variável contador e a inicializa com 0, geralmente para contar ocorrências dentro de um loop.
  for linha in matriz:                             # para cada linha na matriz, execute o bloco de código seguinte.
      for elemento in linha:                       # para cada elemento na linha atual, execute o bloco de código seguinte.
            if elemento % 2 == 0:                    # verifica se o elemento atual é par (ou seja, se o resto da divisão por 2 é igual a 0).
                contador += 1                        # incrementa a variável contador em 1, geralmente quando uma condição é atendida (como encontrar um número par).
  print("quantidade de numeros peres:", contador)   


# =============================
# 3. MATRIZES COM DADOS ALEATÓRIOS
# =============================

def ex11(linhas, colunas, min_val, max_val):
    """
    Exercício 11:
    Crie uma função que gere uma matriz com números aleatórios.
    Parâmetros:
      - linhas (int): número de linhas
      - colunas (int): número de colunas
      - min_val (int): valor mínimo dos números
      - max_val (int): valor máximo dos números
    Retorno:
      - list: matriz com números aleatórios
    """
    pass


def ex12(tamanho):
    """
    Exercício 12:
    Crie uma função que gere uma matriz identidade (diagonal principal = 1, resto = 0).
    Parâmetro:
      - tamanho (int): dimensão da matriz quadrada
    Retorno:
      - list: matriz identidade
    """
    pass


def ex13(matriz):
    """
    Exercício 13:
    Crie uma função que verifique se uma matriz é simétrica.
    Uma matriz é simétrica se A[i][j] = A[j][i] para todos i,j.
    Parâmetro:
      - matriz (list): matriz quadrada para verificar
    Retorno:
      - bool: True se for simétrica, False caso contrário
    """
    pass


# =============================
# 4. MANIPULAÇÃO DE STRINGS
# =============================

def ex14(texto1, texto2):
    """
    Exercício 14:
    Crie uma função que compare duas strings ignorando maiúsculas/minúsculas.
    Parâmetros:
      - texto1 (str): primeira string
      - texto2 (str): segunda string
    Retorno:
      - bool: True se forem iguais (ignorando case), False caso contrário
    """
    pass


def ex15(texto, palavra):
    """
    Exercício 15:
    Crie uma função que conte quantas vezes uma palavra aparece em um texto.
    Parâmetros:
      - texto (str): texto para buscar
      - palavra (str): palavra a ser contada
    Retorno:
      - int: número de ocorrências
    """
    pass


def ex16(texto):
    """
    Exercício 16:
    Crie uma função que remova espaços extras de uma string
    (início, fim e espaços duplos no meio).
    Parâmetro:
      - texto (str): texto a ser limpo
    Retorno:
      - str: texto limpo
    """
    pass


def ex17(texto, char_antigo, char_novo):
    """
    Exercício 17:
    Crie uma função que substitua todos os caracteres de um tipo por outro.
    Parâmetros:
      - texto (str): texto original
      - char_antigo (str): caractere a ser substituído
      - char_novo (str): caractere substituto
    Retorno:
      - str: texto com substituições
    """
    pass


def ex18(lista_palavras):
    """
    Exercício 18:
    Crie uma função que junte uma lista de palavras em uma única string,
    separadas por espaços.
    Parâmetro:
      - lista_palavras (list): lista de strings
    Retorno:
      - str: string única com palavras separadas por espaço
    """
    pass


# =============================
# 5. SISTEMAS DE DADOS (DICIONÁRIOS E LISTAS)
# =============================

def ex19():
    """
    Exercício 19:
    Crie uma função que inicialize um dicionário vazio para armazenar
    dados de alunos (nome como chave, lista de notas como valor).
    Retorno:
      - dict: dicionário vazio para alunos
    """
    pass


def ex20(banco_dados, nome, notas):
    """
    Exercício 20:
    Crie uma função que adicione um aluno e suas notas ao banco de dados.
    Parâmetros:
      - banco_dados (dict): dicionário de alunos
      - nome (str): nome do aluno
      - notas (list): lista de notas do aluno
    Retorno:
      - bool: True se adicionado com sucesso
    """
    pass

notasex21 = []
def ex21(notasex21):
  t = int(input("Digite quantas notas serão calculadas: "))
  for i in range(t):
    valor = int(input(f"Digite a {i+1}º nota: "))
    notasex21.append(valor)
  media = (sum (notasex21))/t
  print(f"A média é {media}")


def ex22(banco_dadosex22, nome):
    """
    Exercício 22:
    Crie uma função que busque um aluno no banco de dados e retorne suas notas.
    Parâmetros:
      - banco_dados (dict): dicionário de alunos
      - nome (str): nome do aluno a buscar
    Retorno:
      - list ou None: lista de notas do aluno ou None se não encontrado
    """
    pass


def ex23(produtos):
    """
    Exercício 23:
    Crie uma função que calcule o valor total do estoque.
    Cada produto é uma lista: [nome, preço, quantidade]
    Parâmetro:
      - produtos (list): lista de produtos
    Retorno:
      - float: valor total do estoque
    """
    pass


def ex24(produtos, nome_produto):
    """
    Exercício 24:
    Crie uma função que encontre um produto pelo nome na lista de produtos.
    Parâmetros:
      - produtos (list): lista de produtos
      - nome_produto (str): nome do produto a buscar
    Retorno:
      - list ou None: dados do produto ou None se não encontrado
    """
    pass


def ex25(produtos, nome_produto, novo_preco):
    """
    Exercício 25:
    Crie uma função que atualize o preço de um produto específico.
    Parâmetros:
      - produtos (list): lista de produtos
      - nome_produto (str): nome do produto
      - novo_preco (float): novo preço do produto
    Retorno:
      - bool: True se atualizado com sucesso, False se produto não encontrado
    """
    pass


# =============================
# 6. EXERCÍCIOS INTEGRADOS
# =============================

def ex26(matriz):
    """
    Exercício 26:
    Crie uma função que receba uma matriz e retorne um dicionário com:
    - 'soma_total': soma de todos os elementos
    - 'maior': maior elemento
    - 'menor': menor elemento
    - 'media': média de todos os elementos
    Parâmetro:
      - matriz (list): matriz para análise
    Retorno:
      - dict: dicionário com estatísticas
    """
    pass


def ex27(texto):
    """
    Exercício 27:
    Crie uma função que analise um texto e retorne um dicionário com:
    - 'caracteres': total de caracteres
    - 'palavras': total de palavras
    - 'linhas': total de linhas
    - 'vogais': total de vogais
    Parâmetro:
      - texto (str): texto para análise
    Retorno:
      - dict: dicionário com estatísticas do texto
    """
    pass


def ex28(lista_numeros):
    """
    Exercício 28:
    Crie uma função que organize uma lista de números em uma matriz 
    onde cada linha tenha um tamanho específico.
    Parâmetros:
      - lista_numeros (list): lista de números
      - colunas (int): número de colunas da matriz
    Retorno:
      - list: matriz organizada
    """
    pass


def ex29(matriz_vendas, produtos):
    """
    Exercício 29:
    Crie uma função que processe dados de vendas.
    A matriz_vendas contém vendas por dia e produto.
    A lista produtos contém os nomes dos produtos.
    Retorne o produto com maior total de vendas.
    Parâmetros:
      - matriz_vendas (list): matriz com vendas [dia][produto]
      - produtos (list): lista com nomes dos produtos
    Retorno:
      - str: nome do produto com maior total de vendas
    """
    pass


def ex30():
    """
    Exercício 30:
    Crie um menu interativo que permita:
    1. Criar matriz
    2. Exibir matriz
    3. Calcular soma das diagonais
    4. Encontrar maior e menor valor
    5. Transpor matriz
    6. Sair

    Implemente todas as funcionalidades usando as funções criadas anteriormente.
    """
    pass
