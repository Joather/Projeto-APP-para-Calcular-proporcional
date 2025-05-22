import customtkinter as ctk
from tkinter import messagebox

# Configuração da aparência
ctk.set_appearance_mode('dark') # Modo escuro
ctk.set_default_color_theme('green') # Cor dos botões e destaques

app = ctk.CTk()
app.title("Calculadora de Proporcional")
app.geometry("620x600")

# Configurando as abas
tabview = ctk.CTkTabview(app, width=600)
tabview.pack(pady=20)
tabview.add("Alteração de Plano")
tabview.add("Alteração de Vencimento")


# --- ABA 1: Alteração de Plano
# Função para o calculo da mudança de plano
def calcularProporcionalPlano():
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

        texto = (
            f"Proporcional do plano atual: R${proporcionalPlanoAtual:.2f}\n"
            f"Referente a {diasPlanoAtual} utilizados do plano antigo\n\n"
            f"Proporcional do novo plano: R${proporcionalPlanoNovo:.2f}\n"
            f"Referente a {diasPlanoNovo}, utilizados do plano novo\n\n"
            f"VALOR TOTAL: R${valorTotal:.2f}"
        )
        label_resultado1.configure(text=texto)
        global texto_pronto
        texto_pronto = texto # Guarda para o botão copiar
    except ValueError:
        messagebox.showerror(("Erro"))

# --- ABA 1: Layout ---
frame1 = tabview.tab("Alteração de Plano")
# Label e entrada de dados - ValorPlanoAtual
labelValorPlanoAtual = ctk.CTkLabel(frame1, text="Digite o valor do plano atual")
labelValorPlanoAtual.pack(pady=(20, 0))
entryValorPlanoAtual = ctk.CTkEntry(frame1, placeholder_text="Digite o valor do plano atual")
entryValorPlanoAtual.pack(pady='0')
# Label e entrada de dados - ValorPlanoNovo
labelValorPlanoNovo = ctk.CTkLabel(frame1, text="Digite o valor do novo plano")
labelValorPlanoNovo.pack(pady=(20, 0))
entryValorPlanoNovo = ctk.CTkEntry(frame1, placeholder_text="Digite o valor do novo plano")
entryValorPlanoNovo.pack(pady ='0')
# Label e entrada de dados - DiaDoVencimento
labelDiaVencimento = ctk.CTkLabel(frame1, text="Digite o dia do vencimento.")
labelDiaVencimento.pack(pady=(20, 0))
entryDiaVencimento = ctk.CTkEntry(frame1, placeholder_text="Digite o dia do vencimento.")
entryDiaVencimento.pack(pady='0')
# Label e entrada de dados - DiaDaAlteração
labelDiaAlteracao = ctk.CTkLabel(frame1, text="Digite o dia da alteração")
labelDiaAlteracao.pack(pady=(10, 0))
entryDiaAlteracao = ctk.CTkEntry(frame1, placeholder_text="Digite o dia da alteração")
entryDiaAlteracao.pack(pady='0')
# Botão para calcular
botao_calcular_plano = ctk.CTkButton(frame1, text="Calcular", command=calcularProporcionalPlano)
botao_calcular_plano.pack(pady=10 )
# Mostrar o resultado
label_resultado1 = ctk.CTkLabel(frame1, text='', font=('Arial', 14))
label_resultado1.pack(pady='10')

# --- ABA 2: Mudança de Vencimento ---
# Função que será executada ao clicar no botão
def calcularProporcionalVencimento():
    try:
        # Captura os dados digitados
        vencimento_atual = int(campo_vencimento1.get())
        vencimento_novo = int(campo_vencimento2.get())
        valor_plano = float(campo_valor.get().replace(',', '.'))

        # Lógica do cálculo
        if(vencimento_atual < vencimento_novo):
            dias_proporcionais = vencimento_novo - vencimento_atual
        else:
            dias_proporcionais = (30 - vencimento_atual) + vencimento_novo

        diaria_plano = valor_plano / 30
        proporcional = diaria_plano * dias_proporcionais
        valor_total = proporcional + valor_plano

        # Exibir os resultados
        label_resultado2.configure(text=f"Proporcional: R$ {proporcional:.2f}\nValor total: R$ {valor_total:.2f}")
        texto = (
            f"Alteração de Vencimento\n\n"
            f"Vencimento antigo: dia {vencimento_atual}\n"
            f"Novo vencimento: dia {vencimento_novo}\n"
            f"Dias proporcionais: {dias_proporcionais}\n"
            f"Valor proporcional: R${proporcional:.2f}\n"
            f"Valor total: R${valor_total:.2f}"
        )
        label_resultado2.configure(text=texto)
        global texto_pronto
        texto_pronto = texto # guarda para o botão "Copiar"
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos.")

# --- ABA 2: Layout ---
frame2 = tabview.tab("Alteração de Vencimento")
# label e campo: vencimento atual
label_vencimento1 = ctk.CTkLabel(frame2,text='Data de vencimento atual.')
label_vencimento1.pack(pady=10)
campo_vencimento1 = ctk.CTkEntry(frame2,placeholder_text='Digite o vencimento atual')
campo_vencimento1.pack(pady=10)
# Label e campo: novo vencimento
label_vencimento2 = ctk.CTkLabel(frame2,text='Nova data de vencimento:')
label_vencimento2.pack(pady=10)
campo_vencimento2 = ctk.CTkEntry(frame2, placeholder_text='Digite o novo vencimento (1-30)')
campo_vencimento2.pack(pady=5)
# Label e campo: valor do plano
label_valor = ctk.CTkLabel(frame2, text='Valor atual do plano')
label_valor.pack(pady=5)
campo_valor = ctk.CTkEntry(frame2, placeholder_text='Digite o valor (ex: 100.00)')
campo_valor.pack(pady=5)
# Botão de calcular
botao_calcular_vencimento  = ctk.CTkButton(frame2, text='Calcular',command=calcularProporcionalVencimento)
botao_calcular_vencimento.pack(pady=15)
# Label do texto final
label_resultado2 = ctk.CTkLabel(frame2, text='', font=('Arial', 12), wraplength=380, justify='left')
label_resultado2.pack(pady=10)

def copiar_texto():
    try:
        app.clipboard_clear()
        app.clipboard_append(texto_pronto)
        messagebox.showinfo("Copiado", "Texto copiado para a área de transferência!")
    except:
        messagebox.showerror("Erro", "Nenhum texto para copiar ainda.")
# Botão de copiar
botao_copiar = ctk.CTkButton(app, text="Copiar Texto", command=copiar_texto)
botao_copiar.pack(pady=10)

# Rodapé com copyright
label_copyright = ctk.CTkLabel(
    app,
    text="© 2025 Joaquim 'Joather' Ferreira, Aquiles Alves, Vitor 'Stew' Glennon. Todos os direitos reservados.",
    font=("Arial", 10),
    text_color="gray"
)
label_copyright.pack(side="bottom", pady=5)
# Iniciar o loop
app.mainloop()