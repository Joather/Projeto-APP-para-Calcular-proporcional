import customtkinter as ctk
from tkinter import messagebox

# Função para o calculo
def calcularProporcional():
    try:
        planoAtual = float(entryValorPlanoAtual.get().replace(',', '.'))
        planoNovo = float(entryValorPlanoNovo.get().replace(',', '.'))
        diaDoVencimento = int(entryDiaVencimento.get())
        diaAlteracao = int(entryDiaAlteracao.get())

        if diaAlteracao > diaDoVencimento:
            diasPlanoAtual = diaAlteracao - diaDoVencimento
            diasPlanoNovo = (diaDoVencimento - diaAlteracao) + 30
        else:
            diasPlanoAtual = (diaAlteracao - diaDoVencimento) + 30
            diasPlanoNovo = diaDoVencimento - diaAlteracao

        proporcionalPlanoAtual = (planoAtual / 30) * diasPlanoAtual
        proporcionalPlanoNovo = (planoNovo / 30) * diasPlanoNovo
        valorTotal = proporcionalPlanoAtual + proporcionalPlanoNovo


        # Mostrar resultado
        resultado.configure(text=f"• Proporcional do plano atual: R${proporcionalPlanoAtual:.2f} "
        f"({diasPlanoAtual} dias do plano antigo)\n"
        f"• Proporcional do novo plano: R${proporcionalPlanoNovo:.2f} "
        f"({diasPlanoNovo} dias do novo plano)")

        texto = (
            f"Proporcional do plano atual: R${proporcionalPlanoAtual:.2f}\n"
            f"Referente a {diasPlanoAtual} utilizados do plano antigo\n\n"
            f"Proporcional do novo plano: R${proporcionalPlanoNovo:.2f}\n"
            f"Referente a {diasPlanoNovo}, utilizados do plano novo\n\n"
            f"VALOR TOTAL: R${valorTotal:.2f}"
        )
        frase_final.configure(text=texto)
        global texto_pronto
        texto_pronto = texto # Guarda para o botão copiar
    except ValueError:
        messagebox.showerror(("Erro"))

def copiar_texto():
    try:
        app.clipboard_clear()
        app.clipboard_append(texto_pronto)
        messagebox.showinfo("Copiado", "Texto copiado para a área de transferência!")
    except:
        messagebox.showerror("Erro", "Nenhum texto para copiar ainda.")

# Configurando aparência
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

# Configurando a janela
app = ctk.CTk()
app.title("Calculador de Alteração de plano")
app.geometry('600x600')

# Criação dos campos
# Label e entrada de dados - ValorPlanoAtual
labelValorPlanoAtual = ctk.CTkLabel(app, text="Digite o valor do plano atual")
labelValorPlanoAtual.pack(pady=(20, 0))
entryValorPlanoAtual = ctk.CTkEntry(app, placeholder_text="Digite o valor do plano atual")
entryValorPlanoAtual.pack(pady='0')

# Label e entrada de dados - ValorPlanoNovo
labelValorPlanoNovo = ctk.CTkLabel(app, text="Digite o valor do novo plano")
labelValorPlanoNovo.pack(pady=(20, 0))
entryValorPlanoNovo = ctk.CTkEntry(app, placeholder_text="Digite o valor do novo plano")
entryValorPlanoNovo.pack(pady ='0')

# Label e entrada de dados - DiaDoVencimento
labelDiaVencimento = ctk.CTkLabel(app, text="Digite o dia do vencimento.")
labelDiaVencimento.pack(pady=(20, 0))
entryDiaVencimento = ctk.CTkEntry(app, placeholder_text="Digite o dia do vencimento.")
entryDiaVencimento.pack(pady='0')

# Label e entrada de dados - DiaDaAlteração
labelDiaAlteracao = ctk.CTkLabel(app, text="Digite o dia da alteração")
labelDiaAlteracao.pack(pady=(10, 0))
entryDiaAlteracao = ctk.CTkEntry(app, placeholder_text="Digite o dia da alteração")
entryDiaAlteracao.pack(pady='0')

# Botão para calcular
botao = ctk.CTkButton(app, text="Calcular", command=calcularProporcional)
botao.pack(pady='20')

# Mostrar o resultado
resultado = ctk.CTkLabel(app, text='', font=('Arial', 14))
resultado.pack(pady='10')

# Label do texto final
frase_final = ctk.CTkLabel(app, text='', font=('Arial', 12), wraplength=380, justify='left')
frase_final.pack(pady=10)
frase_final.pack(pady=10)

# Botão de copiar
botao_copiar = ctk.CTkButton(app, text="Copiar", command=copiar_texto)
botao_copiar.pack(pady=10)

# Iniciar o loop
app.mainloop()