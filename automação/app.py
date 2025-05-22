import customtkinter as ctk
from tkinter import messagebox

# Configuração da aparência
ctk.set_appearance_mode('dark') # Modo escuro
ctk.set_default_color_theme('green') # Cor dos botões e destaques

# Criação da janela principal
app = ctk.CTk()
app.title('Calculador de proporcional')
app.geometry('600x600')

# Configurando as abas
tabview = ctk.CTkTabview(app, width=600)
tabview.pack(pady=20)
tabview.add("Alteração de Plano")
tabview.add("Alteração de Vencimento")


# --- ABA 1: Alteração de Plano
# Função que será executada ao clicar no botão
def calcular_proporcional():
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
        resultado.configure(text=f"Proporcional: R$ {proporcional:.2f}\nValor total: R$ {valor_total:.2f}")
        texto = (
            f"Cliente solicita alteração na data de vencimento, indo de dia {vencimento_atual}, "
            f"para o dia {vencimento_novo}, proporcional de {dias_proporcionais} dias utilizados, "
            f"no valor de R${proporcional:.2f}, valor total de R${valor_total:.2f}."
        )
        frase_final.configure(text=texto)
        global texto_pronto
        texto_pronto = texto # guarda para o botão "Copiar"
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos.")

def copiar_texto():
    try:
        app.clipboard_clear()
        app.clipboard_append(texto_pronto)
        messagebox.showinfo("Copiado", "Texto copiado para a área de transferência!")
    except:
        messagebox.showerror("Erro", "Nenhum texto para copiar ainda.")

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

# Label do texto final
frase_final = ctk.CTkLabel(app, text='', font=('Arial', 12), wraplength=380, justify='left')
frase_final.pack(pady=10)

# Botão de copiar
botao_copiar = ctk.CTkButton(app, text='Copiar texto', command=copiar_texto,)
botao_copiar.pack(pady=10)

# Iniciar a aplicação
app.mainloop()