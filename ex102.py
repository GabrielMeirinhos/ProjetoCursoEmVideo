def fatorial(num=1, show=False):
    """
     -> CALCULADORA DE FATORIAL.
    :param num:Recebe um número;
    :param show: (Opicional) Mostrar ou não a conta;
    :return: Retorna o fatorial do número;
    """
    f = 1
    for c in range(num,0,-1):
        f*=c
    for m in range(num, 0, -1):
        if show:
            if m >1:
                print (f"{m} x " , end="")
            else:
                print(f"1 = {f}")
    print('')
    return print(f'O fatorial de {num} é : {f}')


fatorial(10,show=True)
