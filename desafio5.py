def desafiofive():
    palav = str(input('digite um palindromo: ')).lower()
    palavinv = palav[::-1]

    print(palav == palavinv)