
import os
import random
    
palavras_secretas = [
    "abacaxi","bicicleta","computador","elefante","girassol","hipopotamo","janela",
    "lanterna","morango","navio","oculos","paralelepipedo","queijo","rinoceronte",
    "sapato","teclado","universo","violao","xadrez","zebra"
]
palavra_secreta = random.choice(palavras_secretas)
letras_acertadas = ""
tentativas = 0
numeros = "0123456789"
letra_ja_digitada = ""


print("Acerte a palavra secreta!")
print("A palavra secreta contem", len(palavra_secreta), "letras, boa sorte!")

while True:
    letra_digitada = input("Digite uma letra: ")
    letra_digitada = letra_digitada.lower()
    tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue
    if letra_digitada.isdigit():
        print("Digite apenas letras")
        continue
    if letra_digitada in letra_ja_digitada:
        print("Essa letra ja foi digitada")
        continue
    letra_ja_digitada += letra_digitada

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print(palavra_formada)
    
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('ACERTOU!!!! ')
        print("a palavra é ", palavra_secreta)
        print("tentativas: ", tentativas)
        break
