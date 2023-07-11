def desafioum(frases):

# usando a função
    frase_esplitada = ((splitando(frases)))

# colocando em List comprehension.
    nv = [(frase_esplitada[-1-x] ) for x in range(len(frase_esplitada))]
    return ' '.join(nv)
def splitando(frase):
    return frase.split(" ")

def getTestedeCaso():
    return 'Hello, Word! OpenAI is amazing'





#1 tentativa
    #k = ""
    #for x in range(len(frase_esplitada)):
     #   k += frase_esplitada[-1 - x] + " "
    #return k.strip()
