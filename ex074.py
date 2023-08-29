'''from random import randint
x  = cont = maior = menor = 0
tupla = 0,1,2,3,4,5,6,7,8,9,10
s1 = s2 = s3 = 0
print('Os númeors sorteados foram: ',end='')
for sorteio in range (0,5):
    x = randint(0, 10)
    if x:
        s1 = x
        s2=s1
        s3=s2
        s3 = s1+s2
    print(s1,end=' ' if sorteio != 4 else '\n')
    if sorteio == 1:
        maior = menor = x
    if maior<x:
        maior = x
    elif menor>x:
        menor = x
print(f'O menor número foi {menor} e o maior foi {maior}')'''
import random

# Sorteia 5 números de 0 a 9
numeros = [random.randint(0, 9) for i in range(5)]

# Encontra o menor e o maior número
menor = min(numeros)
maior = max(numeros)

# Imprime os resultados
print("Números sorteados:", numeros)
print("Menor número:", menor)
print("Maior número:", maior)
