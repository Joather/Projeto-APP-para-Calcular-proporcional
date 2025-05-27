# calculadora_proporcional.py

import customtkinter as ctk
from tkinter import messagebox

# Configuração inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Calculadora de Proporcional")
app.geometry("640x650")
app.configure(fg_color="#121212")

# Tabs
tabview = ctk.CTkTabview(app, 
                         fg_color="#121212",
                         width=600)
tabview.pack(pady=20)
tabview.add("Alteracao de Plano")
tabview.add("Alteracao de Vencimento")
tabview.add("Desconto ou Cancelamento")

# Variáveis globais para copiar
texto_cliente_plano = ""
texto_ordem_plano = ""
texto_cliente_vencimento = ""
texto_ordem_vencimento = ""
texto_cliente_desconto = ""
texto_ordem_cancelamento = ""
texto_cliente_dias = ""
texto_ordem_dias = ""

# -----------------------------
# Função: Calcular Alteracao de Plano
# -----------------------------
def calcular_alteracao_plano():
    global texto_cliente_plano, texto_ordem_plano
    try:
        valor_plano_atual = float(entry_valor_plano_atual.get().replace(",", "."))
        valor_plano_novo = float(entry_valor_plano_novo.get().replace(",", "."))
        dia_vencimento = int(entry_dia_vencimento.get())
        dia_alteracao = int(entry_dia_alteracao.get())

        if dia_alteracao > dia_vencimento:
            dias_plano_atual = dia_alteracao - dia_vencimento
            dias_plano_novo = 30 - dias_plano_atual
        else:
            dias_plano_atual = 30 - (dia_vencimento - dia_alteracao)
            dias_plano_novo = 30 - dias_plano_atual

        proporcional_atual = (valor_plano_atual / 30) * dias_plano_atual
        proporcional_novo = (valor_plano_novo / 30) * dias_plano_novo
        valor_total = proporcional_atual + proporcional_novo

        texto_cliente_plano = (
            f"Realizando a troca de plano no *dia {dia_alteracao}*, o valor proporcional a ser pago será:",
            f"\n- *{dias_plano_atual}* dias do plano atual *(R$ {proporcional_atual:.2f})*",
            f"\n- *{dias_plano_novo}* dias do novo plano *(R$ {proporcional_novo:.2f})*",
            f"\nTotal na próxima fatura: *R$ {valor_total:.2f}*, que será para a data *{dia_vencimento}*/XX\n\n"
            "Posso seguir com a alteração?"
        )
        texto_cliente_plano = "".join(texto_cliente_plano)

        texto_ordem_plano = (
            f"Plano atual: R$ {valor_plano_atual:.2f}\n",
            f"Novo plano: R$ {valor_plano_novo:.2f}\n",
            f"Dia da alteracao: {dia_alteracao}\n",
            f"Dias plano atual: {dias_plano_atual} -> R$ {proporcional_atual:.2f}\n",
            f"Dias novo plano: {dias_plano_novo} -> R$ {proporcional_novo:.2f}\n",
            f"Total proporcional: R$ {valor_total:.2f}"
        )
        texto_ordem_plano = "".join(texto_ordem_plano)

        label_texto_cliente1.configure(text=texto_cliente_plano)
        label_texto_ordem1.configure(text=texto_ordem_plano)

    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos.")

