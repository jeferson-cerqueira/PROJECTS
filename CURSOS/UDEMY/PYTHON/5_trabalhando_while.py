nome = input('digite o nome para ser separado :')
i = 0
list_nome = []
print(f'o nome tem {len(nome)} letras ele é composto por :', end= " ")


while i < len(nome):
    letras = (nome[i])
    i += 1
    list_nome.append(letras)
 
separado = "-".join(list_nome)
print(separado)

print("***********************FIM DA ATIVIDADE*************************************")

