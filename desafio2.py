from collections import OrderedDict

def remov(frase):
     return ''.join(list(OrderedDict.fromkeys(frase)))

def desafioo2():
     texto = str(input('Digite uma frase: '))
     print(remov(texto))