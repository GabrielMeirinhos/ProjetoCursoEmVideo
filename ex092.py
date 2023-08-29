from datetime import date
x = date.today()
dici={'nome':str(input('NOME: '))}
m = int(input('ANO DE NASCIMENTO: '))
dici={'idade':(x.year-m)}
dici={'CTPS': int(input('CTPS(0 NÃO TEM): '))}
if dici['CTPS'] != 0:
    dici['contratação']= int(input('ANO DE CONTRATAÇÃO: '))
    dici['salario']= float(input('SALÁRIO: '))
    dici['aposentadoria']= (-m+dici['contratação']+35)
for k,v in dici.items():
    print(f'{k} tem o valor {v}.')
