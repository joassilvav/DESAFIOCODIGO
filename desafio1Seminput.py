def desafio1seminput():
# declarando a variÃ¡vel para receber a string
    frases = 'Hello, Word! OpenAI is amazing.'
    #frases = frases.strip()

# usando a função
    frase_esplitada = ((splitando(frases)))
#1 tentativa
    k = ""
    for x in range(len(frase_esplitada)):
        k += frase_esplitada[-1 - x] + " "
    print(k.strip())

# colocando em List comprehension.
    [print(frase_esplitada[-1-x], end=" ") for x in range(len(frase_esplitada))]

def splitando(frase):
    return frase.split(" ")