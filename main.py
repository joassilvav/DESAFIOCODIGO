import desafio1, desafio2, desafio3, desafio4, desafio5

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
            print(desafio1.getTestedeCaso())
        else:
            print(desafio1.desafioum((str(input('digite a frase:')))))
    case 2:
        esc = int(input('1- Ver frase do desafio \n2- Frase nova \n'))
        if esc == 1:
            print(desafio2.getTestedeCaso())
        else:
            print(desafio2.remov((str(input('digite a frase:')))))
    case 3:
        esc = int(input('1- Ver frase do desafio \n2- Frase nova \n'))
        if esc == 1:
            print(desafio3.getTestedeCaso())
        else:
            print(desafio3.desafiotree((str(input('digite a frase:')))))
    case 4:
        esc = int(input('1- Ver frase do desafio \n2- Frase nova \n'))
        if esc == 1:
            print(desafio4.getTestedeCaso())
        else:
            print(desafio4.desafiofour((str(input('digite a frase:')))))
    case 5:
        esc = int(input('1- Ver frase do desafio \n2- Frase nova \n'))
        if esc == 1:
            print(desafio5.getTestedeCaso())
        else:
            print(desafio5.desafiofive(str(input('digite a frase:'))))
    case _:
        print("Inválido")
