matriz = [[0,0,0],[0,0,0],[0,0,0]]
maior = pares = terceiracoluna = 0
for l in range (0,3):
    for c in range(0,3):
        matriz[l][c]= int(input(f'Digite um valor para [{l+1},{c+1}]: '))
        if matriz[l][c] % 2==0:
            pares+=matriz[l][c]
    terceiracoluna+=matriz[l][2]
    if matriz[1][0] or maior < matriz[1][c]:
        maior = matriz[1][c]
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]',end='')

    print()
print(f'A soma de todos os valores pares foi: {pares}.')
print(f'A soma dos valores da terceira coluna foi: {terceiracoluna}.')
print(f'O maior valor da segunda linha foi: {maior}.')
