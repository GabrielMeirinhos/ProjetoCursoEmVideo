x = 0
lista=[]
par=[]
impar=[]
while not x == 'N':
    lista.append(int(input('Digite um número: ')))
    x = str(input('Deseja continuar[S/N]: ')).upper()
    while x not in 'SN':
        x = str(input('Deseja continuar[S/N]: ')).upper()
for p in lista:
    if p%2==0:
        par.append(p)
    elif p%2==1:
        impar.append((p))

print(f'Lista original: {sorted(lista)}.')
if len(par)>0:
    print(f'Lista dos pares: {par}')
else:
    print('Não houve números pares.')
if len(impar)>0:
    print(f'Lista dos impares: {impar}')
else:
    print('Não houve números impares.')
