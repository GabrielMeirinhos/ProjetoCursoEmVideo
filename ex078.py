p = d = 0
lista = []
listamax = []
listamin =[]
for x in range (0,5):
    lista.append(int(input(f'Digite um valor para a posição {x}: ')))
listarec = lista[:]
listamrec= lista[:]
for v in lista:
    if max(lista) == v:
        listamax.append(listarec.index(max(lista))+d)
        listarec.remove(max(listarec))
        d+=1
for aa in lista:
    if min(lista) == aa:
        listamin.append(listamrec.index(min(lista))+p)
        listamrec.remove(min(listamrec))
        p+=1

print(f'Você digitou os valores: {lista}')
if len(listamin)>1:
    print(f'O valor mínimos foi {min(lista)} e ficaram nas posições: {listamin}.')
else:
    print(f'O valor mínimo foi {min(lista)} e ficou na posição: {lista.index(min(lista))}.')
if len(listamax)>1:
    print(f'O valor máximo foi {max(lista)} e ficaram nas posições: {listamax}.')
else:
    print(f'O valor máximo foi {max(lista)} e ficou na posição: {lista.index(max(lista))}.')