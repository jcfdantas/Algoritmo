"""
=============================
LISTA DE EXERCÍCIOS – FUNÇÕES E PROCEDIMENTOS
=============================
Aluno: 
"""

# =============================
# 1. INTRODUÇÃO A FUNÇÕES E PROCEDIMENTOS
# =============================


def ex1():
    print("Bem-vindo ao mundo das funções!")


def ex2():
    print("Olá mundo!")


def ex3():
    nome = str(input("Digite o nome do aluno: "))
    print(f"O nome do aluno é {nome}")



def ex4():
   print(10)


def ex5():
    print("Essa é a linha 1\n",
          "Essa é a linha 2\n",
          "Essa é a inha 3\n")


# =============================
# 2. INTRODUÇÃO AOS PARÂMETROS DE FUNÇÕES
# =============================

def ex6():
  n1 = int(input("Digite o primeiro número: "))
  n2 = int(input("Digite o segundo número"))
  soma = n1 + n2
  print(f"A soma é: {n1} + {n2} = {soma}")

   

def ex7():
 nome= input("Digite seu nome: ")
 print(f"Olá, {nome}! Seja bem-vindo!")


def ex8():
    base =int(input("Digite a base do retângulo: "))
    altura = int(input("Digite a altura do retângulo: "))
    area = base * altura
    print(f"A area do seu retangulo é {area}")


# =============================
# 3. FUNÇÕES UTILIZANDO ALGORITMOS DO 1º SEMESTRE
# =============================

def ex9():
   num = int(input("Digite um número para ser verificado se impar ou par: "))
   if num%2 == 0:
       print("O número é par")
   else:
       print("O número é ímpar")


def ex10():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    media = (n1 + n2 + n3)/ 3
    print(f"A média dos números é {media}")


def ex11():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    if n1 > n2 and n1 >n3:
        print(f"O maior número é {n1}")
    elif n2> n1 and n2 >n3:
        print(f"O maior número é {n2}")
    else:
        print(f"O maior número é {n3}")


    


def ex12():
    graus = int(input('Digite quantos graus para ser convertido em Fahrenheit: '))
    F = graus * 9/5 + 32
    print(F)




def ex13():
    t = int(input("Digite o tamanho da lista: "))
    l = []
    for i in range(t):
        v = int(input(f"Digite o valor para a posição {i+1}:"))
        l.append(v)
    soma = sum(l)
    print(soma)


def ex14():
    t = int(input("Digite o tamanho da lista: "))
    lista = []
    for i in range(t):
        valor = int(input(f"Digite o valor para a posição {i+1}:"))
        lista.append(valor)
    novalista=[]
    for w in range(len(lista)):     
        if lista[w] % 2 == 0:
            novalista.append(lista[w])
    print(novalista)


# =============================
# 4. FUNÇÕES CLÁSSICAS COM ESTRUTURAS DE REPETIÇÃO
# =============================

def ex15(base, expoente):
    """
    Exercício 15:
    Crie uma função que calcule a potência de um número (base^expoente)
    usando estrutura de repetição.
    Parâmetros:
      - base (int ou float): o número base
      - expoente (int): o expoente (deve ser não-negativo)
    Retorno:
      - Resultado da potenciação
    """
    pass


def ex16(numero, digito):
    """
    Exercício 16:
    Crie uma função que conte quantas vezes um dígito específico aparece em um número.
    Use estrutura de repetição para percorrer os dígitos.
    Parâmetros:
      - numero (int): o número para analisar
      - digito (int): o dígito a ser contado (0-9)
    Retorno:
      - int: quantidade de vezes que o dígito aparece
    """
    pass


def ex17():
    """
    Exercício 17:
    Crie uma função que retorne a soma dos dígitos de um número.
    Exemplo: 123 -> 1 + 2 + 3 = 6
    """
    pass


def ex18(numero):
    """
    Exercício 18:
    Crie uma função que calcule o fatorial de um número.
    O fatorial de n (n!) é o produto de todos os números inteiros positivos menores ou iguais a n.
    Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120
    Parâmetro:
      - numero (int): número para calcular o fatorial (deve ser não-negativo)
    Retorno:
      - int: o fatorial do número
    """
    pass


def ex19():
    t = int(input("Digite o tamanho da lista: "))
    lista = []
    for i in range(t):
        valor = int(input(f"Digite o valor para a posição {i+1}:"))
        lista.append(valor)
    novalista = sorted(lista)
    print("Sua lista ordenada é: ", novalista)



def ex20():
    t = int(input("Digite o tamanho da lista: "))
    lista = []
    for i in range(t):
        valor = int(input(f"Digite o valor para a posição {i+1}:"))
        lista.append(valor)
    for i in range(t):
        novalista = lista [:: -1]
    print(f"Sua lista inicial é: {lista}")
    print(f"Essa é a lista com posições invertidas: {novalista}")


#ex1()
#ex2()
#ex3()
#ex4()
#ex5()
#ex6()
#ex7()
#ex8()
#ex9()
#ex10()
#ex11()
#ex12()
#ex13()
#ex14()
#ex16()
#ex17()
#ex18()
#ex19()
#ex20()