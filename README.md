# 📊 Detector de Padrões de Aprendizado

Uma aplicação desktop desenvolvida em Python com uma interface gráfica moderna para monitorar, analisar e detectar padrões de desempenho acadêmico de alunos. O sistema permite o cadastro de notas, cálculo automático de médias, identificação de tendências (melhora, queda ou estabilidade) e visualização de dados por meio de dashboards e relatórios gráficos.

## ✨ Funcionalidades

O aplicativo está dividido em 6 módulos principais:

* **📊 Dashboard Principal:** Visão geral da turma, exibindo a média geral, total de alunos, alunos em risco e chances de aprovação. Inclui um resumo por disciplina com identificação de tendências.
* **👥 Todos os Alunos:** Tabela completa com as notas bimestrais, médias finais e a situação (Aprovado, Atenção, Em risco) de cada estudante. Permite a exclusão de registros.
* **📚 Análise por Disciplina:** Visão detalhada do desempenho em Matemática, Português e História. Gera sugestões automáticas de foco de estudo baseadas nos resultados da turma.
* **➕ Cadastrar Aluno:** Formulário intuitivo para inserir novos alunos, suas turmas e as notas dos 4 bimestres em cada matéria.
* **📝 Lançar Notas:** Interface dedicada para atualizar e editar notas de alunos já cadastrados no sistema.
* **📈 Relatório Visual:** Geração de gráficos de barras horizontais nativos (sem dependências externas pesadas) que ilustram a média por aluno, média por disciplina e a distribuição de alunos por situação.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x:** Linguagem base do projeto.
* **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter):** Biblioteca principal utilizada para criar a interface gráfica moderna, com cantos arredondados e cores customizadas.
* **Tkinter:** Utilizado para manipulação do Canvas (nos gráficos do relatório) e caixas de diálogo (MessageBox).

## 🎨 Paleta de Cores do Projeto

O design do aplicativo utiliza um modo de aparência claro (`light mode`) com a seguinte paleta de cores para facilitar a leitura e indicar status:

| Cor | Hexadecimal | Uso Principal |
| :--- | :--- | :--- |
| **Verde Lima** | `#80B918` | Botões do menu, interações de *hover*. |
| **Verde Escuro** | `#2D6A4F` | Menu lateral, títulos, status "Aprovado". |
| **Preto Suave** | `#1B1B1B` | Textos padrão, dados nas tabelas. |
| **Cinza Claro** | `#E9ECE5` | Fundo principal da área de conteúdo. |
| **Branco** | `#FFFFFF` | Fundo dos cartões e painéis, texto de destaque. |
| **Vermelho** | `#D00000` | Alertas, botões de exclusão, status "Em risco". |
| **Laranja** | `#C76A00` | Status de "Atenção". |

## 🚀 Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Você precisará instalar a biblioteca `customtkinter`.

### Passo a Passo

1.  **Clone o repositório** (ou baixe o arquivo `.py`):
    ```bash
    git clone https://github.com/GustavoOS20/university-project-available-students-performace.git
    cd DETECTOR_APRENDIZAGEM
    ```

2.  **Instale as dependências:**
    ```bash
    pip install customtkinter
    ```

3.  **Execute a aplicação:**
    ```bash
    python main.py
    ```

> **Nota:** O sistema já vem com dados "mockados" (fictícios) de quatro alunos para facilitar a visualização inicial e os testes das métricas de aprovação e relatórios visuais.

## 🧠 Lógica de Avaliação

O sistema utiliza os seguintes critérios para classificar os alunos:
* **Aprovado:** Média geral $\ge 7.0$
* **Atenção:** Média geral entre $6.0$ e $6.9$
* **Em risco:** Média geral $< 6.0$

A **tendência** é calculada comparando as notas dos últimos bimestres para identificar se o aprendizado está em progressão, retrocesso ou se mantém estável ao longo do ano letivo.

> **Nota:** Como o tempo fez com que não fosse possível o versionamento correto do código, coloquei a versão de cada um em uma branch e, por fim, separei o código em arquivos com responsabilidades bem definidas.

## Link para Download
https://drive.google.com/drive/folders/1Ve2MLXTTSqom1UV2URqS0C5If6rMT7nO?usp=sharing
```
