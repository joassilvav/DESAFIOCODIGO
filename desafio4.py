
p = "hello, \thow are you? \ti'm fine,\tthank you."
x =(p.split('\t'))
nvv = []
for i in x:
    j = i.capitalize()
    nvv.append(j)
print(nvv)
print(''.join(nvv))


