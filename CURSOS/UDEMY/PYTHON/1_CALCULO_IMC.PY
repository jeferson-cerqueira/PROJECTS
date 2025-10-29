nome = input("digite seu nome : ")
idade = int(input("digite sua idade : "))
peso = float(input("digite seu peso : "))
altura = float(input("digite sua altura : "))
imc = peso / (altura * altura)
classificação = ""

if imc < 18.5:
    classificação = "Abaixo do peso"
elif imc < 25:
    classificação = "Peso normal"
elif imc < 30:
    classificação = "Sobrepeso"
elif imc < 35:
    classificação = "Obesidade grau 1"
elif imc < 40:
    classificação = "Obesidade grau 2"
else:
    classificação = "Obesidade grau 3"

print(f'Olá, {nome}! Sua idade é {idade} anos, sua altura é {altura}m '
 f'e seu peso é {peso}kg. Portanto, seu IMC é {imc:.2f}. e você está {classificação}')
