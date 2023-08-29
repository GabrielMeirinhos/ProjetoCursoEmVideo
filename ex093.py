lista=[]
ficha={'nome':str(input('Nome: '))}
x=int(input(f'Quantas partidas {ficha["nome"].title()} jogou: '))
tot=0
for y in range (0,x):
    z = int(input(f'Quantos gols na partida {y+1}: '))
    lista.append(z)
    tot+=z
ficha['gols'] = lista
ficha['total'] = tot
print('-='*30)
print(ficha)
print('-='*30)
for k,v in ficha.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {ficha["nome"].title()} jogou {x} partidas.')
for m,v in enumerate(lista):
    print(f'    => Na partida {m+1}, fez {v}')
print(f'Foi um total de {tot} gols.')
print('-='*30)
