def desafiofourseminput():
    p = "hello. how are you? i'm fine, thank you."
    #x =(p.split('\t'))
    nvv = []
    x = [c for c in p]
    x[0] = x[0].capitalize()

    for i in range(len(x)):
        if i > 2:
            if x[i - 2] == '.' or x[i - 2] == '?' or x[i - 2] == '!':
                x[i] = x[i].capitalize()
        #j = i.capitalize()
        #nvv.append(j)
    #print(nvv)
    print(''.join(x))