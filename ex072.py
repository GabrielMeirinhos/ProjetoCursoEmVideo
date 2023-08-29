número = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = x =0
while True:
        x = int(input('Digite um número para recebe-lo por extenso[0 a 20]: '))
        if x<=20 and x>=0:
            print(f'O seu número escolhido foi {número[x]}.')
            continuar = input('Deseja continuar[sim/não]: ')
            if continuar in 'nãonaoNÃONAO':
                print('Fim do programa! Volte sempre')
                break
        else:
            print('Tente novamente! ',end='')