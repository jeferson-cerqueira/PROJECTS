print ("********** ATIVIDADE 1 *************")

try:
    numero_int = int(input("digite um numero : "))

    if numero_int %2 == 0:
     print(f'o numero {numero_int} é um numero par')
    else:
        print(f'o numero {numero_int} é impar')
    
except:
    print("o valor digitado não é um numero inteiro")

#########################################################################


print("********** ATIVIDADE 2 *************")

try:
    hora_atual = int(input("digite apenas a hora atual : "))

    if hora_atual <=11 :
        print("BOM DIA !!!")
    elif hora_atual >11 and hora_atual <18:
        print("BOA TARDE !!!")
    elif hora_atual >=18 and hora_atual <= 23:
        print("BOA NOITE !!! ")
    else:
        print(f'A hora {hora_atual} é invalida ')
        print("Por gentileza digite um valor entre 0h e 23h")

except:
    print("o valor digitado não é um numero valido")


#########################################################################


print("********** ATIVIDADE 3 *************")

nome_usuario = input("digite seu nome : ")
tamanho_nome = len(nome_usuario)

if tamanho_nome <=4:
    print(f'O {nome_usuario} é curto')

elif tamanho_nome >4 and tamanho_nome <=7:
    print(f'O {nome_usuario} é normal')

else:
    print(f'O {nome_usuario} é longo ')


