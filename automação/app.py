import customtkinter as ctk

# Configuração da aparência
ctk.set_appearance_mode('dark')

# Criação da janela principal
app = ctk.CTk()
app.title('Calculador de proporcional')
app.geometry('400x400')

# Criação dos campos
# label
label_vencimento1 = ctk.CTkLabel(app,text='Data de vencimento antigo.')
label_vencimento1.pack(pady=10)

# Entry
campo_usuario1 = ctk.CTkEntry(app,placeholder_text='Digite o vencimento antigo')
campo_usuario1.pack(pady=10)

# label
label_vencimento2 = ctk.CTkLabel(app,text='Nova data de vencimento.')
label_vencimento2.pack(pady=10)

# Botão
ctk.CTkButton(app, text='Calcular',command=calcular_proporcional)


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

# Iniciar a aplicação
app.mainloop()