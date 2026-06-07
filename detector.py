import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk

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
AZUL = "#1A6FA8"

ctk.set_appearance_mode("light")


class DetectorPadroesApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Detector de Padrões de Aprendizado")
        self.geometry("1350x780")
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
            width=270,
            fg_color=VERDE_ESCURO,
            corner_radius=0
        )
        self.menu.pack(side="left", fill="y")
        self.menu.pack_propagate(False)

        ctk.CTkLabel(
            self.menu,
            text="DETECTOR DE\nPADRÕES DE\nAPRENDIZADO",
            text_color=BRANCO,
            font=("Arial", 22, "bold"),
            justify="left"
        ).pack(anchor="w", padx=25, pady=(35, 45))

        botoes = [
            ("📊  Dashboard",         self.mostrar_dashboard),
            ("👥  Todos os Alunos",    self.mostrar_alunos),
            ("📚  Análise por Disciplina", self.mostrar_disciplina),
            ("➕  Cadastrar Aluno",    self.mostrar_cadastro),
            ("📝  Lançar Notas",       self.mostrar_lancamento),
            ("📈  Relatório Visual",   self.mostrar_relatorio),
        ]

        self.botoes_menu = []
        for texto, comando in botoes:
            btn = self.botao_menu(texto, comando)
            btn.pack(fill="x", padx=18, pady=6)
            self.botoes_menu.append(btn)

        ctk.CTkLabel(
            self.menu,
            text="Aprender é detectar\npadrões e evoluir sempre.",
            text_color=BRANCO,
            font=("Arial", 13),
            justify="left"
        ).pack(side="bottom", anchor="w", padx=25, pady=30)

        self.area = ctk.CTkScrollableFrame(
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
            height=46,
            corner_radius=12,
            font=("Arial", 14, "bold"),
            anchor="w"
        )

    def limpar_area(self):
        for widget in self.area.winfo_children():
            widget.destroy()

    def titulo_tela(self, titulo, subtitulo):
        ctk.CTkLabel(
            self.area,
            text=titulo,
            text_color=VERDE_ESCURO,
            font=("Arial", 30, "bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            self.area,
            text=subtitulo,
            text_color=PRETO_SUAVE,
            font=("Arial", 15)
        ).pack(anchor="w", pady=(2, 22))

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
        painel.pack(fill="both", expand=True, pady=22, padx=5)

        ctk.CTkLabel(
            painel,
            text="Resumo por Disciplina",
            text_color=VERDE_ESCURO,
            font=("Arial", 22, "bold")
        ).pack(anchor="w", padx=25, pady=(22, 12))

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
            linha.pack(fill="x", padx=25, pady=7)

            ctk.CTkLabel(
                linha, text=nome, width=220, anchor="w",
                text_color=PRETO_SUAVE, font=("Arial", 17, "bold")
            ).pack(side="left", padx=20, pady=14)

            ctk.CTkLabel(
                linha, text=f"Média: {media_disc:.2f}", width=180, anchor="w",
                text_color=VERDE_ESCURO if media_disc >= 7 else VERMELHO,
                font=("Arial", 17, "bold")
            ).pack(side="left", padx=20)

            ctk.CTkLabel(
                linha, text=f"Tendência: {tend}", anchor="w",
                text_color=PRETO_SUAVE, font=("Arial", 17)
            ).pack(side="left", padx=20)

    def criar_card(self, pai, titulo, valor):
        card = ctk.CTkFrame(pai, fg_color=BRANCO, corner_radius=15, width=210, height=110)
        card.pack(side="left", padx=8, pady=5)
        card.pack_propagate(False)

        ctk.CTkLabel(card, text=titulo, text_color=PRETO_SUAVE,
                     font=("Arial", 13, "bold")).pack(pady=(16, 4))
        ctk.CTkLabel(card, text=str(valor), text_color=VERDE_ESCURO,
                     font=("Arial", 28, "bold")).pack()

    # =====================
    # TELA 2 - TODOS OS ALUNOS
    # =====================
    def mostrar_alunos(self):
        self.limpar_area()
        self.titulo_tela("Todos os Alunos", "Lista completa com médias e situação de cada aluno")

        if not self.alunos:
            ctk.CTkLabel(self.area, text="Nenhum aluno cadastrado ainda.",
                         font=("Arial", 16), text_color=PRETO_SUAVE).pack(pady=40)
            return

        tabela = ctk.CTkFrame(self.area, fg_color=BRANCO, corner_radius=12)
        tabela.pack(fill="x", padx=5, pady=10)

        colunas = ["#", "ALUNO", "TURMA", "MATEMÁTICA", "PORTUGUÊS", "HISTÓRIA", "MÉDIA", "SITUAÇÃO"]
        larguras = [50, 200, 100, 120, 120, 120, 100, 120]

        for i, (col, larg) in enumerate(zip(colunas, larguras)):
            ctk.CTkLabel(
                tabela, text=col, fg_color=VERDE_ESCURO, text_color=BRANCO,
                font=("Arial", 13, "bold"), height=50, width=larg
            ).grid(row=0, column=i, sticky="nsew", padx=1, pady=1)

        for linha, aluno in enumerate(self.alunos, start=1):
            media_mat  = self.media(aluno["matematica"])
            media_port = self.media(aluno["portugues"])
            media_hist = self.media(aluno["historia"])
            media_fin  = self.media_aluno(aluno)
            sit        = self.situacao(media_fin)

            dados = [linha, aluno["nome"], aluno["turma"],
                     f"{media_mat:.2f}", f"{media_port:.2f}",
                     f"{media_hist:.2f}", f"{media_fin:.2f}", sit]

            bg = BRANCO if linha % 2 == 0 else "#F4F7F2"

            for col, (valor, larg) in enumerate(zip(dados, larguras)):
                cor = PRETO_SUAVE
                if col in [3, 4, 5, 6]:
                    cor = VERDE_ESCURO if float(valor) >= 7 else VERMELHO
                if col == 7:
                    cor = VERDE_ESCURO if valor == "Aprovado" else (LARANJA if valor == "Atenção" else VERMELHO)

                ctk.CTkLabel(
                    tabela, text=str(valor), fg_color=bg, text_color=cor,
                    font=("Arial", 13, "bold" if col >= 3 else "normal"),
                    height=50, width=larg
                ).grid(row=linha, column=col, sticky="nsew", padx=1, pady=1)

        # Botão excluir
        frame_excluir = ctk.CTkFrame(self.area, fg_color=CINZA_CLARO)
        frame_excluir.pack(anchor="w", pady=(15, 5))

        ctk.CTkLabel(frame_excluir, text="Excluir aluno pelo nome:",
                     font=("Arial", 14), text_color=PRETO_SUAVE).pack(side="left", padx=(0, 10))

        self.entry_excluir = ctk.CTkEntry(frame_excluir, width=220, placeholder_text="Nome do aluno")
        self.entry_excluir.pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            frame_excluir, text="Excluir", fg_color=VERMELHO,
            hover_color="#A00000", text_color=BRANCO,
            font=("Arial", 13, "bold"), width=100,
            command=self.excluir_aluno
        ).pack(side="left")

    def excluir_aluno(self):
        nome = self.entry_excluir.get().strip()
        antes = len(self.alunos)
        self.alunos = [a for a in self.alunos if a["nome"].lower() != nome.lower()]
        if len(self.alunos) < antes:
            messagebox.showinfo("Sucesso", f"Aluno '{nome}' removido.")
            self.mostrar_alunos()
        else:
            messagebox.showerror("Erro", f"Aluno '{nome}' não encontrado.")

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
        linha_filtros.pack(anchor="w", pady=(0, 18))

        ctk.CTkLabel(linha_filtros, text="Disciplina:", text_color=PRETO_SUAVE,
                     font=("Arial", 14, "bold")).pack(side="left", padx=(0, 10))

        self.combo_disciplina = ctk.CTkComboBox(
            linha_filtros, values=["Matemática", "Português", "História"],
            command=self.atualizar_analise, width=220
        )
        self.combo_disciplina.pack(side="left")

        self.painel_analise = ctk.CTkFrame(self.area, fg_color=BRANCO, corner_radius=15)
        self.painel_analise.pack(fill="both", expand=True, padx=5, pady=10)

        self.combo_disciplina.set("Matemática")
        self.atualizar_analise("Matemática")

    def atualizar_analise(self, disciplina):
        for widget in self.painel_analise.winfo_children():
            widget.destroy()

        mapa = {"Matemática": "matematica", "Português": "portugues", "História": "historia"}
        chave = mapa[disciplina]

        notas = []
        for aluno in self.alunos:
            notas.extend(aluno[chave])

        if not notas:
            ctk.CTkLabel(self.painel_analise, text="Sem dados.", font=("Arial", 16)).pack(pady=30)
            return

        media_disc   = self.media(notas)
        maior        = max(notas)
        menor        = min(notas)
        variacao     = notas[-1] - notas[0]
        tend         = self.tendencia(notas)
        probabilidade = self.probabilidade_aprovacao(media_disc)
        situacao     = self.situacao(media_disc)

        if media_disc >= 7:
            sugestao = "A turma apresenta bom desempenho. Continue mantendo a rotina de estudos."
        elif media_disc >= 6:
            sugestao = "A disciplina precisa de atenção. Reforce exercícios e revise os conteúdos principais."
        else:
            sugestao = "A disciplina está em situação de risco. É recomendado foco maior e acompanhamento do professor."

        ctk.CTkLabel(
            self.painel_analise, text=f"Disciplina: {disciplina}",
            text_color=VERDE_ESCURO, font=("Arial", 22, "bold")
        ).pack(anchor="w", padx=25, pady=(22, 10))

        texto = (
            f"Notas registradas: {notas}\n\n"
            f"Média da disciplina: {media_disc:.2f}\n"
            f"Maior nota: {maior:.1f}\n"
            f"Menor nota: {menor:.1f}\n"
            f"Variação entre início e fim: {variacao:.1f}\n\n"
            f"Tendência identificada: {tend}\n"
            f"Probabilidade estimada de aprovação: {probabilidade:.1f}%\n\n"
            f"Situação geral: {situacao}\n\n"
            f"Sugestão de foco:\n{sugestao}"
        )

        ctk.CTkLabel(
            self.painel_analise, text=texto, text_color=PRETO_SUAVE,
            font=("Arial", 16), justify="left"
        ).pack(anchor="w", padx=25, pady=10)

    # =====================
    # TELA 4 - CADASTRAR ALUNO
    # =====================
    def mostrar_cadastro(self):
        self.limpar_area()
        self.titulo_tela("Cadastrar Novo Aluno", "Preencha os dados do aluno e suas notas bimestrais")

        painel = ctk.CTkFrame(self.area, fg_color=BRANCO, corner_radius=15)
        painel.pack(fill="x", padx=5, pady=10)

        def campo(pai, label, row, placeholder=""):
            ctk.CTkLabel(pai, text=label, text_color=PRETO_SUAVE,
                         font=("Arial", 14, "bold")).grid(row=row, column=0, sticky="w", padx=30, pady=10)
            entry = ctk.CTkEntry(pai, width=300, placeholder_text=placeholder)
            entry.grid(row=row, column=1, sticky="w", padx=20, pady=10)
            return entry

        self.cad_nome  = campo(painel, "Nome do aluno:",  0, "Ex: João Silva")
        self.cad_turma = campo(painel, "Turma:",          1, "Ex: 9º A")

        ctk.CTkLabel(painel, text="── Notas de Matemática (4 bimestres) ──",
                     text_color=VERDE_ESCURO, font=("Arial", 14, "bold")
                     ).grid(row=2, column=0, columnspan=4, padx=30, pady=(20, 5), sticky="w")

        self.cad_mat = self._linha_notas(painel, 3)

        ctk.CTkLabel(painel, text="── Notas de Português (4 bimestres) ──",
                     text_color=VERDE_ESCURO, font=("Arial", 14, "bold")
                     ).grid(row=4, column=0, columnspan=4, padx=30, pady=(15, 5), sticky="w")

        self.cad_port = self._linha_notas(painel, 5)

        ctk.CTkLabel(painel, text="── Notas de História (4 bimestres) ──",
                     text_color=VERDE_ESCURO, font=("Arial", 14, "bold")
                     ).grid(row=6, column=0, columnspan=4, padx=30, pady=(15, 5), sticky="w")

        self.cad_hist = self._linha_notas(painel, 7)

        ctk.CTkButton(
            painel, text="✔  Salvar Aluno", fg_color=VERDE_ESCURO,
            hover_color="#1F4D38", text_color=BRANCO,
            font=("Arial", 15, "bold"), height=48, width=220,
            command=self.salvar_aluno
        ).grid(row=8, column=0, columnspan=4, pady=30)

    def _linha_notas(self, pai, row):
        entries = []
        bimestres = ["1º Bim", "2º Bim", "3º Bim", "4º Bim"]
        for col, label in enumerate(bimestres):
            ctk.CTkLabel(pai, text=label, text_color=PRETO_SUAVE,
                         font=("Arial", 13)).grid(row=row, column=col, padx=(30 if col == 0 else 10), pady=5)
            e = ctk.CTkEntry(pai, width=80, placeholder_text="0.0")
            e.grid(row=row, column=col + 4, padx=10, pady=5)
            entries.append(e)
        return entries

    def salvar_aluno(self):
        nome  = self.cad_nome.get().strip()
        turma = self.cad_turma.get().strip()

        if not nome or not turma:
            messagebox.showerror("Erro", "Preencha o nome e a turma.")
            return

        try:
            mat  = [float(e.get()) for e in self.cad_mat]
            port = [float(e.get()) for e in self.cad_port]
            hist = [float(e.get()) for e in self.cad_hist]
        except ValueError:
            messagebox.showerror("Erro", "Preencha todas as notas com números válidos (ex: 7.5).")
            return

        for notas in [mat, port, hist]:
            if any(n < 0 or n > 10 for n in notas):
                messagebox.showerror("Erro", "As notas devem ser entre 0 e 10.")
                return

        self.alunos.append({
            "nome": nome, "turma": turma,
            "matematica": mat, "portugues": port, "historia": hist
        })

        messagebox.showinfo("Sucesso", f"Aluno '{nome}' cadastrado com sucesso!")
        self.mostrar_cadastro()

    # =====================
    # TELA 5 - LANÇAR NOTAS
    # =====================
    def mostrar_lancamento(self):
        self.limpar_area()
        self.titulo_tela("Lançar / Editar Notas", "Selecione o aluno e atualize as notas bimestrais")

        if not self.alunos:
            ctk.CTkLabel(self.area, text="Nenhum aluno cadastrado ainda.",
                         font=("Arial", 16), text_color=PRETO_SUAVE).pack(pady=40)
            return

        nomes = [a["nome"] for a in self.alunos]

        linha_sel = ctk.CTkFrame(self.area, fg_color=CINZA_CLARO)
        linha_sel.pack(anchor="w", pady=(0, 18))

        ctk.CTkLabel(linha_sel, text="Aluno:", font=("Arial", 14, "bold"),
                     text_color=PRETO_SUAVE).pack(side="left", padx=(0, 10))

        self.combo_aluno = ctk.CTkComboBox(
            linha_sel, values=nomes, width=260,
            command=self.carregar_notas_aluno
        )
        self.combo_aluno.pack(side="left")

        self.painel_lancamento = ctk.CTkFrame(self.area, fg_color=BRANCO, corner_radius=15)
        self.painel_lancamento.pack(fill="x", padx=5, pady=10)

        self.combo_aluno.set(nomes[0])
        self.carregar_notas_aluno(nomes[0])

    def carregar_notas_aluno(self, nome):
        for w in self.painel_lancamento.winfo_children():
            w.destroy()

        aluno = next((a for a in self.alunos if a["nome"] == nome), None)
        if not aluno:
            return

        self.lan_entries = {}

        for disc_label, disc_chave in [("Matemática", "matematica"),
                                        ("Português", "portugues"),
                                        ("História", "historia")]:
            ctk.CTkLabel(
                self.painel_lancamento,
                text=f"── {disc_label} ──",
                text_color=VERDE_ESCURO, font=("Arial", 14, "bold")
            ).pack(anchor="w", padx=30, pady=(18, 5))

            linha = ctk.CTkFrame(self.painel_lancamento, fg_color=CINZA_CLARO, corner_radius=8)
            linha.pack(fill="x", padx=30, pady=5)

            entries = []
            for i, bim in enumerate(["1º Bim", "2º Bim", "3º Bim", "4º Bim"]):
                ctk.CTkLabel(linha, text=bim, font=("Arial", 13),
                             text_color=PRETO_SUAVE).pack(side="left", padx=(20, 4), pady=12)
                e = ctk.CTkEntry(linha, width=75)
                e.insert(0, str(aluno[disc_chave][i]))
                e.pack(side="left", padx=(0, 18), pady=12)
                entries.append(e)

            self.lan_entries[disc_chave] = entries

        ctk.CTkButton(
            self.painel_lancamento, text="💾  Salvar Notas",
            fg_color=VERDE_ESCURO, hover_color="#1F4D38",
            text_color=BRANCO, font=("Arial", 14, "bold"),
            height=46, width=200,
            command=lambda: self.salvar_notas(nome)
        ).pack(pady=25)

    def salvar_notas(self, nome):
        aluno = next((a for a in self.alunos if a["nome"] == nome), None)
        if not aluno:
            return

        try:
            for disc, entries in self.lan_entries.items():
                novas = [float(e.get()) for e in entries]
                if any(n < 0 or n > 10 for n in novas):
                    raise ValueError
                aluno[disc] = novas
        except ValueError:
            messagebox.showerror("Erro", "Notas inválidas. Use números entre 0 e 10.")
            return

        messagebox.showinfo("Sucesso", f"Notas de '{nome}' atualizadas!")

    # =====================
    # TELA 6 - RELATÓRIO VISUAL
    # =====================
    def mostrar_relatorio(self):
        self.limpar_area()
        self.titulo_tela("Relatório Visual da Turma", "Gráficos de barras com desempenho de cada aluno")

        if not self.alunos:
            ctk.CTkLabel(self.area, text="Nenhum aluno cadastrado.",
                         font=("Arial", 16), text_color=PRETO_SUAVE).pack(pady=40)
            return

        # ---- Gráfico 1: Médias gerais por aluno ----
        secao = ctk.CTkFrame(self.area, fg_color=BRANCO, corner_radius=15)
        secao.pack(fill="x", padx=5, pady=12)

        ctk.CTkLabel(secao, text="Média Geral por Aluno",
                     text_color=VERDE_ESCURO, font=("Arial", 20, "bold")
                     ).pack(anchor="w", padx=25, pady=(20, 10))

        max_media = 10
        for aluno in self.alunos:
            med = self.media_aluno(aluno)
            sit = self.situacao(med)
            cor = VERDE_ESCURO if sit == "Aprovado" else (LARANJA if sit == "Atenção" else VERMELHO)
            self._barra(secao, aluno["nome"], med, max_media, cor)

        ctk.CTkLabel(secao, text="", height=10).pack()

        # ---- Gráfico 2: Médias por disciplina ----
        secao2 = ctk.CTkFrame(self.area, fg_color=BRANCO, corner_radius=15)
        secao2.pack(fill="x", padx=5, pady=12)

        ctk.CTkLabel(secao2, text="Média por Disciplina (turma)",
                     text_color=VERDE_ESCURO, font=("Arial", 20, "bold")
                     ).pack(anchor="w", padx=25, pady=(20, 10))

        disciplinas = [("Matemática", "matematica"), ("Português", "portugues"), ("História", "historia")]
        for nome_d, chave in disciplinas:
            notas = []
            for aluno in self.alunos:
                notas.extend(aluno[chave])
            med = self.media(notas)
            cor = VERDE_ESCURO if med >= 7 else (LARANJA if med >= 6 else VERMELHO)
            self._barra(secao2, nome_d, med, 10, cor)

        ctk.CTkLabel(secao2, text="", height=10).pack()

        # ---- Gráfico 3: Situação da turma (contagem) ----
        secao3 = ctk.CTkFrame(self.area, fg_color=BRANCO, corner_radius=15)
        secao3.pack(fill="x", padx=5, pady=12)

        ctk.CTkLabel(secao3, text="Distribuição de Situações",
                     text_color=VERDE_ESCURO, font=("Arial", 20, "bold")
                     ).pack(anchor="w", padx=25, pady=(20, 10))

        contagem = {"Aprovado": 0, "Atenção": 0, "Em risco": 0}
        for aluno in self.alunos:
            contagem[self.situacao(self.media_aluno(aluno))] += 1

        total = len(self.alunos)
        cores_sit = {"Aprovado": VERDE_ESCURO, "Atenção": LARANJA, "Em risco": VERMELHO}
        for sit, qtd in contagem.items():
            self._barra(secao3, f"{sit} ({qtd} aluno{'s' if qtd != 1 else ''})",
                        qtd, total if total > 0 else 1, cores_sit[sit], sufixo=f"{qtd}")

        ctk.CTkLabel(secao3, text="", height=10).pack()

        # ---- Legenda ----
        legenda = ctk.CTkFrame(self.area, fg_color=CINZA_CLARO, corner_radius=10)
        legenda.pack(fill="x", padx=5, pady=(5, 15))

        for cor, texto in [(VERDE_ESCURO, "Aprovado  ≥ 7.0"),
                           (LARANJA,     "Atenção   6.0 – 6.9"),
                           (VERMELHO,    "Em risco  < 6.0")]:
            bloco = ctk.CTkFrame(legenda, fg_color=cor, width=18, height=18, corner_radius=4)
            bloco.pack(side="left", padx=(20, 6), pady=14)
            ctk.CTkLabel(legenda, text=texto, font=("Arial", 13),
                         text_color=PRETO_SUAVE).pack(side="left", padx=(0, 24))

    def _barra(self, pai, label, valor, maximo, cor, sufixo=None):
        linha = ctk.CTkFrame(pai, fg_color="transparent")
        linha.pack(fill="x", padx=25, pady=5)

        ctk.CTkLabel(linha, text=label, width=220, anchor="w",
                     font=("Arial", 14), text_color=PRETO_SUAVE).pack(side="left")

        proporcao = valor / maximo if maximo > 0 else 0
        largura_total = 500
        largura_barra = max(int(proporcao * largura_total), 6)

        canvas = tk.Canvas(linha, width=largura_total, height=28,
                           bg=CINZA_CLARO, highlightthickness=0)
        canvas.pack(side="left", padx=(10, 10))
        canvas.create_rectangle(0, 4, largura_barra, 24, fill=cor, outline="")
        canvas.create_rectangle(0, 4, largura_total, 24, fill="", outline="#CCCCCC")

        texto_val = sufixo if sufixo else f"{valor:.2f}"
        ctk.CTkLabel(linha, text=texto_val, font=("Arial", 14, "bold"),
                     text_color=cor).pack(side="left")


if __name__ == "__main__":
    app = DetectorPadroesApp()
    app.mainloop()