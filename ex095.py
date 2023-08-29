time=[]
jogadores={}
gol=[]
tot = g = n = 0
while True:
    jogadores={'nome':str(input('Nome: '))}
    n+=1
    partidas=int(input(f'Quantos jogos {jogadores["nome"]} jogou: '))
    for p in range(0,partidas):
        g = int(input(f'Quantos gols na {p + 1}º partida: '))
        gol.append(g)
        tot+=g
    jogadores['total']=tot
    jogadores['gols']=gol[:]
    time.append(jogadores)
    gol.clear()
    tot=0
    cont= str(input('Deseja continuar [S/N]: '))
    if cont in 'Nn':
        break
print('-='*40)
print(f'{"cod nome":<15}{"gols":>15}{"total":>15}')
print('-'*80)
for i,v in enumerate(time):
    print(f"{i} {(time[i]['nome']).title():<15}{(str(time[i]['gols'])):>15} {time[i]['total']:>15}")
print("=-"*40)
resp = int(input("Que mostrar os dados de qual jogador [999 para parar]: "))
while True:
    if resp > n or resp == 999:
        while True:
            if resp < len(jogadores["nome"]) or resp == 999:
                break
            resp = int(input("NÃO EXISTE JOGADOR COM ESSE VALOR, TENTE NOVAMENTE!![999 para parar]: "))

    if resp <= n:
        print(f"LEVANTAMENTO DO JOGADOR {str(time[resp]['nome']).upper()}:")
        for x in range(0,int(len(time[resp]["gols"]))):
            print(f'No jogo {x+1} fez {time[resp]["gols"][x]}')
    print("=-"*40)
    if resp == 999:
        print("=-" * 40)
        break
    resp=int(input("Quer mostrar os dados de qual jogador [999 para parar]: "))
    if resp == 999:
        print("=-" * 40)
        break


