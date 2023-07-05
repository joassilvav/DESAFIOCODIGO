import dasafio1, desafio2, desafio4

print("Desafio 1- manipulação de string. Revertendo a ordem das palavras. \nDesafio 2 - Removendo duplicados. \n" )
escolha = int(input('Escolha o numero do desafio: '))

match escolha:
    case 1:
        dasafio1.desafioum()

    case 2:
        desafio2.desafioo2()

    case 3:
        print('')
    case 4:
        desafio4.desafiofour()