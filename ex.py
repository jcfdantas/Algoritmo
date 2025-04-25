def calculadora ():
    print("calculadora simples")
    print("1, soma")
    print("2, subtração")
    print("3, Multiplicação")
    print("4, Divisão")   
#Input da operação
    
    try: 
        opçao = int(input("Escolha a operação(1 - 4): "))
        if opçao < 1 or opçao > 4 :
            print("operação inválida! Escolha entre 1 e 4 ")
            return
    except ValueError:
        print("entrada inválida, digite um numero:")
        return
    
    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float (input("Digite o segundo numero: "))
    except ValueError:
        print("entrada inválida! Digite apenas números.")
        return
    
    #operação usando match case
    match opçao:
        case 1:
            resultado = num1 + num2
            print(f"resultado: {num1} + {num2} = {resultado}")
  
        case 2:
            resultado = num1 - num2
            print (f"resultado: {num1} - {num2} = {resultado}")
        case 3: 
            resultado = num1 * num2
            print ( f"resultado: {num1} * {num2} = {resultado} ")
        case 4:
            if num2 == 0:
                print ("não é possivel dividir por 0")
                return
            resultado = num1 / num2
            print ( f"resultado: {num1} / {num2} = {resultado} ")

        case _:
            print("operação inválida")





#executar a calculadora
            #criar loop usando while



if __name__ == "__main__":
   calculadora()