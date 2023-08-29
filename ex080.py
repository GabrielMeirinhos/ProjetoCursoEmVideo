lista=[]
for x in range (0,5):
    n = int(input('Digite um valor: '))
    if x == 0 or n > lista[-1]:
        lista.append(n)
        print('Seu valor foi adicionado no final da lista.')
    else:
        pos = 0
        while True:
            if n < lista[pos]:
                lista.insert(pos,n)
                print(f'Seu valor foi adicionado na posição {pos}.')
                break
            pos+=1
print(f'Sua lista:{lista}')

