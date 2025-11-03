

print("################ PROJETO CALCULADORA ############################")
try:
    while True:
        deseja_iniciar = input("deseja fazer conta [S] sim [N] não")
        deseja_iniciar = deseja_iniciar.upper()
        
        if deseja_iniciar == "S":

            numero_1 = int(input("digite um numero : "))
            numero_2 = int(input("digite outro numero : "))
            print("os operadores validos são [+,-,*,/]")
            digite_operadores = input("digite um operador : ")

            if digite_operadores == "+": 
                print(f'a soma é : {numero_1 + numero_2}')
            elif digite_operadores == "-": 
                print(f'a subtração é : {numero_1 - numero_2}')
            elif digite_operadores == "*": 
                print(f'a multiplicação é : {numero_1 * numero_2}')
            elif digite_operadores == "/": 
                print(f'a divisão é : {numero_1 / numero_2}')
            else:
                print("operador ou  numero errado")
        
        elif deseja_iniciar == "N":
             print("Ok, quando precisar é só iniciar novamente")
             break
        else:
            print("Não foi possivel idetificar sua resposta vamos recomeçar")
            
            
except:
    print("Não foi possivel identificar os valores dgitados, " \
             "por gentileza digite valores validos")
    
print("obrigado por utilizar a calculadora, volte sempre!!!")