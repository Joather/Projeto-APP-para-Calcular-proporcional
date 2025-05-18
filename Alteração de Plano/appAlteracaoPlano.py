planoAtual = float(input("Digite o valor do plano atual: "))
planoNovo = float(input("Digite o valor do novo plano: "))
diaDoVencimento = int(input("Digite o dia de vencimento: "))
diaAlteracao = int(input("Digite o dia em que foi alterado (Data de hoje, caso seja hoje): "))

if diaAlteracao > diaDoVencimento:
    diasPlanoAtual = diaAlteracao - diaDoVencimento
    diasPlanoNovo = (diaDoVencimento - diaAlteracao) + 30
else:
    diasPlanoAtual = (diaAlteracao - diaDoVencimento) + 30
    diasPlanoNovo = diaDoVencimento - diaAlteracao

proporcionalPlanoAtual = (planoAtual / 30) * diasPlanoAtual
proporcionalPlanoNovo = (planoNovo / 30) * diasPlanoNovo
valorTotal = proporcionalPlanoAtual + proporcionalPlanoNovo

print(f"Dias utilizado plano atual: {diasPlanoAtual}, totalizando: R${proporcionalPlanoAtual}")
print(f"Dias utilizado do plano novo: {diasPlanoNovo}, totalizando: R${proporcionalPlanoNovo}")
print(valorTotal)