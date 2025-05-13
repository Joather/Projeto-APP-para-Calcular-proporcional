valor_plano = float(input("Digite o valor atual do plano: "))
dias_acrescentados = int(input("Digite os dias acrescentados no plano: "))
diaria_plano = valor_plano / 30
proporcional = diaria_plano * dias_acrescentados
valor_total = proporcional + valor_plano
print(valor_total)