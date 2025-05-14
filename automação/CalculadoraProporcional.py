import customtkinter as ctk
vencimento_atual = int(input('Digite o vencimento atual: '))
vencimento_novo = int(input('Digite o novo vencimento: '))
valor_plano = float(input('Digite o valor atual do plano: '))

if(vencimento_atual < vencimento_novo):
    dias_proporcionais = vencimento_novo - vencimento_atual
else:
    dias_proporcionais = (30 - vencimento_atual) + vencimento_novo

diaria_plano = valor_plano / 30
proporcional = diaria_plano * dias_proporcionais
valor_total = proporcional + valor_plano
print(valor_total)