import os
import random

JogarNovamente="s"
jogadas=0
quemJoga=1 #cada jogar joga em um número entre 1 e 2
maxjogadas=9
v="n"
velha=[["  ", "  ", "  " ] , ["  ", "  ", "  " ] , [ "  ", "  ", "  "]  ]
def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0       1      2")
    print("0:  " , velha[0][0], " | ", velha[0][1], " | ", velha[0][2])
    print("   ------------------")
    print("1:  " , velha[1][0], " | ", velha[1][1], " | ", velha[1][2])
    print("   ------------------")
    print("2:  " , velha[2][0], " | ", velha[2][1], " | ", velha[2][2])
    print("Números de jogadas: ", str(jogadas))
def j1j():
    global velha
    global jogadas
    global quemJoga
    if quemJoga==1:
        l=int(input("Digite a linha: "))
        c=int(input("Digite a coluna: "))
        while velha[l][c]!= "  ":
            l=int(input("Digite a linha: "))
            c=int(input("Digite a coluna: "))
        try:
            velha[l][c]=("X")
            quemJoga=2
        except:
            print("Linha ou Coluna inválida")
            #vit="n"
def j2j():
    global velha
    global jogadas
    global quemJoga
    if quemJoga==2:
        l=int(input("Digite a linha: "))
        c=int(input("Digite a coluna: "))
        while velha[l][c]!="  ":
            l=int(input("Digite a linha: "))
            c=int(input("Digite a coluna: "))
        try:
            velha[l][c]="O"
            quemJoga=1
        except:
            print("Linha ou Coluna inválida")
            #vit="n"


#while True:
tela()
    #jog1
j1j()
    #jog2
j2j()
    #vit ou der
