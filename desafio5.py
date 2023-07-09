def desafiofive(palav):
    #transformando a string em palindromo
    palavinv = palav[::-1]

    print(palav == palavinv)
    if palav.lower() == palavinv.lower():
        return 'True'
    else:
        return 'False'
    #return 'text'

def getTestedeCaso():
    return 'racecar'
