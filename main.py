import dasafio1, desafio2, desafio4, desafio1Seminput, desafio2Seminput
import desafio3
import desafio5

print("Desafio 1- manipulação de string. Revertendo a ordem das palavras. "
      "\nDesafio 2 - Removendo duplicados. "
      "\nDesafio 3- Encontrar Substring palindroma. "
      "\nDesafio 4 - Colocar em letra maiúscula a primeira letra de cada frase. "
      "\nDesafio 5 - Verificar se a string é um anagrama de um polímero."
      "\n"   )
escolha = int(input('Escolha o numero do desafio: '))

match escolha:
    case 1:
        esc = int(input('1- Ver frase do desafio \n2- Frase nova \n'))
        if esc == 1:
            desafio1Seminput.desafio1seminput()
        else:
            dasafio1.desafioum()
    case 2:
        esc = int(input('1- Ver frase do desafio \n2- Frase nova \n'))
        if esc == 1:
            desafio2Seminput.desafioo2semimput()
        else:
            desafio2.desafioo2()
    case 3:
        desafio3.desafiotree()
    case 4:
        desafio4.desafiofour()
    case 5:
        desafio5.desafiofive()
    case _:
        print("Inválido")
