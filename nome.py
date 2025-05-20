n=input("Digite uma palavra: ")
n1=input("Digite outra palavra: ")
a=input("Você deseja continuar: (sim/não)")
a.lower()
if a == "sim":
    n2=input("Digite mais uma palavra: ")
elif a =="não":
    n2=("Não escolhida")
a1=int(input("Okay, você deseja as palavras em ordem alfabética(1) ou por número de letras(2): "))
if a1==1:
    print(sorted([n,n1,n2]))
elif a1==2:
   if len(n) <= len(n1) and len(n) <= len(n2):
        print(n)
   if len(n1) <= len(n2):
        print(n1)
        print(n2)
   else:
        print(n2)
        print(n1)
elif len(n1) <= len(n) and len(n1) <= len(n2):
    print(n1)
    if len(n) <= len(n2):
        print(n)
        print(n2)
    else:
        print(n2)
        print(n)
else:
    print(n2)
    if len(n) <= len(n1):
        print(n)
        print(n1)
    else:
        print(n1)
        print(n)