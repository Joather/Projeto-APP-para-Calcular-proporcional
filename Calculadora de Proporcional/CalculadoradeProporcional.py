# calculadora_proporcional.py

import sys
import os
import customtkinter

# Definir o caminho correto para o tema, tanto no modo .py quanto .exe
if hasattr(sys, '_MEIPASS'):
    theme_path = os.path.join(sys._MEIPASS, "assets", "zenix.json")
else:
    theme_path = os.path.join(os.path.dirname(__file__), "assets", "zenix.json")

if hasattr(sys, '_MEIPASS'):
    icon_path = os.path.join(sys._MEIPASS, "assets", "logo.ico")
else:
    icon_path = os.path.join(os.path.dirname(__file__), "assets", "logo.ico")

if hasattr(sys, '_MEIPASS'):
    logo_path = os.path.join(sys._MEIPASS, "assets", "logo.png")
else:
    logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")

import customtkinter as ctk
from tkinter import messagebox
from customtkinter import CTkImage
from PIL import Image, ImageTk

# Configuração inicial
ctk.set_appearance_mode("System")
customtkinter.set_default_color_theme(theme_path)

app = ctk.CTk()
app.title("Calculadora de Proporcional")
app.iconbitmap(icon_path)
app.geometry("750x650+150+20")
app.resizable(True, True)

# Logo da Zenix
logo = Image.open(logo_path)
logo_ctk = CTkImage(light_image=logo, dark_image=logo, size=(120, 31))
label_imagem = ctk.CTkLabel(app, text="", image=logo_ctk)
label_imagem.pack(pady=(20, 10))

# Tabs
tabview = ctk.CTkTabview(app, width=600,)
tabview.pack(pady=(0, 20))
tabview.add("Alteração de Plano")
tabview.add("Alteração de Vencimento")
tabview.add("Desconto ou Cancelamento")

