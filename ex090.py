'''if dicti['Média']>= 7:
    print(f'O aluno {dicti["Nome"]} foi aprovado com média: {dicti["Média"]}.')
else:
    print(f'O aluno {dicti["Nome"]} foi reprovado com média: {dicti["Média"]}.')'''
dicti ={'Nome':str(input('Nome: ')),'Média':float(input('Média: ')),'Situação':'Reprovado'}
if dicti['Média']>=7:
     dicti['Situação'] = 'Aprovado'
for k,v in dicti.items():
    print(f"O {k} é igual a {v}.")
