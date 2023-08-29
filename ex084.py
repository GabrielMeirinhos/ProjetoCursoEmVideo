pessoas = gordo = magro = 0
pesadas=[]
leves=[]
lista=[]
dados=[]
while True:
    dados.append(str(input('Nome: ').title()))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    x = str(input('deseja continuar[S/N]: '))
    if pessoas == 0:
        gordo = magro = lista[0][1]
    if gordo < lista[pessoas][1]:
        gordo = lista[pessoas][1]
    if magro > lista[pessoas][1]:
        magro = lista[pessoas][1]
    pessoas+=1
    if x in 'Nn':
        break
for p,c in enumerate(lista):
    if gordo == c[1]:
        pesadas.append(lista[p][0])
    elif magro == c[1]:
        leves.append(lista[p][0])

print(f'Ao todo, você cadastrou {pessoas} pessoas.')
print(f'O maior peso foi {gordo}.Peso de: {pesadas}.')
print(f'O menor peso foi {magro}.Peso de: {leves}.')
