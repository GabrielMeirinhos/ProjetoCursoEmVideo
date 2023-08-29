from random import sample
from time import sleep
lista=[]
num = list(range(1,61))
print('-'*30) 
print(F'{"JOGA NA MEGASENA":^30}')
print('-'*30)
quantidade = int(input('Quantas jogos você quer sortear: '))
for x in range(0,quantidade):
    lista.append(sample(num,6))
print(f'-=-=-=  SORTEANDO OS {quantidade} JOGOS =-=-=-')
for x in range(0,quantidade):
    print(f'Jogo {x+1}: {sorted(lista[x])}')
    sleep(0.3)
print(f'-=-=-=-=-=< BOA SORTE >-=-=-=-=-=')