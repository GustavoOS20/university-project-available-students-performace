import customtkinter as ctk

app = ctk.CTk()
app.title("Plano de Fluxo")
app.geometry("1000x650")
app.configure(fg_color="#1B1B1B")

titulo = ctk.CTkLabel(
    app,
    text="Fluxo do Sistema",
    font=("Arial", 28, "bold"),
    text_color="#80B918"
)
titulo.pack(pady=20)

fluxo = """
INÍCIO
   ↓

Cadastrar Aluno

   ↓

Inserir A1, A2 e A3

   ↓

Criar Vetor de Notas

   ↓

Calcular Total e Média

   ↓

Analisar Tendência

   ↓

Detectar Queda ou Melhora

   ↓

Gerar Relatório Visual

   ↓

FIM
"""

ctk.CTkLabel(
    app,
    text=fluxo,
    font=("Consolas", 22),
    text_color="#E9ECE5"
).pack(pady=40)

app.mainloop()