# -----------------------------
# Função: Calcular Alteracao de Vencimento
# -----------------------------
def calcular_alteracao_vencimento():
    global texto_cliente_vencimento, texto_ordem_vencimento
    try:
        vencimento_atual = int(entry_vencimento_atual.get())
        vencimento_novo = int(entry_vencimento_novo.get())
        valor_plano = float(entry_valor_plano_vencimento.get().replace(",", "."))

        if vencimento_atual < vencimento_novo:
            dias_proporcionais = vencimento_novo - vencimento_atual
        else:
            dias_proporcionais = (30 - vencimento_atual) + vencimento_novo

        diaria = valor_plano / 30
        valor_proporcional = diaria * dias_proporcionais
        valor_total = valor_plano + valor_proporcional

        texto_cliente_vencimento = (
            f"O Sr(a) solicitou a mudança do vencimento do dia *{vencimento_atual}* para *{vencimento_novo}*.\n"
            f"Serão cobrados *{dias_proporcionais}* dias proporcionais no valor de *R${valor_proporcional:.2f}*,\n"
            f"Totalizando *R${valor_total:.2f}* na próxima fatura, para o dia *{vencimento_novo}/XX.*\n\n"
            "Posso seguir com a alteração?"
        )


        texto_ordem_vencimento = (
            f"Vencimento Atual: {vencimento_atual}\n"
            f"Novo vencimento: {vencimento_novo}\n"
            f"Dias proporcionais: {dias_proporcionais}\n"
            f"Valor proporcional: R$ {valor_proporcional:.2f}\n"
            f"Total nova fatura: R$ {valor_total:.2f}"
        )

        label_texto_cliente2.configure(text=texto_cliente_vencimento)
        label_texto_ordem2.configure(text=texto_ordem_vencimento)

    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos.")

# -----------------------------
# Função: Calcular Dias: CANCELAMENTO OU DESCONTO
# -----------------------------
def  calcular_dias():
    global texto_cliente_dias, texto_ordem_dias
    try:
        valor_plano = float(entry_valor_plano.get().replace(",", "."))
        dias_proporcional = int(entry_dias_proporcional.get())
        valor_proporcional = (valor_plano / 30) * dias_proporcional

        texto_cliente_dias = (
            f"Conforme verificado, aplicado um desconto de *R${valor_proporcional:.2f}* devido a *{dias_proporcional} dias* sem conexão. Fatura ajustada para *R${valor_plano - valor_proporcional:.2f}*"
        )

        texto_ordem_dias = (
            f"Conforme verificado, será cobrado um valor de *R${valor_proporcional:.2f}* devido a *{dias_proporcional} dias* utilizados de conexão. a fatura ficará no valor de *R${valor_proporcional:.2f}*"
        )

        label_texto_desconto.configure(text=texto_cliente_dias)
        label_texto_cancelamento.configure(text=texto_ordem_dias)

    except ValueError:
        messagebox.showerror("Erro", "Digite valores númericos válidos.")

# -----------------------------
# Funções de Cópia - PLANO
# -----------------------------
def copiar_cliente_plano():
    if texto_cliente_plano:
        app.clipboard_clear()
        app.clipboard_append(texto_cliente_plano)
        messagebox.showinfo("Copiado", "Texto do cliente copiado.")

def copiar_ordem_plano():
    if texto_ordem_plano:
        app.clipboard_clear()
        app.clipboard_append(texto_ordem_plano)
        messagebox.showinfo("Copiado", "Texto da ordem copiado.")

# -----------------------------
# Funções de Cópia - VENCIMENTO
# -----------------------------
def copiar_cliente_vencimento():
    if texto_cliente_vencimento:
        app.clipboard_clear()
        app.clipboard_append(texto_cliente_vencimento)
        messagebox.showinfo("Copiado", "Texto do cliente copiado.")

def copiar_ordem_vencimento():
    if texto_ordem_vencimento:
        app.clipboard_clear()
        app.clipboard_append(texto_ordem_vencimento)
        messagebox.showinfo("Copiado", "Texto da ordem copiado.")

# -----------------------------
# Funções de Cópia - DIAS
# -----------------------------
def copiar_cliente_dias():
    if texto_cliente_dias:
        app.clipboard_clear()
        app.clipboard_append(texto_cliente_dias)
        messagebox.showinfo("Copiado", "Texto do cliente copiado.")

def copiar_ordem_dias():
    if texto_ordem_dias:
        app.clipboard_clear()
        app.clipboard_append(texto_ordem_dias)
        messagebox.showinfo("Copiado", "Texto da ordem copiado.")

