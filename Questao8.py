peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
else:
    print("Sobrepeso")