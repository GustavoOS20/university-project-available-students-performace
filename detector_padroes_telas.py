
import customtkinter as ctk

# =====================
# PALETA DE CORES
# =====================
VERDE_LIMA = "#80B918"
VERDE_ESCURO = "#2D6A4F"
PRETO_SUAVE = "#1B1B1B"
CINZA_CLARO = "#E9ECE5"
BRANCO = "#FFFFFF"
VERMELHO = "#D00000"
LARANJA = "#C76A00"

ctk.set_appearance_mode("light")


class DetectorPadroesApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Detector de Padrões de Aprendizado")
        self.geometry("1250x720")
        self.configure(fg_color=CINZA_CLARO)

        self.alunos = [
            {
                "nome": "Ana Beatriz",
                "turma": "9º A",
                "matematica": [8.5, 7.5, 7.0, 8.0],
                "portugues": [7.0, 7.5, 8.0, 8.0],
                "historia": [8.0, 8.5, 8.0, 9.0],
            },
            {
                "nome": "Bruno Santos",
                "turma": "9º A",
                "matematica": [5.0, 6.0, 5.5, 6.0],
                "portugues": [6.0, 6.5, 6.0, 6.0],
                "historia": [6.0, 5.5, 6.0, 6.5],
            },
            {
                "nome": "Carlos Eduardo",
                "turma": "9º A",
                "matematica": [4.0, 5.0, 4.5, 4.0],
                "portugues": [5.5, 5.0, 5.5, 6.0],
                "historia": [5.0, 5.5, 5.0, 5.5],
            },
            {
                "nome": "Daniela Lima",
                "turma": "9º A",
                "matematica": [9.0, 8.5, 9.0, 8.0],
                "portugues": [8.5, 9.0, 9.0, 9.5],
                "historia": [8.0, 8.5, 9.0, 9.0],
            },
        ]

        self.criar_layout()
        self.mostrar_dashboard()

    # =====================
    # FUNÇÕES DE CÁLCULO
    # =====================
    def media(self, notas):
        return sum(notas) / len(notas)

    def media_aluno(self, aluno):
        medias = [
            self.media(aluno["matematica"]),
            self.media(aluno["portugues"]),
            self.media(aluno["historia"])
        ]
        return self.media(medias)

    def situacao(self, media):
        if media >= 7:
            return "Aprovado"
        elif media >= 6:
            return "Atenção"
        else:
            return "Em risco"

    def tendencia(self, notas):
        if notas[-1] < notas[-2] and notas[-2] < notas[-3]:
            return "Queda"
        elif notas[-1] > notas[-2]:
            return "Melhora"
        else:
            return "Estável"

    def probabilidade_aprovacao(self, media):
        return min((media / 7) * 100, 100)

    # =====================
    # LAYOUT PRINCIPAL
    # =====================
    def criar_layout(self):
        self.menu = ctk.CTkFrame(
            self,
            width=260,
            fg_color=VERDE_ESCURO,
            corner_radius=0
        )
        self.menu.pack(side="left", fill="y")
        self.menu.pack_propagate(False)

        ctk.CTkLabel(
            self.menu,
            text="DETECTOR DE\nPADRÕES DE\nAPRENDIZADO",
            text_color=BRANCO,
            font=("Arial", 24, "bold"),
            justify="left"
        ).pack(anchor="w", padx=25, pady=(40, 60))

        self.botao_dashboard = self.botao_menu("Dashboard", self.mostrar_dashboard)
        self.botao_dashboard.pack(fill="x", padx=20, pady=8)

        self.botao_alunos = self.botao_menu("Todos os Alunos", self.mostrar_alunos)
        self.botao_alunos.pack(fill="x", padx=20, pady=8)

        self.botao_disciplina = self.botao_menu("Análise por Disciplina", self.mostrar_disciplina)
        self.botao_disciplina.pack(fill="x", padx=20, pady=8)

        ctk.CTkLabel(
            self.menu,
            text="Aprender é detectar\npadrões e evoluir sempre.",
            text_color=BRANCO,
            font=("Arial", 14),
            justify="left"
        ).pack(side="bottom", anchor="w", padx=25, pady=35)

        self.area = ctk.CTkFrame(
            self,
            fg_color=CINZA_CLARO,
            corner_radius=0
        )
        self.area.pack(side="right", fill="both", expand=True, padx=25, pady=25)

    def botao_menu(self, texto, comando):
        return ctk.CTkButton(
            self.menu,
            text=texto,
            command=comando,
            fg_color=VERDE_LIMA,
            hover_color="#6EA414",
            text_color=PRETO_SUAVE,
            height=48,
            corner_radius=12,
            font=("Arial", 15, "bold")
        )

    def limpar_area(self):
        for widget in self.area.winfo_children():
            widget.destroy()

    def titulo_tela(self, titulo, subtitulo):
        ctk.CTkLabel(
            self.area,
            text=titulo,
            text_color=VERDE_ESCURO,
            font=("Arial", 32, "bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            self.area,
            text=subtitulo,
            text_color=PRETO_SUAVE,
            font=("Arial", 16)
        ).pack(anchor="w", pady=(2, 25))

    # =====================
    # TELA 1 - DASHBOARD
    # =====================
    def mostrar_dashboard(self):
        self.limpar_area()
        self.titulo_tela("Dashboard Principal", "Visão geral do desempenho da turma")

        medias_alunos = [self.media_aluno(aluno) for aluno in self.alunos]
        media_geral = self.media(medias_alunos)
        alunos_risco = len([m for m in medias_alunos if m < 6])
        probabilidade = self.probabilidade_aprovacao(media_geral)

        linha_cards = ctk.CTkFrame(self.area, fg_color=CINZA_CLARO)
        linha_cards.pack(fill="x", pady=5)

        self.criar_card(linha_cards, "Total de Alunos", len(self.alunos))
        self.criar_card(linha_cards, "Média Geral", f"{media_geral:.2f}")
        self.criar_card(linha_cards, "Chance de Aprovação", f"{probabilidade:.1f}%")
        self.criar_card(linha_cards, "Alunos em Risco", alunos_risco)

        painel = ctk.CTkFrame(self.area, fg_color=BRANCO, corner_radius=15)
        painel.pack(fill="both", expand=True, pady=25, padx=5)

        ctk.CTkLabel(
            painel,
            text="Resumo por Disciplina",
            text_color=VERDE_ESCURO,
            font=("Arial", 24, "bold")
        ).pack(anchor="w", padx=25, pady=(25, 15))

        disciplinas = [
            ("Matemática", "matematica"),
            ("Português", "portugues"),
            ("História", "historia")
        ]

        for nome, chave in disciplinas:
            notas = []
            for aluno in self.alunos:
                notas.extend(aluno[chave])

            media_disc = self.media(notas)
            tend = self.tendencia(notas)

            linha = ctk.CTkFrame(painel, fg_color=CINZA_CLARO, corner_radius=10)
            linha.pack(fill="x", padx=25, pady=8)

            ctk.CTkLabel(
                linha,
                text=nome,
                width=220,
                anchor="w",
                text_color=PRETO_SUAVE,
                font=("Arial", 18, "bold")
            ).pack(side="left", padx=20, pady=15)

            ctk.CTkLabel(
                linha,
                text=f"Média: {media_disc:.2f}",
                width=180,
                anchor="w",
                text_color=VERDE_ESCURO if media_disc >= 7 else VERMELHO,
                font=("Arial", 18, "bold")
            ).pack(side="left", padx=20)

            ctk.CTkLabel(
                linha,
                text=f"Tendência: {tend}",
                anchor="w",
                text_color=PRETO_SUAVE,
                font=("Arial", 18)
            ).pack(side="left", padx=20)

    def criar_card(self, pai, titulo, valor):
        card = ctk.CTkFrame(
            pai,
            fg_color=BRANCO,
            corner_radius=15,
            width=220,
            height=115
        )
        card.pack(side="left", padx=8, pady=5)
        card.pack_propagate(False)

        ctk.CTkLabel(
            card,
            text=titulo,
            text_color=PRETO_SUAVE,
            font=("Arial", 14, "bold")
        ).pack(pady=(18, 5))

        ctk.CTkLabel(
            card,
            text=str(valor),
            text_color=VERDE_ESCURO,
            font=("Arial", 30, "bold")
        ).pack()

    # =====================
    # TELA 2 - TODOS OS ALUNOS
    # =====================
    def mostrar_alunos(self):
        self.limpar_area()
        self.titulo_tela("Todos os Alunos", "Lista de alunos e médias gerais")

        tabela = ctk.CTkFrame(self.area, fg_color=BRANCO, corner_radius=12)
        tabela.pack(fill="x", padx=5, pady=10)

        colunas = [
            "ID", "ALUNO", "TURMA",
            "MATEMÁTICA", "PORTUGUÊS", "HISTÓRIA",
            "MÉDIA", "SITUAÇÃO"
        ]

        larguras = [60, 210, 100, 135, 135, 135, 110, 135]

        for coluna, largura in enumerate(larguras):
            tabela.grid_columnconfigure(coluna, minsize=largura)

        for i, nome_coluna in enumerate(colunas):
            label = ctk.CTkLabel(
                tabela,
                text=nome_coluna,
                fg_color=VERDE_ESCURO,
                text_color=BRANCO,
                font=("Arial", 14, "bold"),
                height=55,
                width=larguras[i]
            )
            label.grid(row=0, column=i, sticky="nsew", padx=1, pady=1)

        for linha, aluno in enumerate(self.alunos, start=1):
            media_mat = self.media(aluno["matematica"])
            media_port = self.media(aluno["portugues"])
            media_hist = self.media(aluno["historia"])
            media_final = self.media_aluno(aluno)
            situacao = self.situacao(media_final)

            dados = [
                linha,
                aluno["nome"],
                aluno["turma"],
                f"{media_mat:.2f}",
                f"{media_port:.2f}",
                f"{media_hist:.2f}",
                f"{media_final:.2f}",
                situacao
            ]

            for coluna, valor in enumerate(dados):
                cor_texto = PRETO_SUAVE

                if coluna in [3, 4, 5, 6]:
                    cor_texto = VERDE_ESCURO if float(valor) >= 7 else VERMELHO

                if coluna == 7:
                    if valor == "Aprovado":
                        cor_texto = VERDE_ESCURO
                    elif valor == "Atenção":
                        cor_texto = LARANJA
                    else:
                        cor_texto = VERMELHO

                label = ctk.CTkLabel(
                    tabela,
                    text=str(valor),
                    fg_color=BRANCO,
                    text_color=cor_texto,
                    font=("Arial", 14, "bold" if coluna >= 3 else "normal"),
                    height=55,
                    width=larguras[coluna]
                )
                label.grid(row=linha, column=coluna, sticky="nsew", padx=1, pady=1)

    # =====================
    # TELA 3 - ANÁLISE POR DISCIPLINA
    # =====================
    def mostrar_disciplina(self):
        self.limpar_area()
        self.titulo_tela(
            "Análise Detalhada por Disciplina",
            "Escolha uma disciplina para visualizar desempenho, tendência e sugestão de foco"
        )

        linha_filtros = ctk.CTkFrame(self.area, fg_color=CINZA_CLARO)
        linha_filtros.pack(anchor="w", pady=(0, 20))

        ctk.CTkLabel(
            linha_filtros,
            text="Disciplina:",
            text_color=PRETO_SUAVE,
            font=("Arial", 15, "bold")
        ).pack(side="left", padx=(0, 10))

        self.combo_disciplina = ctk.CTkComboBox(
            linha_filtros,
            values=["Matemática", "Português", "História"],
            command=self.atualizar_analise,
            width=220
        )
        self.combo_disciplina.pack(side="left")

        self.painel_analise = ctk.CTkFrame(self.area, fg_color=BRANCO, corner_radius=15)
        self.painel_analise.pack(fill="both", expand=True, padx=5, pady=10)

        self.combo_disciplina.set("Matemática")
        self.atualizar_analise("Matemática")

    def atualizar_analise(self, disciplina):
        for widget in self.painel_analise.winfo_children():
            widget.destroy()

        mapa = {
            "Matemática": "matematica",
            "Português": "portugues",
            "História": "historia"
        }

        chave = mapa[disciplina]

        notas = []
        for aluno in self.alunos:
            notas.extend(aluno[chave])

        media_disc = self.media(notas)
        maior = max(notas)
        menor = min(notas)
        variacao = notas[-1] - notas[0]
        tend = self.tendencia(notas)
        probabilidade = self.probabilidade_aprovacao(media_disc)
        situacao = self.situacao(media_disc)

        if media_disc >= 7:
            sugestao = "A turma apresenta bom desempenho. Continue mantendo a rotina de estudos."
        elif media_disc >= 6:
            sugestao = "A disciplina precisa de atenção. Reforce exercícios e revise os conteúdos principais."
        else:
            sugestao = "A disciplina está em situação de risco. É recomendado foco maior e acompanhamento do professor."

        ctk.CTkLabel(
            self.painel_analise,
            text=f"Disciplina: {disciplina}",
            text_color=VERDE_ESCURO,
            font=("Arial", 24, "bold")
        ).pack(anchor="w", padx=25, pady=(25, 10))

        texto = f"""
Notas registradas: {notas}

Média da disciplina: {media_disc:.2f}
Maior nota: {maior:.1f}
Menor nota: {menor:.1f}
Variação entre início e fim: {variacao:.1f}

Tendência identificada: {tend}
Probabilidade estimada de aprovação: {probabilidade:.1f}%

Situação geral: {situacao}

Sugestão de foco:
{sugestao}
"""

        ctk.CTkLabel(
            self.painel_analise,
            text=texto,
            text_color=PRETO_SUAVE,
            font=("Arial", 18),
            justify="left"
        ).pack(anchor="w", padx=25, pady=10)


if __name__ == "__main__":
    app = DetectorPadroesApp()
    app.mainloop()
