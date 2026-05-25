temperatura = float(input("Digite a temperatura da caldeira (°C): "))

if temperatura < 100:
    print("Temperatura Baixa")
elif temperatura >= 100 and temperatura <= 150:
    print("Temperatura Normal")
else:
    print("Alerta: Temperatura Alta")