from collections import OrderedDict

#criando a função
def remov(frase):
     # transformando em dicionario e lista para usar o .join(junta lista dentro de uma string, nessa caso é o '')
     return ''.join(list(OrderedDict.fromkeys(frase)))

def desafioo2():
     texto = str(input('Digite uma frase: '))
     print(remov(texto))