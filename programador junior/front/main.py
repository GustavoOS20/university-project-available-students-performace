import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Detector de Padrões de Aprendizado")
app.geometry("1000x600")
app.configure(fg_color="#1B1B1B")

titulo = ctk.CTkLabel(
    app,
    text="Detector de Padrões de Aprendizado",
    font=("Arial", 30, "bold"),
    text_color="#80B918"
)
titulo.pack(pady=40)

ctk.CTkButton(
    app,
    text="Cadastrar Aluno",
    width=300,
    height=50,
    fg_color="#2D6A4F",
    hover_color="#80B918"
).pack(pady=15)

ctk.CTkButton(
    app,
    text="Relatório Visual",
    width=300,
    height=50,
    fg_color="#2D6A4F",
    hover_color="#80B918"
).pack(pady=15)

ctk.CTkButton(
    app,
    text="Plano de Fluxo",
    width=300,
    height=50,
    fg_color="#2D6A4F",
    hover_color="#80B918"
).pack(pady=15)

app.mainloop()