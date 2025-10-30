
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


if nome and idade != " " :
    print(f'seu nome é {nome} e sua idade é {idade} anos ')
else: 
    print("Você deixou campos vazios")


#nome ao contrario 
nome_invertido = nome[::-1]


print(f'Seu nome ao contrario é {nome_invertido}')
# se existe letra no nome 
letra = " "

if letra in nome:
    print('o nome contem espaços')
else:
    print('o nome não contem espaços')

#  quantidade de letras no nome
qtde_letras= len(nome)
print(f'Seu nome tem {qtde_letras} letras')

# primeira letra do nome
print(f'a prmeira letra é {nome[0]}')
# ultima letra do nome
print(f'a ultima letra é {nome[-1]}')

# nome em maiusculo
print("seu nome em maiusculo é ", nome.upper())
# nome em minusculo
print("seu nome em minusculo é ", nome.lower())