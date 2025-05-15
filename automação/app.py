import customtkinter as ctk
from tkinter import messagebox

# Função que será executada ao clicar no botão
def calcular_proporcional():
    try:
        # Captura os dados digitados
        vencimento_atual = int(campo_vencimento1.get())
        vencimento_novo = int(campo_vencimento2.get())
        valor_plano = float(campo_valor.get())

        # Lógica do cálculo
        if(vencimento_atual < vencimento_novo):
            dias_proporcionais = vencimento_novo - vencimento_atual
        else:
            dias_proporcionais = (30 - vencimento_atual) + vencimento_novo

        diaria_plano = valor_plano / 30
        proporcional = diaria_plano * dias_proporcionais
        valor_total = proporcional + valor_plano

        # Exibir os resultados
        resultado.configure(text=f"Proporcional: R$ {proporcional:.2f}\nValor total: R$ {valor_total:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos.")

# Configuração da aparência
ctk.set_appearance_mode('dark') # Modo escuro
ctk.set_default_color_theme('green') # Cor dos botões e destaques

# Criação da janela principal
app = ctk.CTk()
app.title('Calculador de proporcional')
app.geometry('400x400')

# Criação dos campos
# label e campo: vencimento atual
label_vencimento1 = ctk.CTkLabel(app,text='Data de vencimento antigo.')
label_vencimento1.pack(pady=10)
campo_vencimento1 = ctk.CTkEntry(app,placeholder_text='Digite o vencimento antigo')
campo_vencimento1.pack(pady=10)

# Label e campo: novo vencimento
label_vencimento2 = ctk.CTkLabel(app,text='Nova data de vencimento:')
label_vencimento2.pack(pady=10)
campo_vencimento2 = ctk.CTkEntry(app, placeholder_text='Digite o novo vencimento (1-30)')
campo_vencimento2.pack(pady=5)

# Label e campo: valor do plano
label_valor = ctk.CTkLabel(app, text='Valor atual do plano')
label_valor.pack(pady=5)
campo_valor = ctk.CTkEntry(app, placeholder_text='Digite o valor (ex: 100.00)')
campo_valor.pack(pady=5)

# Botão de calcular
botao = ctk.CTkButton(app, text='Calcular',command=calcular_proporcional)
botao.pack(pady=15)

# Label de resultado
resultado = ctk.CTkLabel(app, text='', font=('Arial', 14))
resultado.pack(pady=10)

# Iniciar a aplicação
app.mainloop()