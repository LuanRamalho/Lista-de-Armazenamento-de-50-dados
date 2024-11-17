import tkinter as tk
from tkinter import messagebox

# Função para inserir os dados
def adicionar_dado():
    if len(lista_dados) < 50:
        dado = entrada_dado.get()
        if dado.strip():
            lista_dados.append(dado)
            lista_box.insert(tk.END, f"Dado {len(lista_dados)}/50: {dado}")
            entrada_dado.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Por favor, insira um dado válido!")
    else:
        messagebox.showinfo("Concluído", "Você já inseriu 50 dados!")

# Função para exibir todos os dados
def exibir_dados():
    if lista_dados:
        dados_formatados = "\n".join([f"{i + 1}: {d}" for i, d in enumerate(lista_dados)])
        messagebox.showinfo("Dados Inseridos", dados_formatados)
    else:
        messagebox.showwarning("Aviso", "Nenhum dado foi inserido ainda!")

# Função para remover um dado selecionado
def remover_dado():
    selecionado = lista_box.curselection()
    if selecionado:
        indice = selecionado[0]
        lista_dados.pop(indice)
        lista_box.delete(indice)
        messagebox.showinfo("Sucesso", "Dado removido com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Por favor, selecione um dado para remover!")

# Janela principal
janela = tk.Tk()
janela.title("Programa de Dados")
janela.geometry("500x600")
janela.configure(bg="#ffdfba")

# Lista para armazenar os dados
lista_dados = []

# Rótulo de título
titulo = tk.Label(janela, text="Programa de Inserção e Remoção de Dados", bg="#ffb6c1", font=("Helvetica", 16, "bold"))
titulo.pack(pady=10)

# Entrada para o dado
entrada_dado = tk.Entry(janela, font=("Helvetica", 12))
entrada_dado.pack(pady=5)

# Botão para adicionar o dado
btn_adicionar = tk.Button(janela, text="Adicionar Dado", bg="#add8e6", font=("Helvetica", 12, "bold"), command=adicionar_dado)
btn_adicionar.pack(pady=5)

# Lista para exibir os dados inseridos
lista_box = tk.Listbox(janela, width=50, height=15, font=("Helvetica", 10))
lista_box.pack(pady=10)

# Botão para remover o dado selecionado
btn_remover = tk.Button(janela, text="Remover Dado", bg="#f08080", font=("Helvetica", 12, "bold"), command=remover_dado)
btn_remover.pack(pady=5)

# Botão para exibir todos os dados
btn_exibir = tk.Button(janela, text="Exibir Todos os Dados", bg="#90ee90", font=("Helvetica", 12, "bold"), command=exibir_dados)
btn_exibir.pack(pady=5)

# Iniciar a interface gráfica
janela.mainloop()
