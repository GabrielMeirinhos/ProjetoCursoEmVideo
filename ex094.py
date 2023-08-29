tot = soma = media =0
lista =[]
dados={}
mulheres=[]
idosos=[]
while True:
    dicti={'nome':str(input('NOME:')).title().strip(),'sexo':str(input('SEXO[M/F]: ')),'idade':int(input('IDADE: '))}
    x= str(input('CONTINUAR[S/N]: '))
    lista.append(dicti)
    tot+=1
    soma +=dicti['idade']
    if dicti['sexo'] in 'fF':
        mulheres.append(dicti['nome'])
    if x in 'Nn':
        break
media = soma/tot
for u in range(0,tot):
    if lista[u]['idade']>media:
        idosos.append(lista[u])

print(f'- O grupo tem {tot} pessoas.')
print(f'- A média de idade é {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}.')
print('Lista de pessoas que estão acima da média:')
for m,n in enumerate(idosos):
    print(f'nome = {idosos[m]["nome"]}; sexo = {idosos[m]["sexo"]}; idade = {idosos[m]["idade"]};')
