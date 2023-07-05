palav = str(input('digite um palindromo: '))
palavinv = palav[::-1]

cc = ''

for i in range(len(palav)):
    for j in range(len(palav)):
        if j >= i:
            string = palavinv[i:j+1]
            if string in palav:
                if len(string) >= len(cc):
                    cc = string


print(cc)