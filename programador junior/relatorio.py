import customtkinter as ctk

app = ctk.CTk()
app.title("Cadastro de Aluno")
app.geometry("1000x650")
app.configure(fg_color="#1B1B1B")

titulo = ctk.CTkLabel(
    app,
    text="Cadastro de Aluno e Notas",
    font=("Arial", 28, "bold"),
    text_color="#80B918"
)
titulo.pack(pady=20)

nome = ctk.CTkEntry(
    app,
    width=350,
    placeholder_text="Nome do aluno"
)
nome.pack(pady=10)

a1 = ctk.CTkEntry(
    app,
    width=350,
    placeholder_text="Nota A1 (0 a 30)"
)
a1.pack(pady=10)

a2 = ctk.CTkEntry(
    app,
    width=350,
    placeholder_text="Nota A2 (0 a 30)"
)
a2.pack(pady=10)

a3 = ctk.CTkEntry(
    app,
    width=350,
    placeholder_text="Nota A3 (0 a 40)"
)
a3.pack(pady=10)

ctk.CTkButton(
    app,
    text="Salvar Dados",
    width=250,
    height=45,
    fg_color="#2D6A4F",
    hover_color="#80B918"
).pack(pady=25)

app.mainloop()