# -----------------------------
# Layout - Aba: Alteracao de Plano
# -----------------------------
frame_plano = tabview.tab("Alteracao de Plano")
frame_plano.configure(fg_color="#1E1E1E")

entry_valor_plano_atual = ctk.CTkEntry(frame_plano, placeholder_text="Valor do plano atual")
entry_valor_plano_atual.pack(pady=(15, 5))
entry_valor_plano_novo = ctk.CTkEntry(frame_plano, placeholder_text="Valor do novo plano")
entry_valor_plano_novo.pack(pady=5)
entry_dia_vencimento = ctk.CTkEntry(frame_plano, placeholder_text="Dia do vencimento")
entry_dia_vencimento.pack(pady=5)
entry_dia_alteracao = ctk.CTkEntry(frame_plano, placeholder_text="Dia da alteracao")
entry_dia_alteracao.pack(pady=5)

botao_calcular_plano = ctk.CTkButton(frame_plano, 
                                    text="Calcular", 
                                    command=calcular_alteracao_plano, 
                                    fg_color="#32CD32", hover_color="#94ff94", 
                                    text_color="#333333")
botao_calcular_plano.pack(pady=10)

frame_cliente1 = ctk.CTkFrame(frame_plano, fg_color="#1E1E1E")
frame_cliente1.pack(fill="x", padx=10, pady=5)
ctk.CTkLabel(frame_cliente1, 
            text_color="#e0e0e0",
            text="Texto para o Cliente", 
            font=('Arial', 14, 'bold')).pack()
label_texto_cliente1 = ctk.CTkLabel(frame_cliente1, text="", wraplength=550, justify="left")
label_texto_cliente1.pack(pady=5)
ctk.CTkButton(frame_cliente1, 
            text="Copiar Texto Cliente", 
            fg_color="#32CD32", hover_color="#94ff94", 
            text_color="#333333",
            command=copiar_cliente_plano).pack(pady=5)

frame_ordem1 = ctk.CTkFrame(frame_plano,  fg_color="#1E1E1E")
frame_ordem1.pack(fill="x", padx=10, pady=5)
ctk.CTkLabel(frame_ordem1, text="Texto para Ordem", font=('Arial', 14, 'bold')).pack()
label_texto_ordem1 = ctk.CTkLabel(frame_ordem1, text="", wraplength=550, justify="left")
label_texto_ordem1.pack(pady=5)
ctk.CTkButton(frame_ordem1, 
            fg_color="#32CD32", hover_color="#94ff94", 
            text_color="#333333",
            text="Copiar Texto Ordem", command=copiar_ordem_plano).pack(pady=5)

# -----------------------------
# Layout - Aba: Alteracao de Vencimento
# -----------------------------
frame_vencimento = tabview.tab("Alteracao de Vencimento")
frame_vencimento.configure(fg_color="#1E1E1E")

entry_vencimento_atual = ctk.CTkEntry(frame_vencimento, placeholder_text="Vencimento atual")
entry_vencimento_atual.pack(pady=(15, 5))
entry_vencimento_novo = ctk.CTkEntry(frame_vencimento, placeholder_text="Novo vencimento")
entry_vencimento_novo.pack(pady=5)
entry_valor_plano_vencimento = ctk.CTkEntry(frame_vencimento, placeholder_text="Valor do plano")
entry_valor_plano_vencimento.pack(pady=5)

botao_calcular_vencimento = ctk.CTkButton(frame_vencimento, 
                                        fg_color="#32CD32", hover_color="#94ff94", 
                                        text_color="#333333",                                     
                                        text="Calcular", command=calcular_alteracao_vencimento)
botao_calcular_vencimento.pack(pady=10)

frame_cliente2 = ctk.CTkFrame(frame_vencimento,  fg_color="#1E1E1E")
frame_cliente2.pack(fill="x", padx=10, pady=5)

