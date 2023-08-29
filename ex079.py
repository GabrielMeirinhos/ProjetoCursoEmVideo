lista = []
listacop=[]
x =0
while True:
    if x == 'N':
        break
    lista.append(int(input('Digite um valor: ')))
    if lista[-1] in listacop:
        print('Valor duplicado! Não vou adicionar.')
        lista.pop()
    x=str(input('Deseja continuar [S/N]: '))
    if x in 'Nn':
        break
    elif x not in 'Ss':
        while True:
            x = str(input('Deseja continuar [S/N]: ')).upper()
            if x in 'SN':
                break
    listacop = lista[:]
print(f'Sua lista ficou assim: {sorted(lista)}')
print('Fim do programa!')