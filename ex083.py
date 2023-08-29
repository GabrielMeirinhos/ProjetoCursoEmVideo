x = input('Digite uma expreção: ')
a = b = cont = 0
while not len(x) == cont:
    if '(' in x :
        a +=1
    elif ')' in x:
        b +=1
    cont+=1
if a == b:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida!')
print(a,b)