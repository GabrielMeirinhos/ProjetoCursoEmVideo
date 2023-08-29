tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FUTURO')
for x in tupla:
    print(f'A sua palavra escolhida foi {x} e existem as vogais: ',end="")
    for p in x:
        if p in"AEIOU":
            print(f"{p} ",end="")
    print("")