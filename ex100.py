from random import randint
numeros=[]
def sorteia():
    a=0
    print('Sorteando a lista: ',end="")
    for x in range (0,5):
        a = randint(0,9)
        numeros.append(a)
        print(f'{a}',end=' ')
    print('Pronto!')


def somaPar():
    soma = 0
    for i,v in enumerate(numeros):
        if v%2 == 0:
            soma+=v
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia()
somaPar()