def desafiofive(palav):
    #transformando a string em palindromo
    palavinv = palav[::-1]

    print(palav == palavinv)
    if palav == palavinv:
        return 'True'
    else:
        return 'False'
    #return 'text'

def getTestedeCaso():
    return 'racecar'