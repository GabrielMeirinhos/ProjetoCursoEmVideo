'''Crie um programa que leia nome e duas notas de vários alunos e
 guarde tudo em uma lista composta.No final, mostre um boletim
  contendo a média de cada um e permita que o usuário
 possa mostrar as notas de cada aluno individualmente.'''
lista=[]

y =0
while True:
    lista.append([])
    lista[0].append(str(input('Aluno:')))
    lista[0].append(float(input('Av1: ')))
    lista[0].append(float(input('Av2: ')))
    cont=(str(input('Deseja continuar[S/N]: ')))
    if cont in 'Nn':
        break
for p,x in enumerate(lista):
    print(lista[p][0])

