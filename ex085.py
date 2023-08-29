lista= [[], []]
for x in range (0,7):
    valor = int(input(f'Digite o {x+1}º valor: '))
    if valor%2==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'Os valores pares digitados foram: {sorted(lista[0])}.')
print(f'Os valores impares digitados foram: {sorted(lista[1])}.')
