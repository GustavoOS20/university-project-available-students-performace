import numpy as np

def calcular_media(notas):
    if not notas:
        return 0.0
    n = len(notas)
    vetor_notas = np.array(notas)
    vetor_pesos = np.full(n, 1/n)
    return float(np.dot(vetor_notas, vetor_pesos))

def calcular_media_aluno(aluno):
    medias = [
        calcular_media(aluno["matematica"]),
        calcular_media(aluno["portugues"]),
        calcular_media(aluno["historia"])
    ]
    return calcular_media(medias)

def definir_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 6:
        return "Atenção"
    return "Em risco"

def analisar_tendencia(notas):
    if len(notas) < 3:
        return "Estável"
    if notas[-1] < notas[-2] and notas[-2] < notas[-3]:
        return "Queda"
    elif notas[-1] > notas[-2]:
        return "Melhora"
    return "Estável"

def probabilidade_aprovacao(media):
    return min((media / 7) * 100, 100)