# Variáveis globais para copiar
texto_cliente_plano = ""
texto_ordem_plano = ""
texto_cliente_vencimento = ""
texto_ordem_vencimento = ""
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

        if dia_vencimento == dia_alteracao:
            ValueError
            messagebox.showerror("Erro", "Se o cliente solicitou a troca do plano no mesmo dia do vencimento, não tem proporcional!!!")

        elif dia_alteracao > dia_vencimento:
            dias_plano_atual = dia_alteracao - dia_vencimento
            dias_plano_novo = 30 - dias_plano_atual
        else:
            dias_plano_atual = 30 - (dia_vencimento - dia_alteracao)
            dias_plano_novo = 30 - dias_plano_atual
        
        if dia_alteracao == 31:
            dias_plano_atual = dias_plano_atual + 1
            diaria_plano_atual = valor_plano_atual / 31
            diaria_plano_novo = valor_plano_novo / 31
        else:
            diaria_plano_atual = valor_plano_atual / 30
            diaria_plano_novo = valor_plano_novo / 30

        proporcional_atual = diaria_plano_atual * dias_plano_atual
        proporcional_novo = diaria_plano_novo * dias_plano_novo
        valor_total = proporcional_atual + proporcional_novo



        texto_cliente_plano = (
            f"Realizando a troca de plano no *dia {dia_alteracao}*, o valor proporcional a ser pago será:",
            f"\n- *{dias_plano_atual}* dias do plano atual *(R$ {proporcional_atual:.2f})*",
            f"\n- *{dias_plano_novo}* dias do novo plano *(R$ {proporcional_novo:.2f})*",
            f"\nTotal na próxima fatura: *R$ {valor_total:.2f}*, que será para a data *{dia_vencimento}/XX*\n\n"
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

        if texto_cliente_plano.strip():
            label_texto_cliente1.configure(text=texto_cliente_plano)
            label_texto_cliente1.pack(pady=5)
        else:
            label_texto_cliente1.pack_forget()

        if texto_ordem_plano.strip():
            label_texto_ordem1.configure(text=texto_ordem_plano)
            label_texto_ordem1.pack(pady=5)
        else:
            label_texto_ordem1.pack_forget()

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
        
        if vencimento_atual == vencimento_novo:
            ValueError
            messagebox.showerror("Erro", "Se o cliente solicitou a troca do plano no mesmo dia do vencimento, não tem proporcional!!!")
        
        elif vencimento_atual < vencimento_novo:
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

        if texto_cliente_vencimento.strip():
            label_texto_cliente2.configure(text=texto_cliente_vencimento)
            label_texto_cliente2.pack(pady=5)
        else:
            label_texto_cliente2.pack_forget()

        if texto_ordem_vencimento.strip():
            label_texto_ordem2.configure(text=texto_ordem_vencimento)
            label_texto_ordem2.pack(pady=5)
        else:
            label_texto_ordem2.pack_forget()


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

        if texto_cliente_dias.strip():
            label_texto_desconto.configure(text=texto_cliente_dias)
            label_texto_desconto.pack(pady=5)
        else:
            label_texto_desconto.pack_forget()

        if texto_ordem_dias.strip():
            label_texto_cancelamento.configure(text=texto_ordem_dias)
            label_texto_cancelamento.pack(pady=5)
        else:
            label_texto_cancelamento.pack_forget()


    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos.")

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
frame_plano = tabview.tab("Alteração de Plano")
frame_plano.configure(corner_radius=10)

scrollable_frame_plano = ctk.CTkScrollableFrame(frame_plano, width=600, height=400)
scrollable_frame_plano.pack(fill="both", expand=True)

label_valor_plano_atual = ctk.CTkLabel(scrollable_frame_plano, text="Digite o valor do plano atual (R$):")
label_valor_plano_atual.pack(pady=0)
entry_valor_plano_atual = ctk.CTkEntry(scrollable_frame_plano, placeholder_text="Valor do plano atual")
entry_valor_plano_atual.pack(pady=(0, 15))

label_valor_plano_novo = ctk.CTkLabel(scrollable_frame_plano, text="Digite o valor do plano novo (R$):")
label_valor_plano_novo.pack(pady=0)
entry_valor_plano_novo = ctk.CTkEntry(scrollable_frame_plano, placeholder_text="Valor do novo plano")
entry_valor_plano_novo.pack(pady=(0, 15))

label_dia_vencimento = ctk.CTkLabel(scrollable_frame_plano, text="Digite o dia do vencimento:")
label_dia_vencimento.pack(pady=0)
entry_dia_vencimento = ctk.CTkEntry(scrollable_frame_plano, placeholder_text="Dia do vencimento")
entry_dia_vencimento.pack(pady=(0, 15))

label_dia_alteracao = ctk.CTkLabel(scrollable_frame_plano, text="Digite o dia da troca:")
label_dia_alteracao.pack(pady=0)
entry_dia_alteracao = ctk.CTkEntry(scrollable_frame_plano, placeholder_text="Dia da alteração")
entry_dia_alteracao.pack(pady=(0, 0))

botao_calcular_plano = ctk.CTkButton(scrollable_frame_plano, 
                                    text="Calcular", 
                                    command=calcular_alteracao_plano)
botao_calcular_plano.pack(pady=10)

frame_cliente1 = ctk.CTkFrame(scrollable_frame_plano) 
frame_cliente1.pack(fill="x", padx=10, pady=5)

ctk.CTkLabel(frame_cliente1,
            text="Texto para encaminhar para o Cliente").pack()
label_texto_cliente1 = ctk.CTkLabel(frame_cliente1, text="", wraplength=650, justify="left")
label_texto_cliente1.pack(pady=5)
ctk.CTkButton(frame_cliente1,
            text="Copiar Texto Cliente", 
            command=copiar_cliente_plano).pack(pady=5)

frame_ordem1 = ctk.CTkFrame(scrollable_frame_plano)
frame_ordem1.pack(fill="x", padx=10, pady=5)
ctk.CTkLabel(frame_ordem1, text="Texto para o Cadastro em Sistema").pack()
label_texto_ordem1 = ctk.CTkLabel(frame_ordem1, text="", wraplength=650, justify="left")
label_texto_ordem1.pack(pady=5)
ctk.CTkButton(frame_ordem1,
            text="Copiar Texto Ordem", command=copiar_ordem_plano).pack(pady=5)

# -----------------------------
# Layout - Aba: Alteracao de Vencimento
# -----------------------------
frame_vencimento = tabview.tab("Alteração de Vencimento")
frame_vencimento.configure(corner_radius=10)

scrollable_frame_vencimento = ctk.CTkScrollableFrame(frame_vencimento, width=600, height=400)
scrollable_frame_vencimento.pack(fill="both", expand=True)

label_vencimento_atual = ctk.CTkLabel(scrollable_frame_vencimento, text="Dia do vencimento atual:")
label_vencimento_atual.pack(pady=0)
entry_vencimento_atual = ctk.CTkEntry(scrollable_frame_vencimento, placeholder_text="Vencimento atual")
entry_vencimento_atual.pack(pady=(0, 15))

label_vencimento_novo = ctk.CTkLabel(scrollable_frame_vencimento, text="Dia do novo vencimento:")
label_vencimento_novo.pack(pady=0)   
entry_vencimento_novo = ctk.CTkEntry(scrollable_frame_vencimento, placeholder_text="Novo vencimento")
entry_vencimento_novo.pack(pady=(0, 15))

label_valor_plano_vencimento = ctk.CTkLabel(scrollable_frame_vencimento, text="Valor do plano (R$):")
label_valor_plano_vencimento.pack(pady=0)
entry_valor_plano_vencimento = ctk.CTkEntry(scrollable_frame_vencimento, placeholder_text="Valor do plano")
entry_valor_plano_vencimento.pack(pady=(0 , 0))

botao_calcular_vencimento = ctk.CTkButton(scrollable_frame_vencimento,                                  
                                        text="Calcular", command=calcular_alteracao_vencimento)
botao_calcular_vencimento.pack(pady=10)

frame_cliente2 = ctk.CTkFrame(scrollable_frame_vencimento)
frame_cliente2.pack(fill="x", padx=10, pady=5)

ctk.CTkLabel(frame_cliente2, text="Texto para encaminhar para o Cliente").pack()
label_texto_cliente2 = ctk.CTkLabel(frame_cliente2, text="", wraplength=650, justify="left")
label_texto_cliente2.pack(pady=5)
ctk.CTkButton(frame_cliente2,
            text="Copiar Texto Cliente", command=copiar_cliente_vencimento).pack(pady=5)

frame_ordem2 = ctk.CTkFrame(scrollable_frame_vencimento)
frame_ordem2.pack(fill="x", padx=10, pady=5)

ctk.CTkLabel(frame_ordem2, text="Texto para o Cadastro em Sistema").pack()
label_texto_ordem2 = ctk.CTkLabel(frame_ordem2, text="", wraplength=650, justify="left")
label_texto_ordem2.pack(pady=5)
ctk.CTkButton(frame_ordem2, 
            text="Copiar Texto Ordem", command=copiar_ordem_vencimento).pack(pady=5)

# -----------------------------
# Layout - Aba: Proporcional de Dias
# -----------------------------
frame_dias = tabview.tab("Desconto ou Cancelamento")
frame_dias.configure(corner_radius=10)

scrollable_frame_dias = ctk.CTkScrollableFrame(frame_dias, width=600, height=400)
scrollable_frame_dias.pack(fill="both", expand=True)

label_valor_plano = ctk.CTkLabel(scrollable_frame_dias, text="Digite o valor do plano (R$):")
label_valor_plano.pack(pady=0)
entry_valor_plano = ctk.CTkEntry(scrollable_frame_dias, placeholder_text="Valor do plano")
entry_valor_plano.pack(pady=(0, 20))
label_dias_proporcional = ctk.CTkLabel(scrollable_frame_dias, text="Digite os dias para o calculo de proporcional:")
label_dias_proporcional.pack(pady=0)
entry_dias_proporcional = ctk.CTkEntry(scrollable_frame_dias, placeholder_text="Digite os dias para o calculo")
entry_dias_proporcional.pack(pady=(0, 20))

botao_calcular_proporcional = ctk.CTkButton(scrollable_frame_dias, 
                                            text="Calcular", command=calcular_dias)
botao_calcular_proporcional.pack(pady=10)

frame_desconto = ctk.CTkFrame(scrollable_frame_dias)
frame_desconto.pack(fill="x", padx=10, pady=5)
ctk.CTkLabel(frame_desconto, text="Texto para Utilizar em Descontos").pack()
label_texto_desconto = ctk.CTkLabel(frame_desconto, text="", wraplength=550, justify="left")
label_texto_desconto.pack(pady=5)
ctk.CTkButton(frame_desconto,
            text="Copiar Texto Descontos", command=copiar_cliente_dias).pack(pady=5)

frame_cancelamento = ctk.CTkFrame(scrollable_frame_dias)
frame_cancelamento.pack(fill="x", padx=10, pady=5)
ctk.CTkLabel(frame_cancelamento, text="Texto para Utilizar em Cancelamentos").pack()
label_texto_cancelamento = ctk.CTkLabel(frame_cancelamento, text="", wraplength=550, justify="left")
label_texto_cancelamento.pack(pady=5)
ctk.CTkButton(frame_cancelamento,
            text="Copiar Texto Cancelamentos", command=copiar_ordem_dias).pack(pady=5)

# -----------------------------
# Rodapé
# -----------------------------
ctk.CTkLabel(app, text="\u00a9 2025 Joaquim 'Joather' Ferreira, Aquiles Alves Pereira, Vitor 'Stew' Glennon.", font=("Arial", 10), text_color="gray").pack(pady=10)

# Iniciar
app.mainloop()