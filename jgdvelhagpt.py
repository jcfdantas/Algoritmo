import os
import random

JogarNovamente="s"
jogadas=0
quemJoga=1 #cada jogar joga em um número entre 1 e 2
maxjogadas=9
v="n"
velha=[[" ", " ", " " ] , [" ", " ", " " ] , [ " ", " ", " "]  ]
def tela():
    global velha
    global jogadas
    os.system("cls" if os.name == "nt" else "clear")
    print("    0      1     2")
    print("0:  " , velha[0][0], " | ", velha[0][1], " | ", velha[0][2])
    print("   ------------------")
    print("1:  " , velha[1][0], " | ", velha[1][1], " | ", velha[1][2])
    print("   ------------------")
    print("2:  " , velha[2][0], " | ", velha[2][1], " | ", velha[2][2])
    print("Números de jogadas: ", str(jogadas))
def j1j():
    global jogadas
    global quemJoga
    global v
    global maxjogadas
    if quemJoga==1 and jogadas<maxjogadas:
        l=int(input("Digite a linha: "))
        c=int(input("Digite a coluna: "))
        while velha[l][c]!= " ":
            l=int(input("Digite a linha: "))
            c=int(input("Digite a coluna: "))
        try:
            velha[l][c]="X"
            quemJoga=2
            jogadas+=1
            tela()
        except:
            print("Linha ou Coluna inválida")
            #vit="n"
def j2j():
    global jogadas
    global quemJoga
    global v
    global maxjogadas
    if quemJoga==2 and jogadas<maxjogadas:
        l=int(input("Digite a linha: "))
        c=int(input("Digite a coluna: "))
        while velha[l][c]!=" ":
            l=int(input("Digite a linha: "))
            c=int(input("Digite a coluna: "))
        try:
            velha[l][c]="O"
            quemJoga=1
            jogadas+=1
            tela()
        except:
            print("Linha ou Coluna inválida")
            #vit="n"
def vv():
    global velha
    global vitorias
    simbolos=["X", "O"]
    for s in simbolos:
        vitorias="n"
        #Verificar linhas
        il=ic=0
        while il<3:
            soma = 0
            ic=0
            while ic<3:
                if (velha[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitorias=s
            break
        il+=1 
            #il+=1
        if(vitorias!="n"):
            break
        #Verificar colunas
        il=ic=0
        while ic<3:
            soma = 0
            il=0
            while il<3:
                if (velha[il][ic]==s):
                    soma+=1
                il+=1
            if(soma==3):
                vitorias=s
            break
        ic+=1
        if(vitorias!="n"):
            break
        #Verificar diagonal 1
        soma=0
        idiag=0
        while idiag<3:
            if (velha[idiag][idiag]==s):
                    soma+=1
            idiag+=1
        if(soma==3):
            vitorias=s
            break
        soma=0
        idiagl=0
        idiagc=2
        while idiag>=0:
            if (velha[idiagl][idiagc]==s):
                    soma+=1
            idiagl+=1
            idiagl-=1
        if(soma==3):
            vitorias=s
            break
    return vitorias
def redefinir():
    global velha
    global v
    global jogadas
    global quemJoga
    global maxjogadas
    
    velha=[[" ", " ", " " ] , [" ", " ", " " ] , [ " ", " ", " "]  ]
while True:
    tela()
    j1j()
    j2j()
    v = vv()
    if(v!="n")or(jogadas>=maxjogadas):
        break
