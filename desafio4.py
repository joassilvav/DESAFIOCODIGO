def desafiofour(p):

    x = [c for c in p]
    x[0] = x[0].capitalize()

    for i in range(len(x)):
        if i > 2:
            #declarando o final de uma frase com a pontuação.
            if x[i - 2] == '.' or x[i - 2] == '?' or x[i - 2] == '!':
                #usando o método capitalize( Coloca a 1ª letra Maiúscula) para resolver o desafio
                x[i] = x[i].capitalize()

    #usando a função join para juntar elementos de uma lista pelo caracter ('') transformando em string
    return ''.join(x)

def getTestedeCaso():
    return "hello. how are you? i'm fine, thank you."