ctk.CTkLabel(frame_cliente2, text="Texto para o Cliente", font=('Arial', 14, 'bold')).pack()
label_texto_cliente2 = ctk.CTkLabel(frame_cliente2, text="", wraplength=550, justify="left")
label_texto_cliente2.pack(pady=5)
ctk.CTkButton(frame_cliente2, 
            fg_color="#32CD32", hover_color="#94ff94", 
            text_color="#333333",
            text="Copiar Texto Cliente", command=copiar_cliente_vencimento).pack(pady=5)

frame_ordem2 = ctk.CTkFrame(frame_vencimento,  fg_color="#1E1E1E")
frame_ordem2.pack(fill="x", padx=10, pady=5)

ctk.CTkLabel(frame_ordem2, text="Texto para o Ordem", font=('Arial', 14, 'bold')).pack()
label_texto_ordem2 = ctk.CTkLabel(frame_ordem2, text="", wraplength=550, justify="left")
label_texto_ordem2.pack(pady=5)
ctk.CTkButton(frame_ordem2, 
            fg_color="#32CD32", hover_color="#94ff94", 
            text_color="#333333",
            text="Copiar Texto Ordem", command=copiar_ordem_vencimento).pack(pady=5)

# -----------------------------
# Layout - Aba: Proporcional de Dias
# -----------------------------
frame_dias = tabview.tab("Desconto ou Cancelamento")
frame_dias.configure(fg_color="#1E1E1E")

label_valor_plano = ctk.CTkLabel(frame_dias, text="Digite o valor do plano")
label_valor_plano.pack(pady=0)
entry_valor_plano = ctk.CTkEntry(frame_dias, placeholder_text="Valor do Plano")
entry_valor_plano.pack(pady=(0, 20))
label_dias_proporcional = ctk.CTkLabel(frame_dias, text="Digite os dias para o calculo de proporcional")
label_dias_proporcional.pack(pady=0)
entry_dias_proporcional = ctk.CTkEntry(frame_dias, placeholder_text="Digite os dias para o calculo")
entry_dias_proporcional.pack(pady=(0, 20))

botao_calcular_proporcional = ctk.CTkButton(frame_dias, 
                                            fg_color="#32CD32", hover_color="#94ff94", 
                                            text_color="#333333",
                                            text="Calcular", command=calcular_dias)
botao_calcular_proporcional.pack(pady=10)

frame_desconto = ctk.CTkFrame(frame_dias,  fg_color="#1E1E1E")
frame_desconto.pack(fill="x", padx=10, pady=5)
ctk.CTkLabel(frame_desconto, text="Texto para Descontos", font=('Arial', 14, 'bold')).pack()
label_texto_desconto = ctk.CTkLabel(frame_desconto, text="", wraplength=550, justify="left")
label_texto_desconto.pack(pady=5)
ctk.CTkButton(frame_desconto, 
            fg_color="#32CD32", hover_color="#94ff94", 
            text_color="#333333",
            text="Texto para Desconto", command=copiar_cliente_dias).pack(pady=5)

frame_cancelamento = ctk.CTkFrame(frame_dias,  fg_color="#1E1E1E")
frame_cancelamento.pack(fill="x", padx=10, pady=5)
ctk.CTkLabel(frame_cancelamento, text="Texto para cancelamentos", font=('Arial', 14, 'bold')).pack()
label_texto_cancelamento = ctk.CTkLabel(frame_cancelamento, text="", wraplength=550, justify="left")
label_texto_cancelamento.pack(pady=5)
ctk.CTkButton(frame_cancelamento, 
            fg_color="#32CD32", hover_color="#94ff94", 
            text_color="#333333",
            text="Texto para Cancelamento", command=copiar_ordem_dias).pack(pady=5)

# -----------------------------
# Rodapé
# -----------------------------
ctk.CTkLabel(app, text="\u00a9 2025 Joaquim 'Joather' Ferreira, Aquiles Alves Pereira, Vitor 'Stew' Glennon.", font=("Arial", 10), text_color="gray").pack(pady=10)

# Iniciar
app.mainloop()