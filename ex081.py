lista=[]
cont = x = 0
while x != 'N':
    lista.append(int(input('Digite um valor: ')))
    cont+=1
    x = str(input('Quer continuar[S/N]: ')).upper()
    if x not in 'NS':
        while x not in 'SN':
            x = str(input('Quer continuar[S/N]: ')).upper()
            if x == 'N':
                break
print(f'Foram digitados {cont} números!')
print(f'Lista: {sorted(lista,reverse=True)} !')
if '5' in lista:
    print('O número 5 apareceuna lista!')
else:
    print('O número 5 não apareceu na lista!')


