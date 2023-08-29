from random import randint
from time import sleep
from operator import itemgetter
lista =[]
dicionario={'jogador0':randint(1,6),'jogador1':randint(1,6),'jogador2':randint(1,6),'jogador3':randint(1,6)}
ranking = []
ranking = sorted(dicionario.items(), key= itemgetter(1), reverse=True)
print('DADOS LANÇADOS:')
for k,v in dicionario.items():
    print(f'    O {k} tirou {v}.')
print('RANKING DOS JOGADORES: ')
for i, v in enumerate(ranking):
    print(f'    O {v[0]} ficou em na {i+1}º posição com {v[1]} pontos!!')