cont = 0
número=(int(input('Digite um número: ')),int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),int(input('Digite o último número: ')))
for par  in range(0,len(número)):
        if número[par]%2==0:
                cont+=1
print(f'O valor 9 apareceu {número.count(9)} vezes.')
print(f'Apareceram {cont} valores pares.')
if 3 in número:
        print(f'O número 3 aparce a primeira vez na posição {número.index(3)+1}!')
else:
        print('O valor 3 não foi escolhido.')