salario = float(input("Digite o salário atual: "))
tempo = float(input("Digite o tempo de empresa (em anos): "))

if tempo < 2:
    novo_salario = salario * 1.05
elif tempo >= 2 and tempo <= 5:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.15

print("Novo salário:", novo_salario)