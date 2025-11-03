numero_1 = int(input("digite um numero : "))
numero_2 = int(input("digite outro numero : "))

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