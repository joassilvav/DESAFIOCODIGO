def desafiotree(palav):

    palavinv = palav[::-1]

    cc = ''
   #usando como referência a analise de matrizes para passar por cada letra da palav.
    for i in range(len(palav)):
        for j in range(len(palav)):
            #j>=1 pegando todas as letras de 0:0 até 4:4
            if j >= i:
                string = palavinv[i:j+1]
               #obtendo as substring
                if string in palav:
                #pegando as mais longas substring
                    if len(string) >= len(cc):
                        cc = string

    #printando a mais longa substring
    return cc
def getTestedeCaso():
    return 'babad'