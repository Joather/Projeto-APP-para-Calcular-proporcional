def calcular_fatura():
    # Solicita os dados ao usuário
    valor_antigo = float(input("Digite o valor do plano antigo (R$): "))
    valor_novo = float(input("Digite o valor do novo plano (R$): "))
    vencimento = int(input("Digite o dia do vencimento (1 a 30): "))
    alteracao = int(input("Digite o dia da alteração do plano (1 a 30): "))

    # Calcula o início do ciclo (30 dias antes do vencimento)
    inicio_ciclo = vencimento - 30
    if inicio_ciclo <= 0:
        inicio_ciclo += 30  # ajusta se ficar negativo ou zero

    # Dias com plano antigo
    if alteracao >= inicio_ciclo:
        dias_antigo = alteracao - inicio_ciclo
    else:
        dias_antigo = (30 - inicio_ciclo) + alteracao

    # Dias com plano novo
    dias_novo = 30 - dias_antigo

    # Cálculo proporcional
    valor_parcial_antigo = (valor_antigo / 30) * dias_antigo
    valor_parcial_novo = (valor_novo / 30) * dias_novo
    total = valor_parcial_antigo + valor_parcial_novo

    # Exibe o resultado
    print(f"\nResumo:")
    print(f"Dias com plano antigo: {dias_antigo}")
    print(f"Dias com plano novo: {dias_novo}")
    print(f"Valor proporcional do plano antigo: R${valor_parcial_antigo:.2f}")
    print(f"Valor proporcional do plano novo: R${valor_parcial_novo:.2f}")
    print(f"Valor total da fatura: R${total:.2f}")

# Executa o programa
calcular_fatura()